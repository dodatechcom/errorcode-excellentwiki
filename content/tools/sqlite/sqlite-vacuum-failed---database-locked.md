---
title: "[Solution] SQLite VACUUM failed - database locked"
description: "VACUUM could not run because the database was locked by another connection."
tools: ["sqlite"]
error-types: ["database-error"]
severities: ["error"]
---


# [Solution] SQLite VACUUM failed - database locked

SQLite reports **VACUUM failed - database locked** when vacuum could not run because the database was locked by another connection. VACUUM and PRAGMA are powerful maintenance tools that require careful use.

## Common Causes

- Another connection holds a lock on the database.
- A long-running read transaction is preventing VACUUM.
- VACUUM requires exclusive access.

## How to Fix

### Close all other connections before running VACUUM

```bash
sqlite3 mydb.sqlite 'VACUUM;'
```

### Use PRAGMA wal_checkpoint to release WAL locks

```sql
PRAGMA wal_checkpoint(TRUNCATE);
VACUUM;
```

### Schedule VACUUM during low-traffic periods

```bash
# Run during maintenance window
```

## Examples

```sql
-- Session 1: holding a read lock
BEGIN;
SELECT * FROM large_table;
-- Session 2:
VACUUM;
-- Error: database is locked
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
