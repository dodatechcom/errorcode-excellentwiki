---
title: "SQLITE_BUSY: database is locked"
description: "The SQLite database is locked because another connection holds a lock on it."
tools: ["sqlite"]
error-types: ["database-error"]
severities: ["error"]
tags: ["database", "locking", "concurrency"]
weight: 5
---

The `SQLITE_BUSY` error occurs when SQLite cannot acquire a lock on the database because another connection or process already holds a conflicting lock. SQLite uses file-level locking, so only one writer can modify the database at a time.

## Common Causes

- Another process or thread is holding a write lock on the database
- A long-running transaction is blocking other connections
- The WAL (Write-Ahead Logging) file is locked by another process
- Concurrent write attempts exceed SQLite's locking capabilities

## How to Fix

Increase the busy timeout so SQLite waits longer before failing:

```sql
PRAGMA busy_timeout = 5000;
```

Ensure your application properly closes connections after use:

```bash
# Check for processes using the database
lsof your_database.db

# Kill a stuck process
kill <PID>
```

## Examples

```sql
-- Attempting to write while another connection holds a lock
BEGIN IMMEDIATE;
-- Error: SQLITE_BUSY: database is locked
```

A common scenario is two terminals opening the same database:

```bash
# Terminal 1: starts a transaction
sqlite3 mydb.db "BEGIN EXCLUSIVE;"

# Terminal 2: tries to write
sqlite3 mydb.db "INSERT INTO users VALUES (1, 'Alice');"
-- Error: SQLITE_BUSY: database is locked
```

## Related Errors

- [no such table]({{< relref "/tools/sqlite/no-such-table" >}})
