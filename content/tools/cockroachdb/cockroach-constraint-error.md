---
title: "[Solution] CockroachDB Constraint Error - Fix Check Constraint Violation"
description: "Fix CockroachDB check constraint violations. Resolve data integrity constraint errors and fix invalid data writes."
tools: ["cockroachdb"]
error-types: ["constraint-error"]
severities: ["error"]
weight: 5
---

This error means a write operation violated a check constraint on the table. CockroachDB rejects the data to maintain integrity.

## What This Error Means

When a check constraint is violated, you see:

```
ERROR: Check violation for constraint <name>
# or
ERROR: value for column <col> violates check constraint
# or
SQLSTATE 23514: check constraint violated
```

Check constraints ensure data values meet specific conditions. Violations occur when inserted or updated data does not satisfy the constraint expression.

## Why It Happens

- The data being inserted does not satisfy the check constraint
- An update changes a column value to one that violates the constraint
- The constraint expression has a logic error
- Migration scripts insert data before the constraint is properly defined
- Application code does not validate data before writing
- The constraint was added to a table with existing invalid data

## How to Fix It

### Check existing constraints

```sql
SHOW CREATE TABLE orders;
```

Review the constraint definition to understand what values are allowed.

### Verify the failing data

```sql
SELECT * FROM orders WHERE amount < 0;
```

Find rows that would violate the constraint.

### Fix the data before adding the constraint

```sql
UPDATE orders SET amount = 0 WHERE amount < 0;
ALTER TABLE orders ADD CONSTRAINT chk_amount CHECK (amount >= 0);
```

### Temporarily disable the constraint (not recommended)

```sql
ALTER TABLE orders DROP CONSTRAINT chk_amount;
-- Make changes
ALTER TABLE orders ADD CONSTRAINT chk_amount CHECK (amount >= 0);
```

### Use NOT NULL constraints for required fields

```sql
ALTER TABLE orders ALTER COLUMN amount SET NOT NULL;
```

### Add constraints with NOT VALID option

```sql
ALTER TABLE orders ADD CONSTRAINT chk_amount CHECK (amount >= 0) NOT VALID;
```

NOT VALID skips validation of existing rows but enforces for new writes.

### Validate the constraint later

```sql
ALTER TABLE orders VALIDATE CONSTRAINT chk_amount;
```

Validates existing data without locking the table for writes.

### Check constraint details

```sql
SELECT * FROM [SHOW CONSTRAINTS FROM orders];
```

### Use multiple constraints

```sql
ALTER TABLE orders ADD CONSTRAINT chk_amount_positive CHECK (amount >= 0);
ALTER TABLE orders ADD CONSTRAINT chk_amount_max CHECK (amount <= 1000000);
```

### Document constraint requirements

```sql
COMMENT ON CONSTRAINT chk_amount ON orders IS 'Ensures order amount is non-negative';
```

## Common Mistakes

- Adding constraints without first validating existing data
- Using NOT VALID without following up with VALIDATE
- Not testing constraints with edge cases before deployment
- Assuming constraints are automatically checked on existing data
- Forgetting that constraints apply to updates, not just inserts

## Related Pages

- [CockroachDB Serializable Error]({{< relref "/tools/cockroachdb/cockroach-serializable-error" >}}) -- transaction isolation
- [CockroachDB Schema Change]({{< relref "/tools/cockroachdb/cockroach-schema-change" >}}) -- schema issues
- [CockroachDB Timeout]({{< relref "/tools/cockroachdb/cockroach-timeout" >}}) -- timeouts
