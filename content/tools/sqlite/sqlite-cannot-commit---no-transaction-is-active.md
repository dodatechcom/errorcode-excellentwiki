---
title: "[Solution] SQLite cannot commit - no transaction is active"
description: "A COMMIT statement was issued but no transaction is currently active."
tools: ["sqlite"]
error-types: ["locking-error"]
severities: ["error"]
---


# [Solution] SQLite cannot commit - no transaction is active

SQLite reports **cannot commit - no transaction is active** when a commit statement was issued but no transaction is currently active. Proper transaction management is essential for data integrity.

## Common Causes

- The transaction was already committed or rolled back.
- Autocommit is on and statements execute immediately.
- A prior error caused an implicit rollback.

## How to Fix

### Start a transaction before committing

```sql
BEGIN;
-- perform operations
COMMIT;
```

### Check autocommit mode

```python
# In Python sqlite3, autocommit is on by default
conn.execute('BEGIN')
# ... do work ...
conn.commit()
```

### Use savepoints instead of full transactions for nested work

```sql
BEGIN;
SAVEPOINT sp1;
RELEASE sp1;
COMMIT;
```

## Examples

```sql
COMMIT;
-- Error: cannot commit - no transaction is active
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
