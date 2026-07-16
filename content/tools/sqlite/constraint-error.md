---
title: "[Solution] SQLite UNIQUE Constraint Failed"
description: "Fix SQLite UNIQUE constraint failed errors. Resolve duplicate value insertion issues."
tools: ["sqlite"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["sqlite", "unique", "constraint", "duplicate", "insert"]
weight: 5
---

# SQLite UNIQUE Constraint Failed

A UNIQUE constraint failure occurs when an INSERT or UPDATE attempts to add a value that already exists in a column with a UNIQUE constraint or PRIMARY KEY.

## Common Causes

- Attempting to insert a duplicate primary key value
- A column with a UNIQUE constraint already contains the value
- Race condition in concurrent inserts without proper locking
- The application logic does not check for existing records

## How to Fix

### Use INSERT OR REPLACE

```sql
INSERT OR REPLACE INTO users (id, name, email)
VALUES (1, 'Alice', 'alice@example.com');
```

### Use INSERT OR IGNORE to Skip Duplicates

```sql
INSERT OR IGNORE INTO users (id, name, email)
VALUES (1, 'Alice', 'alice@example.com');
```

### Use UPSERT (INSERT ON CONFLICT)

```sql
INSERT INTO users (id, name, email)
VALUES (1, 'Alice', 'alice@example.com')
ON CONFLICT(id) DO UPDATE SET
    name = excluded.name,
    email = excluded.email;
```

### Check Existing Values Before Insert

```sql
-- Check if the value already exists
SELECT COUNT(*) FROM users WHERE id = 1;
-- If count > 0, use UPDATE instead of INSERT
```

### Add Auto-Increment for Primary Keys

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE
);
```

## Examples

```sql
-- Duplicate primary key
INSERT INTO users (id, name) VALUES (1, 'Alice');
INSERT INTO users (id, name) VALUES (1, 'Bob');
-- Error: UNIQUE constraint failed: users.id

-- Duplicate unique email
INSERT INTO users (id, name, email) VALUES (2, 'Bob', 'alice@example.com');
-- Error: UNIQUE constraint failed: users.email
```

## Related Errors

- [Constraint Error]({{< relref "/tools/sqlite/constraint-error" >}}) — other constraint violations
- [Database Locked]({{< relref "/tools/sqlite/database-locked" >}}) — write lock contention
