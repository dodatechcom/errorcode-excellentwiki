---
title: "[Solution] SQL Unknown Column Error Fix"
description: "Fix 'Unknown column X in field list' when a SQL query references a column that does not exist."
languages: ["sql"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

This error occurs when a SQL statement references a column that does not exist in the table. The message reads: `Unknown column 'X' in 'field list'`.

## What This Error Means

After parsing, the database validates that all referenced columns exist in the tables being queried. If a column name is misspelled, doesn't exist in the current table context, or is missing from a JOIN, this error fires.

## Common Causes

- Typo in column name (`use_name` instead of `user_name`)
- Column doesn't exist in the table
- Wrong table alias in JOIN references
- Case sensitivity on some databases

## How to Fix

### Fix 1: Verify the column exists

```sql
DESCRIBE users;
-- or
SHOW COLUMNS FROM users;

-- Then use the correct column name
SELECT user_name, email FROM users;
```

### Fix 2: Check for typos

```sql
-- Wrong — column is "created_at", not "createdAt"
SELECT createdAt FROM users;

-- Correct
SELECT created_at FROM users;
```

### Fix 3: Qualify column names in JOINs

```sql
-- Wrong — ambiguous column in JOIN
SELECT id, name FROM users JOIN orders ON users.id = orders.user_id;

-- Correct — qualify column names
SELECT users.id, users.name
FROM users
JOIN orders ON users.id = orders.user_id;

-- Or use table aliases
SELECT u.id, u.name
FROM users u
JOIN orders o ON u.id = o.user_id;
```

## Examples

```sql
SELECT username FROM users;
-- ERROR 1054: Unknown column 'username' in 'field list'
```

## Related Errors

- [Syntax Error](syntax-error.md) — malformed SQL syntax
- [Table Not Found](table-not-found.md) — the table itself does not exist
- [Column not found]({{< relref "/languages/sql/column-not-found" >}})
