---
title: "[Solution] SQL Index Build Failed Duplicate Index Error Fix"
description: "Fix 'index build failed' and duplicate index errors in SQL. Create, drop, and manage database indexes without conflicts."
languages: ["sql"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# SQL Index Build Failed Duplicate Index Error Fix

The `index build failed` or `duplicate index` error occurs when creating an index that already exists, conflicts with another index, or fails due to data issues.

## What This Error Means

Indexes speed up queries but consume storage. When you try to create an index that already exists, or the index creation fails due to data corruption, lock conflicts, or insufficient space, the database reports this error.

A typical error:

```
ERROR: relation "idx_users_email" already exists
```

Or:

```
ERROR: could not create unique index "idx_unique_email"
DETAIL: Key (email)=(test@example.com) is duplicated.
```

## Why It Happens

Common causes include:

- **Index already exists** — Trying to create an index that was already created.
- **Duplicate data for unique index** — UNIQUE index found duplicate values.
- **Insufficient disk space** — Not enough space for the index.
- **Lock conflict** — Another session is modifying the table.
- **Index name conflict** — Same name in different schemas.

## How to Fix It

### Fix 1: Check existing indexes

```sql
-- PostgreSQL
SELECT indexname, indexdef 
FROM pg_indexes 
WHERE tablename = 'users';

-- SQL Server
SELECT name, type_desc 
FROM sys.indexes 
WHERE object_id = OBJECT_ID('users');

-- MySQL
SHOW INDEX FROM users;
```

### Fix 2: Create index only if not exists

```sql
-- RIGHT: Conditional creation
CREATE INDEX IF NOT EXISTS idx_users_email 
ON users (email);

-- For unique index
CREATE UNIQUE INDEX IF NOT EXISTS idx_unique_email 
ON users (email);
```

### Fix 3: Drop and recreate

```sql
-- RIGHT: Drop first, then create
DROP INDEX IF EXISTS idx_users_email;
CREATE INDEX idx_users_email ON users (email);
```

### Fix 4: Fix duplicate data before unique index

```sql
-- Find duplicates
SELECT email, COUNT(*) 
FROM users 
GROUP BY email 
HAVING COUNT(*) > 1;

-- Remove duplicates
DELETE FROM users 
WHERE id NOT IN (
    SELECT MIN(id) 
    FROM users 
    GROUP BY email
);

-- Now create unique index
CREATE UNIQUE INDEX idx_unique_email ON users (email);
```

### Fix 5: Use CONCURRENTLY for large tables

```sql
-- RIGHT: Don't lock table during index creation
CREATE INDEX CONCURRENTLY idx_users_name ON users (name);

-- Note: CONCURRENTLY cannot run inside a transaction
```

## Common Mistakes

- **Not checking for existing indexes before CREATE INDEX** — Use `IF NOT EXISTS`.
- **Creating indexes during peak hours** — Use CONCURRENTLY to avoid locks.
- **Over-indexing** — Too many indexes slow down writes.

## Related Pages

- [SQL Constraint Error](sql-constraint-error) — Constraint violations
- [SQL Partition Error](sql-partition-error) — Partition key issues
- [SQL View Error](sql-view-error) — View-related issues
