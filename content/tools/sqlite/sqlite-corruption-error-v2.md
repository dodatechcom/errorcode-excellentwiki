---
title: "SQLite - database disk image is malformed"
description: "SQLite detects corruption in the database file, indicating data integrity issues"
tools: ["sqlite"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

The "database disk image is malformed" error occurs when SQLite detects that the database file is corrupted. This can happen due to hardware failures, improper shutdowns, or software bugs that write invalid data to the database file.

## Common Causes

- Power failure or system crash during a write operation
- Disk hardware failure or bad sectors
- Concurrent access without proper locking
- Software bug writing invalid data to the database
- Filesystem corruption

## How to Fix

1. Attempt to dump and restore the database:

```bash
sqlite3 corrupt.db ".dump" | sqlite3 new.db
```

2. Check database integrity:

```bash
sqlite3 mydb.sqlite "PRAGMA integrity_check;"
# Returns "ok" if healthy
```

3. Use the `.recover` command for badly corrupted databases:

```bash
sqlite3 corrupt.db ".recover" | sqlite3 recovered.db
```

4. Enable WAL mode to prevent future corruption:

```sql
PRAGMA journal_mode=WAL;
PRAGMA synchronous=NORMAL;
```

5. Set up automatic integrity checks:

```python
def check_database(path):
    conn = sqlite3.connect(path)
    result = conn.execute("PRAGMA integrity_check").fetchone()
    conn.close()
    return result[0] == 'ok'
```

6. Create regular backups:

```bash
sqlite3 mydb.sqlite ".backup backup.db"
```

## Examples

```python
import sqlite3
conn = sqlite3.connect('mydb.sqlite')
# Error: database disk image is malformed
conn.execute("SELECT * FROM users")

# Fix: dump and restore
import subprocess
subprocess.run(['sqlite3', 'mydb.sqlite', '.dump'], stdout=open('dump.sql', 'w'))
subprocess.run(['sqlite3', 'new.db'], stdin=open('dump.sql'))
```

```bash
# Attempt recovery
sqlite3 corrupted.db ".recover" > recovered.sql
sqlite3 new.db < recovered.sql
sqlite3 new.db "PRAGMA integrity_check;"
# ok
```

## Related Errors

- [I/O error]({{< relref "/tools/sqlite/sqlite-io-error" >}})
- [Memory error]({{< relref "/tools/sqlite/sqlite-memory-error" >}})
