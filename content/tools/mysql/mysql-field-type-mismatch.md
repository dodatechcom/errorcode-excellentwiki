---
title: "[Solution] MySQL Field Type Mismatch Error"
description: "Fix MySQL field type mismatch error when inserting or comparing values with incompatible column data types"
tools: ["mysql"]
error-types: ["tool-error"]
severities: ["error"]
---

# MySQL Field Type Mismatch Error

A data type mismatch occurs when a value is inserted into or compared against a column of an incompatible type. MySQL may silently convert or reject the operation depending on strict mode.

## Common Causes

- String value inserted into a numeric column
- Datetime string does not match the expected format
- Integer overflow when inserting into a SMALLINT column
- Comparing VARCHAR with BINARY column
- Implicit type conversion causes incorrect query results
- ENUM column receives a value not in the defined list

## How to Fix

### Cast Values Explicitly

```sql
-- Instead of relying on implicit conversion
INSERT INTO products (price, quantity) VALUES (CAST('19.99' AS DECIMAL(10,2)), CAST('5' AS UNSIGNED));

-- Use CONVERT for comparison
SELECT * FROM logs WHERE CONVERT(log_time, CHAR) = '2025-01-15';
```

### Match Column Types in INSERT

```sql
-- If price is DECIMAL(10,2)
INSERT INTO products (price) VALUES (19.99);   -- correct
INSERT INTO products (price) VALUES ('19.99');  -- implicit conversion (works but risky)
INSERT INTO products (price) VALUES (19);       -- truncated to 19.00
```

### Use Proper Date Formats

```sql
-- MySQL expects: 'YYYY-MM-DD HH:MM:SS'
INSERT INTO events (created_at) VALUES ('2025-01-15 10:30:00');

-- For other formats, use STR_TO_DATE
INSERT INTO events (created_at)
VALUES (STR_TO_DATE('15/01/2025 10:30', '%d/%m/%Y %H:%i'));
```

### Check ENUM Values

```sql
-- Verify valid ENUM values
SHOW COLUMNS FROM orders LIKE 'status';
-- status: enum('pending','processing','shipped','delivered','cancelled')

INSERT INTO orders (status) VALUES ('pending');  -- correct
INSERT INTO orders (status) VALUES ('shipped');  -- correct
INSERT INTO orders (status) VALUES ('unknown');  -- ERROR 1265
```

### Disable Strict Mode Temporarily

```sql
-- Check current mode
SELECT @@sql_mode;

-- Temporarily allow implicit conversions
SET SESSION sql_mode = '';
INSERT INTO products (price) VALUES ('abc');  -- inserts 0 with warning
SET SESSION sql_mode = 'STRICT_TRANS_TABLES';
```

## Examples

```
ERROR 1265 (01000): Data truncated for column 'status' at row 1

ERROR 1366 (HY000): Incorrect integer value: 'abc' for column
  'quantity' at row 1

WARNING 1365: Division by 0 for column 'ratio' at row 1
```

## Related Errors

- [MySQL Data Truncated]({{< relref "/tools/mysql/mysql-data-truncated" >}}) -- truncation
- [MySQL Incorrect Datetime]({{< relref "/tools/mysql/mysql-incorrect-datetime" >}}) -- datetime issues
- [MySQL Data Too Long]({{< relref "/tools/mysql/mysql-data-too-long" >}}) -- length issues
