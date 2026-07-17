---
title: "[Solution] SQLite I/O Error"
description: "Fix SQLite I/O errors. Resolve disk read/write failures and filesystem issues."
tools: ["sqlite"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# SQLite I/O Error

An I/O error means SQLite encountered a problem reading from or writing to the database file on disk. The OS-level file operation failed.

## Common Causes

- The disk is full, preventing writes
- The database file or journal file has incorrect permissions
- A network filesystem (NFS) is experiencing connectivity issues
- The file system does not support the required locking

## How to Fix

### Check Disk Space

```bash
df -h
du -sh your_database.db
```

### Verify File Permissions

```bash
ls -la your_database.db
chmod 644 your_database.db
chown app-user:app-user your_database.db
```

### Check Journal File Permissions

```bash
ls -la your_database.db-journal
ls -la your_database.db-wal
# These must be writable by the process
```

### Move Database to Local Disk

```bash
# NFS/remote filesystems can cause I/O errors
# Copy to local disk
cp /mnt/nfs/app.db /var/lib/app/app.db
```

### Enable WAL Mode for Better Concurrency

```sql
PRAGMA journal_mode=WAL;
```

### Recover After Disk Full

```bash
# Free disk space
df -h
sudo journalctl --vacuum-size=100M

# Then check integrity
sqlite3 your_database.db "PRAGMA integrity_check;"
```

## Examples

```sql
-- Disk full
INSERT INTO logs SELECT * FROM huge_table;
-- Error: disk I/O error
-- Fix: free disk space or add more storage

-- Permission denied on journal
-- Error: disk I/O error
-- Fix: chmod 644 your_database.db-journal
```

## Related Errors

- [Malformed DB]({{< relref "/tools/sqlite/malformed-db" >}}) — database structure is corrupted
- [Database Locked]({{< relref "/tools/sqlite/database-locked" >}}) — write lock contention
