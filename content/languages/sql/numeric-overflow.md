---
title: "[Solution] Numeric Value Out of Range"
description: "Fix 'Numeric value out of range' when a number exceeds the column's data type limit."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "sql"
tags: ["sql", "data-type, numeric, overflow"]
severity: "error"
---

# Numeric Value Out of Range

## Error Message

```
ERROR 1264: Out of range value for column 'X' at row 1 / Numeric value out of range — The numeric value exceeds the range of the column's data type.
```

## Common Causes

- The value being inserted exceeds the maximum value for the column's numeric data type
- Arithmetic operations produce a result larger than the column can store
- Importing external data with values larger than expected
- Division or multiplication produces more decimal places than the column allows

## Solutions

### Solution 1: Upgrade to a larger numeric data type

Change the column to a data type that can accommodate larger values.

```sql
-- Check current column definition
DESCRIBE users;

-- MySQL: upgrade INT to BIGINT
ALTER TABLE users MODIFY COLUMN balance BIGINT;

-- PostgreSQL: upgrade INTEGER to BIGINT
ALTER TABLE users ALTER COLUMN balance TYPE BIGINT;

-- SQL Server: upgrade to BIGINT or DECIMAL
ALTER TABLE users ALTER COLUMN balance BIGINT;

-- Use DECIMAL for exact precision with large numbers
ALTER TABLE users MODIFY COLUMN balance DECIMAL(20,2);
```

### Solution 2: Validate values before inserting

Check that values are within the allowed range before inserting.

```sql
-- INT range: -2,147,483,648 to 2,147,483,647
-- BIGINT range: -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807

-- Check if value is in range before inserting (MySQL)
SELECT * FROM (SELECT 9999999999999999 AS val) t
WHERE t.val BETWEEN -9223372036854775808 AND 9223372036854775807;

-- PostgreSQL: use range check
INSERT INTO accounts (id, balance)
SELECT id, balance FROM staging_accounts
WHERE balance >= -9223372036854775808 AND balance <= 9223372036854775807;

-- Use TRY_CONVERT to safely test (SQL Server)
SELECT TRY_CONVERT(BIGINT, '9999999999999999');
```

### Solution 3: Use appropriate DECIMAL precision

Define DECIMAL columns with enough precision and scale for your data.

```sql
-- Wrong: DECIMAL(10,2) can only store up to 99999999.99
ALTER TABLE orders MODIFY COLUMN total DECIMAL(10,2);

-- Correct: use larger precision for financial data
ALTER TABLE orders MODIFY COLUMN total DECIMAL(20,4);

-- DECIMAL precision rules: DECIMAL(p,s)
-- p = total number of digits (precision)
-- s = digits after decimal point (scale)
-- DECIMAL(10,2) stores -99999999.99 to 99999999.99
-- DECIMAL(20,4) stores up to 9999999999999999.9999

CREATE TABLE financial_records (
    id INT PRIMARY KEY,
    amount DECIMAL(20,4) NOT NULL,
    rate DECIMAL(10,8)
);
```

## Prevention Tips

- Choose the smallest data type that fits your data range to optimize storage and performance
- Use DECIMAL or NUMERIC for financial calculations where exact precision is required
- Validate numeric ranges in application code and provide clear error messages to users

## Related Errors

- [Integer Overflow]({{< relref "/languages/sql/integer-overflow.md" >}})
- [Decimal Precision]({{< relref "/languages/sql/decimal-precision.md" >}})
- [Data Type Mismatch]({{< relref "/languages/sql/data-type-mismatch.md" >}})
