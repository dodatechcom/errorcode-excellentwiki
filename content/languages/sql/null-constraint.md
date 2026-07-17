---
title: "[Solution] SQL Column Cannot Be Null Error Fix"
description: "Fix 'Column X cannot be null' when inserting or updating a NOT NULL column with NULL."
languages: ["sql"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# SQL Column Cannot Be Null Error Fix

This error occurs when an INSERT or UPDATE tries to set a NOT NULL column to NULL. The message reads: `Column 'X' cannot be null`.

## Description

NOT NULL constraints require that a column always contains a value. If no value is provided or the source expression evaluates to NULL, the database rejects the operation. This commonly happens with missing data, failed JOINs, or unset application defaults.

## Common Causes

- **No value provided** — INSERT omits the column and there's no DEFAULT.
- **Source column is NULL** — copying from a column that contains NULL.
- **Failed LEFT JOIN** — unmatched rows produce NULL for the right side.
- **Incorrect COALESCE** — fallback value is itself NULL.

## How to Fix

### Fix 1: Provide a default value

```sql
-- Option A: Add a DEFAULT to the column
ALTER TABLE users ALTER COLUMN status SET DEFAULT 'active';

-- Option B: Supply the value in the INSERT
INSERT INTO users (name, status) VALUES ('Alice', 'active');
```

### Fix 2: Use COALESCE to handle NULLs

```sql
-- Replace NULL with a sensible default
INSERT INTO users (name, email)
SELECT name, COALESCE(email, 'unknown@example.com') FROM staging_users;
```

### Fix 3: Filter out NULLs before inserting

```sql
-- Only insert rows where required fields are non-NULL
INSERT INTO users (name, email)
SELECT name, email FROM staging_users
WHERE name IS NOT NULL AND email IS NOT NULL;
```

### Fix 4: Use IFNULL for specific columns

```sql
-- MySQL-specific NULL replacement
INSERT INTO orders (user_id, notes)
SELECT user_id, IFNULL(notes, 'No notes') FROM temp_orders;
```

## Examples

```sql
INSERT INTO users (name) VALUES (NULL);
-- ERROR 1048: Column 'name' cannot be null

UPDATE users SET email = NULL WHERE id = 1;
-- ERROR 1048: Column 'email' cannot be null

INSERT INTO orders (user_id, total)
SELECT u.id, o.total FROM users u LEFT JOIN orders o ON u.id = o.user_id;
-- ERROR 1048: Column 'user_id' cannot be null
-- (if the LEFT JOIN produces NULL for user_id)
```

## Related Errors

- [Duplicate Entry](duplicate-entry.md) — violates a UNIQUE constraint.
- [Foreign Key](foreign-key.md) — violates referential integrity.
- [Data Truncation](data-truncation.md) — value too long for the column.
