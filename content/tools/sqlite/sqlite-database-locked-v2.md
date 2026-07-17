---
title: "SQLite - database is locked (BUSY)"
description: "SQLite database is locked by another connection and cannot be accessed within the busy timeout"
tools: ["sqlite"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

SQLite "database is locked (SQLITE_BUSY)" error occurs when a connection tries to access a database that is currently locked by another connection. This is common in concurrent applications where multiple connections try to write simultaneously.

## Common Causes

- Another connection holding a write lock
- Long-running transaction preventing other access
- Default busy timeout too short
- Using journal mode instead of WAL for concurrency
- Multiple processes accessing the same database file

## How to Fix

1. Set a busy timeout:

```python
import sqlite3
conn = sqlite3.connect('mydb.sqlite', timeout=30)
# Wait up to 30 seconds for lock to be released
```

2. Enable WAL (Write-Ahead Logging) mode for better concurrency:

```sql
PRAGMA journal_mode=WAL;
PRAGMA busy_timeout=5000;
```

3. Use connection pooling with proper timeout:

```javascript
const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database('mydb.sqlite', sqlite3.OPEN_READWRITE, (err) => {
  if (err) console.error(err.message);
});

db.configure('busyTimeout', 30000);
```

4. Close connections promptly after use:

```python
conn = sqlite3.connect('mydb.sqlite')
try:
    conn.execute('INSERT INTO users VALUES (1, "John")')
    conn.commit()
finally:
    conn.close()  # Always close in finally block
```

5. Use single connection per process:

```python
# Create a single connection per process
import threading
local = threading.local()

def get_connection():
    if not hasattr(local, 'conn'):
        local.conn = sqlite3.connect('mydb.sqlite', timeout=30)
    return local.conn
```

6. Check WAL mode status:

```bash
sqlite3 mydb.sqlite "PRAGMA journal_mode;"
# Should return: wal
```

## Examples

```python
import sqlite3
conn = sqlite3.connect('mydb.sqlite')
cursor = conn.cursor()
# Error: database is locked
cursor.execute('INSERT INTO users VALUES (1, "John")')

# Fix: set timeout
conn = sqlite3.connect('mydb.sqlite', timeout=30)
```

```sql
-- Set WAL mode for better concurrency
PRAGMA journal_mode=WAL;
PRAGMA busy_timeout=10000;
INSERT INTO users VALUES (1, 'John');
```

## Related Errors

- [Connection error]({{< relref "/tools/sqlite/sqlite-connection-error" >}})
- [Constraint error]({{< relref "/tools/sqlite/sqlite-constraint-error" >}})
