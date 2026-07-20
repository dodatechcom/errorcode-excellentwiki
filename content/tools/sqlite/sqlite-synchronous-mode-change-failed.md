---
title: "[Solution] SQLite synchronous mode change failed"
description: "The PRAGMA synchronous could not be changed to the requested level."
tools: ["sqlite"]
error-types: ["database-error"]
severities: ["error"]
---


# [Solution] SQLite synchronous mode change failed

SQLite reports **synchronous mode change failed** when the pragma synchronous could not be changed to the requested level. VACUUM and PRAGMA are powerful maintenance tools that require careful use.

## Common Causes

- Another connection holds a lock.
- The database is read-only.
- The value is not one of the valid synchronous modes.

## How to Fix

### Use a valid synchronous mode

```sql
-- 0 = OFF, 1 = NORMAL, 2 = FULL, 3 = EXTRA
PRAGMA synchronous = NORMAL;
```

### Change synchronous mode when no other connections are active

```sql
PRAGMA synchronous = NORMAL;
```

### Understand the trade-offs

```sql
-- OFF: fastest but less safe
-- NORMAL: good balance for WAL mode
-- FULL: safest, recommended for DELETE journal mode
```

## Examples

```sql
PRAGMA synchronous = 5;
-- Error: bad value for synchronous: 5
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
