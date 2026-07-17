---
title: "[Solution] SQL Duplicate Entry Error Fix"
description: "Fix 'Duplicate entry X for key Y' when an INSERT or UPDATE violates a unique constraint."
languages: ["sql"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["duplicate-entry", "unique-constraint", "primary-key", "index"]
weight: 5
---

This error occurs when an INSERT or UPDATE statement tries to insert a value that already exists in a column with a UNIQUE or PRIMARY KEY constraint. The message reads: `Duplicate entry 'X' for key 'Y'`.

## What This Error Means

The database enforces uniqueness on certain columns. When you try to insert or update a row with a value that duplicates an existing one in a unique column, the operation is rejected.

## Common Causes

- Inserting a row with a duplicate primary key
- Unique index violation on email, username, or slug columns
- Bulk insert contains duplicate rows
- Race condition in concurrent inserts

## How to Fix

### Fix 1: Use INSERT IGNORE or ON DUPLICATE KEY UPDATE

```sql
-- Ignore duplicates silently
INSERT IGNORE INTO users (email, name)
VALUES ('alice@example.com', 'Alice');

-- Update on duplicate
INSERT INTO users (email, name, login_count)
VALUES ('alice@example.com', 'Alice', 1)
ON DUPLICATE KEY UPDATE login_count = login_count + 1;
```

### Fix 2: Use REPLACE (deletes and re-inserts)

```sql
REPLACE INTO users (id, email, name)
VALUES (1, 'alice@example.com', 'Alice Updated');
```

### Fix 3: Check existing data before inserting

```sql
-- Check if the value already exists
SELECT COUNT(*) FROM users WHERE email = 'alice@example.com';

-- Only insert if not found
INSERT INTO users (email, name)
SELECT 'alice@example.com', 'Alice'
FROM DUAL
WHERE NOT EXISTS (
    SELECT 1 FROM users WHERE email = 'alice@example.com'
);
```

## Examples

```sql
INSERT INTO users (id, email) VALUES (1, 'bob@example.com');
-- ERROR 1062: Duplicate entry '1' for key 'PRIMARY'
```

## Related Errors

- [Foreign Key](foreign-key.md) — constraint violation on related table
- [Deadlock](deadlock.md) — concurrent access conflict
