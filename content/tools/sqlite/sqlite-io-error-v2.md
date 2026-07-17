---
title: "SQLite - I/O error (SQLITE_IOERR)"
description: "SQLite encounters an input/output error while reading from or writing to the database file"
tools: ["sqlite"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

SQLite I/O error (SQLITE_IOERR) occurs when the database engine encounters a failure while performing disk I/O operations. This is a broad error category that can have many specific causes related to the underlying filesystem or storage device.

## Common Causes

- Disk full or insufficient disk space
- Filesystem corruption
- I/O device error (bad disk sectors)
- Permission denied on write operations
- Network filesystem (NFS) instability
- File locking issues on network shares

## How to Fix

1. Check available disk space:

```bash
df -h /path/to/database/
```

2. Free up disk space:

```bash
# Remove old logs
find /var/log -name "*.gz" -delete
# Check for large files
du -sh /path/to/database/* | sort -rh | head -10
```

3. Verify filesystem health:

```bash
sudo fsck /dev/sda1
dmesg | grep -i error
```

4. Test disk write capability:

```bash
dd if=/dev/zero of=/path/to/database/testfile bs=1M count=10
rm /path/to/database/testfile
```

5. Use local filesystem instead of NFS:

```bash
# If using NFS, ensure proper locking support
mount -t nfs -o lock,hard,timeo=600 server:/export /mnt/data
```

6. Enable proper journal mode:

```sql
PRAGMA journal_mode=WAL;
PRAGMA synchronous=NORMAL;
```

## Examples

```python
import sqlite3
conn = sqlite3.connect('/mnt/nfs/mydb.sqlite')
conn.execute("INSERT INTO logs VALUES (?, ?)", (1, "test"))
# Error: disk I/O error (NFS issues)

# Fix: use local storage
conn = sqlite3.connect('/var/lib/mydb.sqlite')
```

```bash
# Check disk I/O errors
dmesg | tail -20
# [sda] disk I/O error, sector 12345678
# Fix: replace failing disk
```

## Related Errors

- [Connection error]({{< relref "/tools/sqlite/sqlite-connection-error" >}})
- [Corruption error]({{< relref "/tools/sqlite/sqlite-corruption-error-v2" >}})
