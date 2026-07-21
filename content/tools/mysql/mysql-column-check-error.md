---
title: "[Solution] MySQL Column Check Constraint Error"
description: "Fix MySQL column check constraint error when inserted data violates a CHECK constraint defined on the table"
tools: ["mysql"]
error-types: ["tool-error"]
severities: ["error"]
---

# MySQL Column Check Constraint Error

An INSERT or UPDATE statement violates a CHECK constraint defined on a column. MySQL rejects the operation and returns the constraint name and failing expression.

## Common Causes

- Inserted value falls outside the CHECK constraint range
- Data type mismatch between the value and the constraint expression
- UPDATE changes a column to a value that violates the constraint
- CHECK constraint references another column in the same row
- Bulk INSERT contains rows that fail the constraint

## How to Fix

### Identify the Failing Constraint

```sql
-- View all CHECK constraints on a table
SELECT
  CONSTRAINT_NAME,
  CHECK_CLAUSE
FROM INFORMATION_SCHEMA.CHECK_CONSTRAINTS
WHERE TABLE_NAME = 'products';
```

### Fix the Data

```sql
-- If the constraint requires price > 0
-- Bad: inserting negative price
INSERT INTO products (name, price) VALUES ('Widget', -5);

-- Good: valid price
INSERT INTO products (name, price) VALUES ('Widget', 9.99);
```

### Use Conditional Inserts

```sql
-- Only insert if constraint is satisfied
INSERT INTO products (name, price, stock)
SELECT 'Widget', 9.99, 100
WHERE 9.99 > 0 AND 100 >= 0;
```

### Modify or Drop the Constraint

```sql
-- Drop a specific constraint
ALTER TABLE products DROP CHECK chk_price_positive;

-- Add a less restrictive constraint
ALTER TABLE products ADD CONSTRAINT chk_price_valid
  CHECK (price >= -100 AND price <= 1000000);
```

### Handle Bulk Operations Gracefully

```sql
-- Use INSERT IGNORE to skip failing rows
INSERT IGNORE INTO products (name, price)
VALUES ('Widget', -5), ('Gadget', 10.00);

-- Or use ON DUPLICATE KEY behavior
SET @valid_price = GREATEST(@input_price, 0);
INSERT INTO products (name, price) VALUES ('Widget', @valid_price);
```

## Examples

```
ERROR 3819 (HY000): Check constraint 'chk_price_positive' is violated.

ERROR 3819 (HY000): Check constraint 'chk_age_range' is violated.
  Table: users, Expression: (age >= 0 AND age <= 150)
```

## Related Errors

- [MySQL Foreign Key Constraint]({{< relref "/tools/mysql/mysql-foreign-key-constraint" >}}) -- FK violations
- [MySQL Data Truncated]({{< relref "/tools/mysql/mysql-data-truncated" >}}) -- data truncation
- [MySQL Data Too Long]({{< relref "/tools/mysql/mysql-data-too-long" >}}) -- length violations
