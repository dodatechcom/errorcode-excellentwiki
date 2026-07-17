---
title: "SQLite Database Corrupted"
description: "SQLite database file is corrupted and cannot be read."
tools: ["sqlite"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# SQLite Database Corrupted

A SQLite database corruption error occurs when the database file becomes unreadable due to disk errors, improper shutdown, or file system issues.

## Common Causes

- Improper shutdown during write operation
- Disk errors or bad sectors
- File system corruption
- Hardware failure

## How to Fix

### Check Integrity

```bash
sqlite3 mydb.sqlite "PRAGMA integrity_check;"
```

### Recover Data

```bash
# Export data to SQL
sqlite3 mydb.sqlite .dump > recovered.sql

# Create new database
sqlite3 newdb.sqlite < recovered.sql
```

### Use Backup Command

```bash
sqlite3 mydb.sqlite ".backup backup.db"
```

### Check for Disk Errors

```bash
chkdsk C: /f /r  # Windows
fsck /dev/sda1    # Linux
```

### Use WAL Mode for Safety

```sql
PRAGMA journal_mode=WAL;
```

## Examples

```bash
sqlite3 mydb.sqlite "SELECT * FROM users;"
Error: database disk image is malformed

# Recover:
sqlite3 mydb.sqlite .dump > recovered.sql
sqlite3 newdb.sqlite < recovered.sql
```

## Related Errors

- [I/O Error]({{< relref "/tools/sqlite/io-error2" >}}) — I/O error
- [Memory Error]({{< relref "/tools/sqlite/memory-error4" >}}) — out of memory
