---
title: "[Solution] SQL Duplicate Entry for PRIMARY KEY Error Fix"
description: "Fix SQL duplicate entry errors when inserting a row with a PRIMARY KEY that already exists."
languages: ["sql"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# SQL Duplicate Entry for PRIMARY KEY Error Fix

A SQL duplicate entry error occurs when you try to insert or update a row with a PRIMARY KEY or UNIQUE constraint value that already exists.

## What This Error Means

The database enforces uniqueness constraints. When an INSERT or UPDATE produces a duplicate value for a PRIMARY KEY or UNIQUE column, the operation is rejected with a duplicate entry error.

## Common Causes

- Inserting a record with an ID that already exists
- Race condition between check and insert
- Uploading/importing duplicate data
- Not using auto-increment properly

## How to Fix

### 1. Use INSERT IGNORE or ON DUPLICATE KEY

```sql
-- CORRECT: Handle duplicates gracefully
INSERT IGNORE INTO users (id, name, email)
VALUES (1, 'Alice', 'alice@example.com');

-- Or use ON DUPLICATE KEY UPDATE
INSERT INTO users (id, name, email)
VALUES (1, 'Alice', 'alice@example.com')
ON DUPLICATE KEY UPDATE name = VALUES(name);
```

### 2. Check before inserting

```sql
-- CORRECT: Verify existence first
SELECT COUNT(*) FROM users WHERE id = 1;
-- If 0, insert; otherwise update
```

### 3. Use REPLACE (MySQL)

```sql
-- CORRECT: Replace existing record
REPLACE INTO users (id, name, email)
VALUES (1, 'Alice Updated', 'alice@example.com');
```

### 4. Use UPSERT pattern

```sql
-- CORRECT: PostgreSQL upsert
INSERT INTO users (id, name, email)
VALUES (1, 'Alice', 'alice@example.com')
ON CONFLICT (id)
DO UPDATE SET name = EXCLUDED.name, email = EXCLUDED.email;
```

## Related Errors

- [SQL Foreign Key](sql-foreign-key-v2) — constraint violations
- [SQL Data Truncated](sql-data-truncated-v2) — data type issues
- [SQL Duplicate Entry]({{< relref "/languages/sql/duplicate-entry" >}}) — alternative reference
