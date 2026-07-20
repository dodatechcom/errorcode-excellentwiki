---
title: "[Solution] SQL Syntax Error Near UPDATE"
description: "Fix 'SQL syntax error near UPDATE' when an UPDATE statement is malformed."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "sql"
tags: ["sql", "syntax"]
severity: "error"
---

# SQL Syntax Error Near UPDATE

## Error Message

```
You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'UPDATE ...'
```

## Common Causes

- Missing WHERE clause causes syntax issues in some contexts or updates all rows unintentionally
- Incorrect SET assignment syntax such as using = instead of := in MySQL for user variables
- Attempting to UPDATE a column that does not exist in the table
- Using JOIN syntax incorrectly in UPDATE statements across different database systems

## Solutions

### Solution 1: Use correct SET clause syntax

Each column assignment in the SET clause must use the format column = value, separated by commas.

```sql
-- Wrong: using semicolon inside SET clause
UPDATE users SET name = 'Alice'; SET email = 'a@ex.com' WHERE id = 1;

-- Correct
UPDATE users
SET name = 'Alice', email = 'alice@example.com'
WHERE id = 1;

-- Wrong: missing WHERE on a conditional update
UPDATE products SET price = price * 1.1;

-- Correct with WHERE clause
UPDATE products SET price = price * 1.1 WHERE category = 'electronics';
```

### Solution 2: Use proper JOIN syntax for multi-table UPDATE

Different databases require different syntax for updating rows based on joins.

```sql
-- MySQL: UPDATE with JOIN
UPDATE orders o
JOIN users u ON o.user_id = u.id
SET o.status = 'archived'
WHERE u.active = 0;

-- SQL Server: UPDATE with FROM
UPDATE o
SET o.status = 'archived'
FROM orders o
INNER JOIN users u ON o.user_id = u.id
WHERE u.active = 0;

-- PostgreSQL: UPDATE with FROM
UPDATE orders
SET status = 'archived'
FROM users
WHERE orders.user_id = users.id AND users.active = 0;
```

### Solution 3: Use CASE for conditional updates

When updating different rows with different values, use a CASE expression.

```sql
-- Update different values based on conditions
UPDATE employees
SET salary = CASE
    WHEN department = 'engineering' THEN salary * 1.10
    WHEN department = 'marketing'  THEN salary * 1.05
    ELSE salary * 1.02
END
WHERE active = 1;

-- PostgreSQL: UPDATE with RETURNING
UPDATE products
SET price = price * 1.10
WHERE category = 'electronics'
RETURNING id, name, price;
```

## Prevention Tips

- Always include a WHERE clause unless you intentionally want to update every row
- Run a SELECT with the same WHERE clause first to verify which rows will be affected
- Use transactions so you can roll back if the UPDATE affects more rows than expected

## Related Errors

- [Syntax Error Where]({{< relref "/languages/sql/syntax-error-where.md" >}})
- [Syntax Error Select]({{< relref "/languages/sql/syntax-error-select.md" >}})
- [Foreign Key Violation]({{< relref "/languages/sql/foreign-key-violation.md" >}})
