---
title: "[Solution] SQLite exclusive access required"
description: "An operation requires exclusive access to the database but another connection holds a lock."
tools: ["sqlite"]
error-types: ["locking-error"]
severities: ["error"]
---


# [Solution] SQLite exclusive access required

SQLite reports **exclusive access required** when an operation requires exclusive access to the database but another connection holds a lock. Proper transaction management is essential for data integrity.

## Common Causes

- VACUUM requires exclusive access.
- ALTER TABLE on some operations needs exclusive lock.
- Another connection holds a shared or reserved lock.

## How to Fix

### Close all other connections before running exclusive operations

```sql
-- Ensure no other connections are active
VACUUM;
```

### Use BEGIN EXCLUSIVE for operations requiring full access

```sql
BEGIN EXCLUSIVE;
-- exclusive operation
COMMIT;
```

### Run VACUUM when the database is not in use

```bash
sqlite3 mydb.sqlite 'VACUUM;'
```

## Examples

```sql
VACUUM;
-- Error: unable to use exclusive lock
-- Another connection has a shared lock
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
