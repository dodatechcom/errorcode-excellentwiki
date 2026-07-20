---
title: "[Solution] SQL Syntax Error Near ORDER BY"
description: "Fix 'SQL syntax error near ORDER BY' when an ORDER BY clause is malformed."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "sql"
tags: ["sql", "syntax"]
severity: "error"
---

# SQL Syntax Error Near ORDER BY

## Error Message

```
You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'ORDER BY ...'
```

## Common Causes

- Using column aliases that are not recognized in ORDER BY depending on the SQL mode
- ORDER BY with an expression that contains unsupported syntax for the database
- Positional ordering using column numbers that exceed the SELECT column count
- Using ORDER BY in subqueries or views without a LIMIT (in MySQL this causes optimization issues)

## Solutions

### Solution 1: Use valid ORDER BY expressions

ORDER BY can reference column names, ordinal positions, or expressions, but the syntax must be correct.

```sql
-- Wrong: column alias in ORDER BY with strict SQL mode
SELECT name AS user_name FROM users ORDER BY user_name;

-- Correct: use the full expression
SELECT name AS user_name FROM users ORDER BY name;

-- Correct: use column ordinal position
SELECT name, age FROM users ORDER BY 2;

-- Correct: use the alias (works in most databases)
SELECT name AS user_name FROM users ORDER BY user_name;
```

### Solution 2: Order by multiple columns

Specify the sort direction (ASC or DESC) for each column in the ORDER BY clause.

```sql
-- Correct: multi-column sort
SELECT name, department, salary
FROM employees
ORDER BY department ASC, salary DESC;

-- Correct: order by expression
SELECT name, salary
FROM employees
ORDER BY salary - bonus DESC;

-- Correct: order by CASE for custom sorting
SELECT name, status FROM users
ORDER BY CASE status
    WHEN 'admin' THEN 1
    WHEN 'moderator' THEN 2
    ELSE 3
END;
```

### Solution 3: Avoid ORDER BY in subqueries

Some databases ignore ORDER BY in subqueries unless combined with LIMIT or TOP.

```sql
-- MySQL: ORDER BY in subquery is ignored without LIMIT
SELECT * FROM (
    SELECT name, age FROM users ORDER BY age
) AS sub;

-- Correct: use LIMIT with ORDER BY in subquery
SELECT * FROM (
    SELECT name, age FROM users ORDER BY age LIMIT 10
) AS sub;

-- SQL Server: use TOP instead
SELECT * FROM (
    SELECT TOP 10 name, age FROM users ORDER BY age
) AS sub;
```

## Prevention Tips

- Use column aliases in ORDER BY only when your database SQL mode permits it
- Remember that ORDER BY with expressions or functions may prevent index usage and slow down queries
- Use NULLS FIRST or NULLS LAST to control where NULL values appear in sorted results (PostgreSQL supports this natively)

## Related Errors

- [Syntax Error Select]({{< relref "/languages/sql/syntax-error-select.md" >}})
- [Syntax Error Group By]({{< relref "/languages/sql/syntax-error-group-by.md" >}})
- [Sql Order By Error]({{< relref "/languages/sql/sql-order-by-error.md" >}})
