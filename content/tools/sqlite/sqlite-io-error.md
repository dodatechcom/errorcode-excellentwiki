---
title: "SQLite I/O Error"
description: "SQLite encounters an I/O error while reading or writing the database."
tools: ["sqlite"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# SQLite I/O Error

A SQLite I/O error occurs when the database engine encounters an error while reading from or writing to the database file. This is typically caused by disk issues or file system errors.

## Common Causes

- Disk full or insufficient disk space
- Bad sectors on disk
- File system corruption
- Permission issues on the database file
- Network file system (NFS) issues

## How to Fix

### Check Disk Space

```bash
df -h .
```

### Check File Permissions

```bash
ls -la mydb.sqlite
chmod 644 mydb.sqlite
```

### Check for Disk Errors

```bash
# Linux
dmesg | grep -i error
smartctl -a /dev/sda
```

### Use Local Filesystem

```bash
# Avoid NFS for SQLite databases
# Use local storage instead
```

### Check File System Type

```bash
df -T .
# SQLite works best on local ext4, NTFS, or APFS
```

### Verify Database File

```bash
sqlite3 mydb.sqlite "PRAGMA integrity_check;"
```

## Examples

```bash
sqlite3 mydb.sqlite "INSERT INTO users VALUES (1, 'Alice');"
Error: disk I/O error

# Check disk space
df -h .
# Filesystem      Size  Used Avail Use% Mounted on
# /dev/sda1       10G   10G     0 100% /
# Fix: free up disk space
```

## Related Errors

- [Connection Error]({{< relref "/tools/sqlite/sqlite-connection-error" >}}) — connection failure
- [Corruption Error]({{< relref "/tools/sqlite/sqlite-corruption-error" >}}) — database corrupted
