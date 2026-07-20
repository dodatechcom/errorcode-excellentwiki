---
title: "[Solution] Integer Overflow Error"
description: "Fix 'Integer overflow error' when a numeric value exceeds the integer type's range."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "sql"
tags: ["sql", "data-type, integer, overflow"]
severity: "error"
---

# Integer Overflow Error

## Error Message

```
ERROR 1690: BIGINT value is out of range / Arithmetic overflow error converting expression to data type int — The value exceeds the maximum (or minimum) value of the integer data type.
```

## Common Causes

- Arithmetic operation produces a result larger than the column's integer type can store
- Summing many large values causes the total to exceed INT range (2,147,483,647)
- Importing data with values larger than the column type's maximum
- Auto-increment counter approaches the INT maximum value

## Solutions

### Solution 1: Upgrade the column to a larger integer type

Change from INT to BIGINT to support larger values.

```sql
-- MySQL: upgrade INT to BIGINT UNSIGNED
ALTER TABLE counters MODIFY COLUMN value BIGINT UNSIGNED;

-- PostgreSQL: upgrade INTEGER to BIGINT
ALTER TABLE counters ALTER COLUMN value TYPE BIGINT;

-- SQL Server: upgrade INT to BIGINT
ALTER TABLE counters ALTER COLUMN value BIGINT;

-- Check current column type
DESCRIBE counters; -- MySQL
SELECT column_name, data_type FROM information_schema.columns
WHERE table_name = 'counters'; -- PostgreSQL/SQL Server
```

### Solution 2: Use appropriate data types from the start

Choose data types that can accommodate expected value ranges.

```sql
-- INT: -2,147,483,648 to 2,147,483,647
-- INT UNSIGNED: 0 to 4,294,967,295
-- BIGINT: -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
-- BIGINT UNSIGNED: 0 to 18,446,744,073,709,551,615

-- Correct: use BIGINT for counters that may grow large
CREATE TABLE page_views (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    page_url VARCHAR(500) NOT NULL,
    view_count BIGINT UNSIGNED DEFAULT 0
);

-- Use BIGINT for IDs in high-volume tables
CREATE TABLE events (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    event_type VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Solution 3: Split large aggregations to avoid overflow

Break down calculations to prevent intermediate values from overflowing.

```sql
-- Wrong: SUM may overflow INT
SELECT SUM(large_value) FROM transactions;
-- If total exceeds 2,147,483,647, overflow occurs

-- Correct: cast to BIGINT before summing
SELECT SUM(CAST(large_value AS BIGINT)) FROM transactions;

-- PostgreSQL: use BIGINT in aggregation
SELECT SUM(large_value::BIGINT) FROM transactions;

-- SQL Server: convert before aggregation
SELECT SUM(CONVERT(BIGINT, large_value)) FROM transactions;

-- MySQL: use BIGINT for intermediate results
SELECT SUM(CAST(large_value AS UNSIGNED)) FROM transactions;
```

## Prevention Tips

- Use BIGINT for primary keys in tables expected to grow beyond 2 billion rows
- Monitor auto-increment counters to ensure they do not approach the integer type's maximum value
- Cast to BIGINT before performing aggregations on large numeric values to prevent overflow

## Related Errors

- [Numeric Overflow]({{< relref "/languages/sql/numeric-overflow.md" >}})
- [Auto Increment Error]({{< relref "/languages/sql/auto-increment-error.md" >}})
- [Decimal Precision]({{< relref "/languages/sql/decimal-precision.md" >}})
