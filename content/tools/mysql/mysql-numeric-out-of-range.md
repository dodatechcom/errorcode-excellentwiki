---
title: "[Solution] MySQL Numeric Value Out of Range Error"
description: "Fix MySQL numeric value out of range error when inserting or updating values that exceed the column data type bounds"
tools: ["mysql"]
error-types: ["tool-error"]
severities: ["error"]
---

# MySQL Numeric Value Out of Range Error

A numeric value exceeds the storage capacity of the target column type. MySQL rejects the value in strict mode or truncates it with a warning.

## Common Causes

- BIGINT value inserted into INT column (max ~2.1 billion)
- DECIMAL precision exceeds column definition
- Negative value inserted into UNSIGNED column
- Auto-increment counter reaches data type maximum
- Float/DOUBLE precision loss during calculations
- Calculated result exceeds column capacity

## How to Fix

### Check Column Data Type Limits

```sql
-- View column types
DESCRIBE orders;

-- INT: -2147483648 to 2147483647
-- BIGINT: -9223372036854775808 to 9223372036854775807
-- DECIMAL(10,2): -99999999.99 to 99999999.99
```

### Use Appropriate Column Types

```sql
-- If values can exceed INT range, use BIGINT
ALTER TABLE orders MODIFY id BIGINT UNSIGNED AUTO_INCREMENT;

-- For financial values, use DECIMAL not FLOAT
ALTER TABLE orders MODIFY total DECIMAL(12,2);
```

### Validate Before INSERT

```sql
-- Check value fits in column
SET @test_value = 2147483648;
SELECT
  @test_value AS value,
  CASE
    WHEN @test_value > 2147483647 THEN 'EXCEEDS INT MAX'
    ELSE 'OK'
  END AS status;
```

### Use UNSIGNED for Non-Negative Values

```sql
-- If column should never be negative
CREATE TABLE products (
  price DECIMAL(10,2) UNSIGNED,  -- ERROR: UNSIGNED not valid for DECIMAL
  stock INT UNSIGNED
);
```

### Handle Overflow in Calculations

```sql
-- Check for overflow before inserting
SELECT
  quantity * price AS total
FROM order_items
WHERE quantity * price > 99999999.99;  -- DECIMAL(10,2) limit

-- Use CAST to prevent overflow
INSERT INTO orders (total)
VALUES (LEAST(CAST(@calculated AS DECIMAL(10,2)), 99999999.99));
```

## Examples

```
ERROR 1264 (22003): Out of range value for column 'price' at row 1
  -- inserting 999999999.99 into DECIMAL(10,2)

ERROR 1690 (22003): BIGINT UNSIGNED value is out of range
  -- subtraction result would be negative in UNSIGNED column
```

## Related Errors

- [MySQL Data Too Long]({{< relref "/tools/mysql/mysql-data-too-long" >}}) -- length overflow
- [MySQL Data Truncated]({{< relref "/tools/mysql/mysql-data-truncated" >}}) -- truncation
- [MySQL Incorrect Value]({{< relref "/tools/mysql/mysql-truncated-incorrect-value" >}}) -- value errors
