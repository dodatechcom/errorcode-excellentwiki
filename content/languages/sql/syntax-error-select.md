---
title: "[Solution] SQL Syntax Error Near SELECT"
description: "Fix 'SQL syntax error near SELECT' when the SELECT statement is malformed."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "sql"
tags: ["sql", "syntax"]
severity: "error"
---

# SQL Syntax Error Near SELECT

## Error Message

```
You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'SELECT ...'
```

## Common Causes

- SELECT clause contains invalid columns or expressions that the parser cannot interpret
- Aggregate functions used in the WHERE clause instead of the HAVING clause
- Missing FROM clause when columns reference a table
- Invalid use of wildcards or column aliases without the AS keyword in contexts that require it

## Solutions

### Solution 1: Fix the SELECT column list syntax

Ensure every column in the SELECT list is valid and properly separated by commas. Remove trailing commas and verify all column names exist.

```sql
-- Wrong: trailing comma after last column
SELECT name, age, FROM users;

-- Correct
SELECT name, age FROM users;

-- Wrong: using aggregate in WHERE instead of HAVING
SELECT department, COUNT(*) FROM employees
WHERE COUNT(*) > 5 GROUP BY department;

-- Correct: filter aggregates in HAVING
SELECT department, COUNT(*) FROM employees
GROUP BY department HAVING COUNT(*) > 5;
```

### Solution 2: Verify column aliases and expressions

Use the AS keyword for aliases and ensure expressions are valid SQL.

```sql
-- Wrong: invalid alias syntax
SELECT name AS, age FROM users;

-- Correct
SELECT name AS user_name, age FROM users;

-- Wrong: string concatenation without proper function
SELECT first_name + last_name FROM employees;

-- Correct (MySQL)
SELECT CONCAT(first_name, ' ', last_name) FROM employees;

-- Correct (PostgreSQL)
SELECT first_name || ' ' || last_name FROM employees;
```

### Solution 3: Use proper subquery syntax in SELECT

Scalar subqueries in the SELECT list must return exactly one column and one row.

```sql
-- Wrong: subquery returns multiple columns
SELECT name, (SELECT id, email FROM users u WHERE u.id = e.user_id) FROM employees e;

-- Correct: scalar subquery
SELECT name, (SELECT email FROM users u WHERE u.id = e.user_id) FROM employees e;

-- Correct: use a JOIN instead
SELECT e.name, u.email FROM employees e
LEFT JOIN users u ON u.id = e.user_id;
```

## Prevention Tips

- Always check that all column names in the SELECT list exist in the referenced tables
- Use your database's EXPLAIN or DESCRIBE command to validate query structure before running complex queries
- Enable strict SQL mode in MySQL to catch syntax issues early during development

## Related Errors

- [Syntax Error Where]({{< relref "/languages/sql/syntax-error-where.md" >}})
- [Syntax Error Join]({{< relref "/languages/sql/syntax-error-join.md" >}})
- [Syntax Error Group By]({{< relref "/languages/sql/syntax-error-group-by.md" >}})
