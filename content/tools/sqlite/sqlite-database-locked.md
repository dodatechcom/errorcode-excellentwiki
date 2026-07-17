---
title: "SQLite Database Locked"
description: "SQLite database is locked by another connection or process."
tools: ["sqlite"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# SQLite Database Locked

The `SQLITE_BUSY` error occurs when SQLite cannot acquire a lock on the database because another connection or process already holds a conflicting lock. SQLite uses file-level locking.

## Common Causes

- Another process holds a write lock
- Long-running transaction blocking others
- WAL file locked by another process
- Concurrent write attempts

## How to Fix

### Increase Busy Timeout

```sql
PRAGMA busy_timeout = 5000;
```

### Check for Locking Processes

```bash
lsof your_database.db
```

### Use WAL Mode

```sql
PRAGMA journal_mode=WAL;
```

### Close Connections Properly

```python
import sqlite3
conn = sqlite3.connect('mydb.sqlite')
try:
    conn.execute('INSERT INTO users VALUES (1, "Alice")')
    conn.commit()
finally:
    conn.close()
```

### Use Connection Pooling

```python
import sqlite3
from contextlib import contextmanager

@contextmanager
def get_connection():
    conn = sqlite3.connect('mydb.sqlite')
    try:
        yield conn
    finally:
        conn.close()
```

## Examples

```sql
-- Terminal 1: starts a transaction
BEGIN IMMEDIATE;

-- Terminal 2: tries to write
INSERT INTO users VALUES (1, 'Alice');
-- Error: SQLITE_BUSY: database is locked
```

## Related Errors

- [Connection Error]({{< relref "/tools/sqlite/sqlite-connection-error" >}}) — connection failure
- [I/O Error]({{< relref "/tools/sqlite/io-error2" >}}) — I/O error
