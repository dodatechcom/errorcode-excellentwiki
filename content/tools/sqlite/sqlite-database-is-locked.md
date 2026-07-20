---
title: "[Solution] SQLite database is locked"
description: "A connection attempted to access the database while another connection held a write lock."
tools: ["sqlite"]
error-types: ["locking-error"]
severities: ["error"]
---


# [Solution] SQLite database is locked

SQLite reports **database is locked** when a connection attempted to access the database while another connection held a write lock. Proper transaction management is essential for data integrity.

## Common Causes

- Another process or thread is writing to the database.
- A long-running write transaction is blocking readers.
- The busy timeout is too short.

## How to Fix

### Increase the busy timeout

```sql
PRAGMA busy_timeout = 5000;  -- 5 seconds
```

### Use WAL mode for concurrent reads and writes

```sql
PRAGMA journal_mode = WAL;
```

### Shorten write transactions

```sql
BEGIN IMMEDIATE;
-- do fast writes
COMMIT;
```

## Examples

```sql
-- Session 1:
BEGIN IMMEDIATE;
UPDATE users SET name = 'Alice';
-- Session 2:
SELECT * FROM users;
-- Error: database is locked
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
