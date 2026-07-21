---
title: "SQL Implicit Type Conversion Performance Error"
description: "Fix SQL implicit type conversion errors that cause index bypass and slow query performance on large tables."
languages: ["sql"]
error-types: ["performance-error"]
severities: ["warning"]
weight: 5
---

## Common Causes

- Comparing VARCHAR column with numeric literal
- Comparing DATE column with string literal in wrong format
- Function applied to indexed column in WHERE clause
- JOIN on columns with different data types
- Using != or <> instead of NOT IN for indexed lookups

## How to Fix

```sql
-- WRONG: VARCHAR compared with number forces conversion
SELECT * FROM users WHERE phone = 5551234;
-- phone is VARCHAR, implicit conversion on every row

-- CORRECT: Use matching type
SELECT * FROM users WHERE phone = '5551234';
```

```sql
-- WRONG: Function on indexed column
SELECT * FROM orders WHERE YEAR(order_date) = 2024;
-- Index on order_date is not used

-- CORRECT: Range condition preserves index
SELECT * FROM orders
WHERE order_date >= '2024-01-01' AND order_date < '2025-01-01';
```

## Examples

```sql
-- Example 1: Type mismatch in JOIN
-- orders.customer_id is INT, customers.id is VARCHAR
SELECT * FROM orders o
JOIN customers c ON o.customer_id = c.id;
-- Fix: cast explicitly
SELECT * FROM orders o
JOIN customers c ON o.customer_id = CAST(c.id AS INT);

-- Example 2: Avoid functions on columns
-- BAD
SELECT * FROM employees WHERE UPPER(last_name) = 'SMITH';
-- GOOD
SELECT * FROM employees WHERE last_name = 'SMITH';
-- Or create functional index

-- Example 3: LIKE with leading wildcard
SELECT * FROM products WHERE name LIKE '%widget%';
-- Cannot use index -- consider full-text search
```

## Related Errors

- [Slow query error](slow-query) -- query performance issues
- [Index error](sql-index-error) -- index-related problems
