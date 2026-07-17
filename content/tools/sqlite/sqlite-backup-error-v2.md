---
title: "SQLite - backup or restore error"
description: "SQLite backup or restore operation fails due to file access issues, corruption, or disk space problems"
tools: ["sqlite"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

SQLite backup or restore error occurs when attempting to create a backup of a database or restore from a backup file. This can fail due to file access permissions, disk space, or corruption in the source or destination.

## Common Causes

- Insufficient disk space for backup file
- Database locked by another connection during backup
- Source database corrupted
- Backup file path not writable
- `.dump` output contains errors due to corruption

## How to Fix

1. Use the `.backup` command for hot backups:

```bash
sqlite3 mydb.sqlite ".backup backup.db"
```

2. Use the backup API for programmatic backups:

```python
import sqlite3
import shutil

def backup_database(source, dest):
    source_conn = sqlite3.connect(source)
    dest_conn = sqlite3.connect(dest)
    source_conn.backup(dest_conn)
    source_conn.close()
    dest_conn.close()

backup_database('mydb.sqlite', 'backup.db')
```

3. Use `.dump` for logical backup:

```bash
sqlite3 mydb.sqlite ".dump" > backup.sql
```

4. Restore from dump:

```bash
sqlite3 restored.db < backup.sql
```

5. Handle locked database during backup:

```python
import sqlite3
import time

def safe_backup(source, dest, retries=3):
    for i in range(retries):
        try:
            src = sqlite3.connect(source)
            dst = sqlite3.connect(dest)
            src.backup(dst)
            src.close()
            dst.close()
            return True
        except sqlite3.OperationalError:
            time.sleep(1)
    return False
```

6. Use VACUUM INTO for efficient backup:

```sql
VACUUM INTO '/path/to/backup.db';
```

## Examples

```bash
# Error: database is locked during backup
$ sqlite3 mydb.sqlite ".dump" > backup.sql
Error: database is locked

# Fix: wait for locks to release
$ sqlite3 mydb.sqlite ".timeout 30000" ".dump" > backup.sql
```

```python
# Backup with corruption check
import sqlite3
conn = sqlite3.connect('mydb.sqlite')
integrity = conn.execute("PRAGMA integrity_check").fetchone()
if integrity[0] == 'ok':
    conn.execute("VACUUM INTO '/backup/mydb_backup.db'")
else:
    print("Database corrupted, attempting recovery")
    # Use .recover instead
```

## Related Errors

- [Corruption error]({{< relref "/tools/sqlite/sqlite-corruption-error-v2" >}})
- [Connection error]({{< relref "/tools/sqlite/sqlite-connection-error" >}})
