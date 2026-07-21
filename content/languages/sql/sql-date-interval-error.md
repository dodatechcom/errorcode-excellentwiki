---
title: "SQL Date Arithmetic Interval Error"
description: "Fix SQL date arithmetic errors when using incorrect interval syntax or incompatible date functions across databases."
languages: ["sql"]
error-types: ["syntax-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- Using MySQL DATE_ADD syntax in PostgreSQL (uses INTERVAL)
- INTERVAL unit typo or unsupported unit name
- Adding interval to non-date column type
- Date format string mismatch between databases
- Using DATEADD with wrong parameter order

## How to Fix

```sql
-- WRONG: MySQL syntax in PostgreSQL
SELECT DATE_ADD(NOW(), INTERVAL 30 DAY);
-- PostgreSQL ERROR

-- CORRECT: PostgreSQL syntax
SELECT NOW() + INTERVAL '30 days';
```

```sql
-- WRONG: SQL Server DATEADD wrong order
SELECT DATEADD(DAY, 30, GETDATE());  -- this is correct for SQL Server
-- But trying DATEADD(GETDATE(), 30, DAY) is wrong

-- CORRECT: Always parameter order for SQL Server
SELECT DATEADD(DAY, 30, GETDATE());
```

## Examples

```sql
-- Example 1: MySQL date arithmetic
SELECT DATE_ADD(order_date, INTERVAL 7 DAY) AS due_date FROM orders;
SELECT DATE_SUB(NOW(), INTERVAL 1 YEAR) AS last_year;

-- Example 2: PostgreSQL date arithmetic
SELECT NOW() + INTERVAL '1 month' AS next_month;
SELECT CURRENT_DATE - INTERVAL '7 days' AS last_week;

-- Example 3: SQL Server DATEADD
SELECT DATEADD(MONTH, -3, GETDATE()) AS three_months_ago;
SELECT DATEADD(HOUR, 2, created_at) AS expires_at FROM sessions;
```

## Related Errors

- [Date format error](date-format-error) -- date parsing issues
- [Syntax error](syntax-error) -- general syntax problems
