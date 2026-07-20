---
title: "[Solution] SQL Syntax Error Near DELETE"
description: "Fix 'SQL syntax error near DELETE' when a DELETE statement is malformed."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "sql"
tags: ["sql", "syntax"]
severity: "error"
---

# SQL Syntax Error Near DELETE

## Error Message

```
You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'DELETE ...'
```

## Common Causes

- DELETE statement missing the FROM keyword
- Using JOIN in DELETE without the correct database-specific syntax
- Attempting to DELETE from a table that is referenced by a foreign key without CASCADE
- Subquery in WHERE clause returns multiple rows instead of a single value

## Solutions

### Solution 1: Include the FROM keyword

DELETE statements require FROM before the table name in all SQL dialects.

```sql
-- Wrong: missing FROM keyword
DELETE users WHERE id = 1;

-- Correct
DELETE FROM users WHERE id = 1;

-- Wrong: deleting without a WHERE clause (dangerous)
DELETE FROM users;

-- Always verify with a SELECT first
SELECT * FROM users WHERE id = 1;
DELETE FROM users WHERE id = 1;
```

### Solution 2: Use proper multi-table DELETE syntax

Different databases support different syntax for deleting from multiple tables.

```sql
-- MySQL: DELETE with JOIN
DELETE o
FROM orders o
JOIN users u ON o.user_id = u.id
WHERE u.active = 0;

-- SQL Server: DELETE with FROM
DELETE o
FROM orders o
INNER JOIN users u ON o.user_id = u.id
WHERE u.active = 0;

-- PostgreSQL: DELETE with USING
DELETE FROM orders
USING users
WHERE orders.user_id = users.id AND users.active = 0;
```

### Solution 3: Handle foreign key constraints before deleting

If a row is referenced by foreign keys, either delete the referencing rows first or use CASCADE.

```sql
-- Option 1: Delete child rows first
DELETE FROM order_items WHERE order_id = 10;
DELETE FROM orders WHERE id = 10;

-- Option 2: Use ON DELETE CASCADE (requires altering the table)
ALTER TABLE order_items
ADD CONSTRAINT fk_order
FOREIGN KEY (order_id) REFERENCES orders(id)
ON DELETE CASCADE;

-- Option 3: Use a subquery
DELETE FROM users WHERE id IN (
    SELECT user_id FROM orders WHERE total > 1000
);
```

## Prevention Tips

- Always use a WHERE clause with DELETE unless you intend to remove all rows
- Run a SELECT with the same WHERE clause first to preview which rows will be deleted
- Consider using soft deletes (setting a deleted_at timestamp) instead of physically removing rows

## Related Errors

- [Foreign Key Violation]({{< relref "/languages/sql/foreign-key-violation.md" >}})
- [Syntax Error Where]({{< relref "/languages/sql/syntax-error-where.md" >}})
- [Lock Timeout]({{< relref "/languages/sql/lock-timeout.md" >}})
