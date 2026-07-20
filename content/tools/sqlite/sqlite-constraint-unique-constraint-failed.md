---
title: "[Solution] SQLite UNIQUE constraint failed"
description: "A UNIQUE constraint was violated by an INSERT or UPDATE that would create a duplicate value."
tools: ["sqlite"]
error-types: ["constraint-error"]
severities: ["error"]
---


# [Solution] SQLite UNIQUE constraint failed

SQLite raises a **UNIQUE constraint failed** error when a unique constraint was violated by an insert or update that would create a duplicate value. This is one of the most common classes of errors encountered in SQLite databases.

## Common Causes

- Inserting a row with a duplicate value in a UNIQUE column.
- Using INSERT OR REPLACE when the replacement also conflicts.
- Concurrent connections inserting the same key without serialization.

## How to Fix

### Use INSERT OR IGNORE to skip conflicting rows

```sql
INSERT OR IGNORE INTO users (id, email) VALUES (1, 'a@b.com');
```

### Use UPSERT to update on conflict

```sql
INSERT INTO users (id, email) VALUES (1, 'a@b.com')
ON CONFLICT(email) DO UPDATE SET email = excluded.email;
```

### Check for existing rows before inserting

```sql
SELECT COUNT(*) FROM users WHERE email = 'a@b.com';
```

## Examples

```sql
INSERT INTO users (id, email) VALUES (1, 'a@b.com');
INSERT INTO users (id, email) VALUES (2, 'a@b.com');
-- Error: UNIQUE constraint failed: users.email
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
