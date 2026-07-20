---
title: "[Solution] SQLite deadlock detected"
description: "Two or more connections are waiting for each other to release locks, creating a circular dependency."
tools: ["sqlite"]
error-types: ["locking-error"]
severities: ["error"]
---


# [Solution] SQLite deadlock detected

SQLite reports **deadlock detected** when two or more connections are waiting for each other to release locks, creating a circular dependency. Proper transaction management is essential for data integrity.

## Common Causes

- Connection A locks table 1 then tries to lock table 2.
- Connection B locks table 2 then tries to lock table 1.
- Both connections are waiting indefinitely.

## How to Fix

### Lock tables in a consistent order across all connections

```sql
-- Always lock table A before table B
BEGIN IMMEDIATE;
SELECT * FROM table_a;
SELECT * FROM table_b;
COMMIT;
```

### Minimize transaction duration

```sql
BEGIN IMMEDIATE;
-- fast operations only
COMMIT;
```

### Use WAL mode to reduce lock contention

```sql
PRAGMA journal_mode = WAL;
```

## Examples

```sql
-- Connection A:
BEGIN IMMEDIATE;
UPDATE table_a SET x = 1;  -- locks table_a
UPDATE table_b SET x = 2;  -- waiting for table_b
-- Connection B:
BEGIN IMMEDIATE;
UPDATE table_b SET x = 3;  -- locks table_b
UPDATE table_a SET x = 4;  -- waiting for table_a → DEADLOCK
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
