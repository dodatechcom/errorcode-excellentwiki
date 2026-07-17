---
title: "SQLite Backup Error"
description: "SQLite backup operation fails."
tools: ["sqlite"]
error-types: ["database-error"]
severities: ["error"]
tags: ["sqlite", "backup", "dump", "export", "restore"]
weight: 5
---

# SQLite Backup Error

A SQLite backup error occurs when attempting to backup, dump, or export the database. This can be caused by file access issues, disk space, or database corruption.

## Common Causes

- Insufficient disk space for backup
- Database locked during backup
- Permission issues on backup location
- Database corruption preventing backup

## How to Fix

### Use .backup Command

```bash
sqlite3 mydb.sqlite ".backup backup.db"
```

### Use .dump Command

```bash
sqlite3 mydb.sqlite ".dump" > backup.sql
```

### Use Online Backup API

```python
import sqlite3

source = sqlite3.connect('mydb.sqlite')
dest = sqlite3.connect('backup.db')
source.backup(dest)
source.close()
dest.close()
```

### Backup with Timestamp

```bash
sqlite3 mydb.sqlite ".backup backup_$(date +%Y%m%d).db"
```

### Check Disk Space

```bash
df -h .
```

### Restore from Backup

```bash
# From .backup
cp backup.db mydb.sqlite

# From .dump
sqlite3 mydb.sqlite < backup.sql
```

### Automated Backup Script

```bash
#!/bin/bash
DB="mydb.sqlite"
BACKUP_DIR="/backups"
DATE=$(date +%Y%m%d_%H%M%S)
sqlite3 "$DB" ".backup $BACKUP_DIR/backup_$DATE.db"
```

## Examples

```bash
# Create backup
sqlite3 mydb.sqlite ".backup mydb_backup.db"

# Restore backup
cp mydb_backup.db mydb.sqlite
sqlite3 mydb.sqlite "PRAGMA integrity_check;"
# OK
```

## Related Errors

- [Connection Error]({{< relref "/tools/sqlite/sqlite-connection-error" >}}) — connection failure
- [Corruption Error]({{< relref "/tools/sqlite/sqlite-corruption-error" >}}) — database corrupted
- [Migration Error]({{< relref "/tools/sqlite/sqlite-migration-error" >}}) — schema migration error
