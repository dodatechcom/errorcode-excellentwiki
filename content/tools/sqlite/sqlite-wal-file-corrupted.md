---
title: "[Solution] SQLite WAL file corrupted"
description: "The Write-Ahead Logging (WAL) file has become corrupted."
tools: ["sqlite"]
error-types: ["corruption-error"]
severities: ["error"]
---


# [Solution] SQLite WAL file corrupted

SQLite encounters **WAL file corrupted** when the write-ahead logging (wal) file has become corrupted. These errors typically relate to the underlying file system and require careful recovery steps.

## Common Causes

- Power failure during WAL write.
- Disk failure corrupted the WAL file.
- A bug in the application caused WAL corruption.

## How to Fix

### Delete the WAL file to recover

```bash
rm -f mydb.sqlite-wal
# SQLite will recreate the WAL on next open
```

### Force a WAL checkpoint

```sql
PRAGMA wal_checkpoint(TRUNCATE);
```

### Restore from backup

```bash
cp backup.db mydb.sqlite
rm -f mydb.sqlite-wal mydb.sqlite-shm
```

## Examples

```bash
sqlite3 mydb.sqlite "SELECT * FROM t;"
-- Error: WAL file corrupted
rm mydb.sqlite-wal
sqlite3 mydb.sqlite "PRAGMA integrity_check;"
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
