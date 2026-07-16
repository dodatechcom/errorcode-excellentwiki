---
title: "[Solution] SQL Duplicate Entry Error Fix"
description: "Fix 'Duplicate entry for key' when inserting a value that violates a UNIQUE constraint."
languages: ["sql"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["duplicate-entry", "unique-constraint", "primary-key"]
weight: 5
---

# SQL Duplicate Entry Error Fix

This error occurs when an INSERT or UPDATE tries to store a duplicate value in a column with a UNIQUE or PRIMARY KEY constraint. The message reads: `Duplicate entry 'X' for key 'Y'`.

## Description

UNIQUE constraints enforce that every value in a column (or combination of columns) is distinct. Attempting to insert or update a row with a value that already exists violates this rule and raises an error.

## Common Causes

- **Inserting a row with an existing primary key** — the ID is already taken.
- **Violating a UNIQUE index** — e.g., duplicate email in a users table.
- **Bulk insert with duplicates** — importing data that contains repeated rows.
- **Race condition** — two concurrent inserts try to create the same record.

## How to Fix

### Fix 1: Use INSERT ... ON DUPLICATE KEY UPDATE

```sql
-- Instead of failing, update the existing row
INSERT INTO users (email, name) VALUES ('alice@example.com', 'Alice')
ON DUPLICATE KEY UPDATE name = VALUES(name);
```

### Fix 2: Use INSERT IGNORE to skip duplicates

```sql
-- Silently skip rows that violate the unique constraint
INSERT IGNORE INTO users (email, name) VALUES ('alice@example.com', 'Alice');
```

### Fix 3: Use REPLACE INTO to overwrite

```sql
-- Delete the existing row and insert the new one
REPLACE INTO users (email, name) VALUES ('alice@example.com', 'Alice');
```

### Fix 4: Check for duplicates before inserting

```sql
-- Verify if the value already exists
SELECT COUNT(*) FROM users WHERE email = 'alice@example.com';

-- Only insert if it doesn't exist
INSERT INTO users (email, name)
SELECT 'alice@example.com', 'Alice'
WHERE NOT EXISTS (SELECT 1 FROM users WHERE email = 'alice@example.com');
```

## Examples

```sql
INSERT INTO users (id, email) VALUES (1, 'bob@example.com');
-- ERROR 1062: Duplicate entry '1' for key 'PRIMARY'

INSERT INTO users (email) VALUES ('alice@example.com');
-- ERROR 1062: Duplicate entry 'alice@example.com' for key 'email'
-- (if email has a UNIQUE constraint and alice@example.com already exists)
```

## Related Errors

- [Null Constraint](null-constraint.md) — violates a NOT NULL constraint instead.
- [Foreign Key](foreign-key.md) — violates a referential integrity constraint.
- [Data Truncation](data-truncation.md) — value too long for the column.
