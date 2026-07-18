---
title: "[Solution] MySQL Foreign Key Constraint Fails - Fix Referential Integrity"
description: "Fix MySQL foreign key constraint fails by ordering operations, checking parent rows, and using SET NULL or CASCADE options properly"
tools: ["mysql"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# MySQL Foreign Key Constraint Fails

This error occurs when an `INSERT` or `UPDATE` on a child table references a value that does not exist in the parent table, or when a `DELETE` on a parent table would orphan child rows.

## What This Error Means

MySQL returns this error when a foreign key constraint is violated:

```
ERROR 1452 (23000): Cannot add or update a child row: a foreign key constraint fails
(`mydb.orders`, CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`))
```

The error includes the constraint name, the child table, the foreign key columns, and the parent table. InnoDB enforces foreign key constraints by default.

## Why It Happens

- The parent row does not exist when inserting a child row
- Updating a parent key value that is referenced by child rows
- Deleting a parent row that has dependent child rows
- Bulk loading data in the wrong order (children before parents)
- The parent table is missing a row that should exist
- Data type mismatch between parent and child columns
- The parent column is not a `PRIMARY KEY` or does not have a `UNIQUE` index

## How to Fix It

### 1. Ensure Parent Rows Exist

```sql
-- Check if the referenced customer exists
SELECT * FROM customers WHERE id = 999;

-- Create the parent row first
INSERT INTO customers (id, name) VALUES (999, 'New Customer');

-- Now the child insert succeeds
INSERT INTO orders (customer_id, product) VALUES (999, 'Widget');
```

### 2. Use ON DELETE and ON UPDATE Options

```sql
-- Automatically delete child rows when parent is deleted
ALTER TABLE orders
    DROP FOREIGN KEY orders_ibfk_1,
    ADD CONSTRAINT orders_ibfk_1
    FOREIGN KEY (customer_id) REFERENCES customers(id)
    ON DELETE CASCADE ON UPDATE CASCADE;
```

### 3. Disable Foreign Key Checks Temporarily

```sql
-- For bulk imports
SET FOREIGN_KEY_CHECKS = 0;

-- Load data in any order
LOAD DATA INFILE '/path/to/orders.csv' INTO TABLE orders;
LOAD DATA INFILE '/path/to/customers.csv' INTO TABLE customers;

-- Re-enable and validate
SET FOREIGN_KEY_CHECKS = 1;

-- Verify constraints
CHECK TABLE orders;
```

### 4. Fix Data Type Mismatch

```sql
-- The parent and child columns must have matching types
-- WRONG: INT vs BIGINT
CREATE TABLE parent (id INT PRIMARY KEY);
CREATE TABLE child (parent_id BIGINT REFERENCES parent(id));

-- CORRECT: matching types
CREATE TABLE child (parent_id INT REFERENCES parent(id));
```

### 5. Find Orphaned Rows

```sql
-- Find child rows with no matching parent
SELECT o.id, o.customer_id
FROM orders o
LEFT JOIN customers c ON o.customer_id = c.id
WHERE c.id IS NULL;
```

## Common Mistakes

- Setting `FOREIGN_KEY_CHECKS = 0` and forgetting to re-enable it -- all foreign key constraints are bypassed for the entire session
- Using `ON DELETE CASCADE` without understanding that it silently deletes dependent data
- Not creating a `UNIQUE` index on the parent column referenced by the foreign key
- Mixing data types between parent and child columns (e.g., `INT` vs `BIGINT`)
- Loading child table data before parent table data in migration scripts

## Related Pages

- [MySQL Duplicate Entry](/tools/mysql/mysql-duplicate-entry)
- [MySQL Table Does Not Exist](/tools/mysql/mysql-table-doesnt-exist)
- [MySQL Data Too Long](/tools/mysql/mysql-data-too-long)
- [PostgreSQL Foreign Key Violation](/tools/postgresql/pg-foreign-key-violation)
