---
title: "[Solution] SQL Duplicate Key Name Error Fix"
description: "Fix 'Duplicate key name' when creating an index that already exists."
languages: ["sql"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["index-error", "duplicate-key-name", "create-index", "index-exists"]
weight: 5
---

# SQL Duplicate Key Name Error Fix

This error occurs when trying to create an index with a name that already exists on the table. The message reads: `Duplicate key name 'X'`.

## Description

Each index on a table must have a unique name within that table. If you try to create an index with a name that's already in use — whether it's a user-defined index or an auto-generated one — the database rejects the operation.

## Common Causes

- **Index already exists** — re-running a migration that creates the same index.
- **Name collision with auto-generated index** — MySQL auto-names PRIMARY, UNIQUE, and INDEX constraints.
- **Duplicate migration scripts** — running the same migration twice.
- **Manual naming conflict** — choosing a name that matches an existing index.

## How to Fix

### Fix 1: Drop the index first, then recreate

```sql
-- Check existing indexes
SHOW INDEX FROM users;

-- Drop the old index
DROP INDEX idx_email ON users;

-- Create the new index
CREATE INDEX idx_email ON users(email);
```

### Fix 2: Use IF NOT EXISTS (MySQL 8.0.29+)

```sql
-- Only creates if it doesn't already exist
CREATE INDEX IF NOT EXISTS idx_email ON users(email);
```

### Fix 3: Use ALTER TABLE with conditional check

```sql
-- Check if index exists before creating
-- (MySQL doesn't support IF EXISTS for CREATE INDEX directly)
-- Run this as a procedure or check manually:

SELECT COUNT(*)
FROM information_schema.statistics
WHERE table_schema = DATABASE()
  AND table_name = 'users'
  AND index_name = 'idx_email';

-- If 0, create it
CREATE INDEX idx_email ON users(email);
```

### Fix 4: Name indexes consistently with a convention

```sql
-- Use a naming convention to avoid conflicts
-- Format: idx_tablename_columnname
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_created_at ON users(created_at);
CREATE INDEX idx_orders_user_id ON orders(user_id);
```

## Examples

```sql
CREATE INDEX idx_email ON users(email);
-- First run: OK

CREATE INDEX idx_email ON users(email);
-- ERROR 1061: Duplicate key name 'idx_email'

-- If the index was auto-created by a UNIQUE constraint:
ALTER TABLE users ADD UNIQUE INDEX idx_email (email);
-- Later:
CREATE INDEX idx_email ON users(email);
-- ERROR 1061: Duplicate key name 'idx_email'
```

## Related Errors

- [Duplicate Entry](duplicate-entry.md) — duplicate value in a UNIQUE column.
- [Lock Timeout](lock-timeout.md) — waiting for locks during index creation.
- [Syntax Error](syntax-error.md) — malformed CREATE INDEX statement.
