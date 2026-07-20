---
title: "[Solution] SQLite disk I/O error"
description: "SQLite encountered an error while performing a disk read or write operation."
tools: ["sqlite"]
error-types: ["io-error"]
severities: ["error"]
---


# [Solution] SQLite disk I/O error

SQLite encounters **disk I/O error** when sqlite encountered an error while performing a disk read or write operation. These errors typically relate to the underlying file system and require careful recovery steps.

## Common Causes

- Disk is full.
- File system corruption.
- Hardware failure (bad sectors).

## How to Fix

### Check disk space

```bash
df -h .
```

### Verify file system integrity

```bash
# Linux:
fsck /dev/sda1
# macOS:
diskutil verifyVolume /
```

### Run PRAGMA integrity_check

```sql
PRAGMA integrity_check;
```

## Examples

```bash
sqlite3 mydb.sqlite "INSERT INTO t VALUES (1);"
-- Error: disk I/O error
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
