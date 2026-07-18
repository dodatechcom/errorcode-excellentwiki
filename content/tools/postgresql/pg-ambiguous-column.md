---
title: "[Solution] PostgreSQL Column Reference is Ambiguous Error — How to Fix"
description: "Fix PostgreSQL ambiguous column references by qualifying column names with table aliases, resolving JOIN conflicts, and clarifying SELECT lists"
tools: ["postgresql"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# PostgreSQL Column Reference is Ambiguous Error

This error means a column name in the query exists in two or more joined tables, and PostgreSQL cannot determine which table you are referring to. You must qualify the column with the table name or alias.

## Why It Happens

- A JOIN query references a column that exists in both tables without a table qualifier
- A subquery inherits column names that conflict with the outer query
- A USING clause references a column that appears elsewhere in the SELECT list
- Multiple tables in a FROM clause share common column names (like `id` or `created_at`)
- A NATURAL JOIN picks up shared columns automatically, creating ambiguity

## Common Error Messages

```
ERROR: column reference "id" is ambiguous
LINE 1: SELECT id, name FROM orders JOIN customers ON ...
```

```
ERROR: column reference "name" is ambiguous
DETAIL: It could refer to either table1.name or table2.name.
```

```
ERROR: column "created_at" is ambiguous
HINT: Use a fully qualified name or an alias.
```

## How to Fix It

### 1. Qualify Columns with Table Aliases

```sql
-- Wrong: id is in both tables
SELECT id, name, total
FROM orders o
JOIN customers c ON o.customer_id = c.id;

-- Right: use table aliases
SELECT o.id, c.name, o.total
FROM orders o
JOIN customers c ON o.customer_id = c.id;
```

### 2. Use Aliases in Complex Queries

```sql
SELECT
    o.id AS order_id,
    c.name AS customer_name,
    p.name AS product_name,
    oi.quantity
FROM orders o
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id
JOIN customers c ON o.customer_id = c.id
WHERE o.created_at > '2025-01-01';
```

### 3. Fix in GROUP BY and ORDER BY

```sql
-- Wrong
SELECT customer_id, COUNT(*)
FROM orders
GROUP BY customer_id
ORDER BY created_at;

-- Right: qualify the ORDER BY column
SELECT o.customer_id, COUNT(*)
FROM orders o
GROUP BY o.customer_id
ORDER BY MAX(o.created_at);
```

### 4. Fix in Subqueries

```sql
-- Wrong: ambiguous in subquery
SELECT id, name
FROM customers
WHERE id IN (
    SELECT customer_id FROM orders WHERE id > 100
);

-- Right: qualify in the subquery
SELECT c.id, c.name
FROM customers c
WHERE c.id IN (
    SELECT o.customer_id FROM orders o WHERE o.id > 100
);
```

### 5. Avoid NATURAL JOIN in Production

```sql
-- Dangerous: NATURAL JOIN automatically matches all columns with the same name
SELECT * FROM orders NATURAL JOIN customers;

-- Safe: explicit JOIN with ON clause
SELECT o.*, c.name
FROM orders o
JOIN customers c ON o.customer_id = c.id;
```

## Common Scenarios

- **SELECT ***: Using `SELECT *` in a JOIN returns all columns from both tables, and `ORDER BY id` becomes ambiguous. Always qualify columns in queries with JOINs.
- **ORM-generated queries**: Some ORMs generate ambiguous SQL when multiple models share column names. Check the generated SQL and add explicit qualifiers.
- **View definition**: A view joins two tables but does not qualify columns. Rewrite the view with explicit table aliases.

## Prevent It

- Always use table aliases (at least one letter) in any query with JOINs
- Avoid `SELECT *` in production queries — specify each column with its table alias
- Use `NATURAL JOIN` only in ad-hoc exploration queries, never in application code

## Related Pages

- [PostgreSQL Duplicate Table](/tools/postgresql/pg-duplicate-table)
- [PostgreSQL Syntax Error](/tools/postgresql/pg-syntax-error)
- [MySQL Unknown Column](/tools/mysql/mysql-unknown-column)
