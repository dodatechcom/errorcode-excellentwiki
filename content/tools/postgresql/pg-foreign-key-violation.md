---
title: "[Solution] PostgreSQL Foreign Key Constraint Fails - Fix Referential Integrity"
description: "Fix PostgreSQL foreign key constraint violation errors by aligning referenced values, ordering operations, and disabling constraints safely"
tools: ["postgresql"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# PostgreSQL Foreign Key Constraint Fails

This error occurs when an `INSERT` or `UPDATE` operation on a child table references a value in the parent table that does not exist, or when a `DELETE` on a parent table would leave orphaned rows in the child table.

## What This Error Means

PostgreSQL foreign key constraints enforce referential integrity between related tables. When you violate this constraint, the database rejects the operation:

```
ERROR: insert or update on table "orders" violates foreign key constraint "orders_customer_id_fkey"
DETAIL: Key (customer_id)=(999) is not present in table "customers".
```

The error includes the constraint name, the table being modified, the key value that is missing, and the parent table it references. This makes it straightforward to identify the broken reference.

## Why It Happens

- Inserting a row with a foreign key value that does not exist in the parent table
- Deleting a parent row that is referenced by child rows (without `ON DELETE CASCADE`)
- Updating a parent key value that is referenced by child rows (without `ON UPDATE CASCADE`)
- Bulk loading data without respecting the order of parent and child tables
- The parent table is missing a row that should exist
- A typo or data corruption causes a foreign key value to reference the wrong ID

## How to Fix It

### 1. Ensure Parent Rows Exist Before Inserting

```sql
-- Check if the referenced customer exists
SELECT * FROM customers WHERE id = 999;

-- If not, create it first
INSERT INTO customers (id, name) VALUES (999, 'New Customer');

-- Now the child insert succeeds
INSERT INTO orders (customer_id, product) VALUES (999, 'Widget');
```

### 2. Use ON DELETE CASCADE

```sql
-- Automatically delete child rows when parent is deleted
ALTER TABLE orders
    DROP CONSTRAINT orders_customer_id_fkey,
    ADD CONSTRAINT orders_customer_id_fkey
    FOREIGN KEY (customer_id) REFERENCES customers(id)
    ON DELETE CASCADE;
```

### 3. Order Operations in Bulk Loads

```sql
-- Insert parent rows first, then child rows
-- Disable foreign key checks temporarily if needed
SET session_replication_role = replica;

-- Load parent data
COPY customers FROM '/path/to/customers.csv';

-- Load child data
COPY orders FROM '/path/to/orders.csv';

-- Re-enable constraints
SET session_replication_role = origin;

-- Validate constraints that were skipped
ALTER TABLE orders VALIDATE CONSTRAINT orders_customer_id_fkey;
```

### 4. Use DEFERRABLE Constraints for Transaction-Order Flexibility

```sql
-- Make the constraint check at COMMIT time, not at statement time
ALTER TABLE orders
    ADD CONSTRAINT orders_customer_id_fkey
    FOREIGN KEY (customer_id) REFERENCES customers(id)
    DEFERRABLE INITIALLY DEFERRED;

-- Now you can insert in any order within the transaction
BEGIN;
INSERT INTO orders (customer_id, product) VALUES (999, 'Widget');
INSERT INTO customers (id, name) VALUES (999, 'New Customer');
COMMIT;
```

### 5. Find Orphaned Rows

```sql
-- Find child rows that reference nonexistent parents
SELECT o.id, o.customer_id
FROM orders o
LEFT JOIN customers c ON o.customer_id = c.id
WHERE c.id IS NULL;
```

## Common Mistakes

- Disabling `session_replication_role` in production without re-enabling it -- constraints are skipped for all sessions until you reset it
- Using `ON DELETE CASCADE` without understanding that it silently removes data
- Not adding indexes on foreign key columns -- this causes slow `DELETE` and `UPDATE` operations on the parent table
- Assuming foreign keys are checked on every statement -- `DEFERRABLE` constraints are only checked at `COMMIT` time by default
- Bulk loading data in alphabetical table order instead of dependency order

## Related Pages

- [PostgreSQL Duplicate Key](/tools/postgresql/pg-duplicate-key)
- [PostgreSQL Null Violation](/tools/postgresql/pg-null-violation)
- [PostgreSQL Permission Denied](/tools/postgresql/pg-permission-denied)
- [MySQL Foreign Key Constraint](/tools/mysql/mysql-foreign-key-constraint)
