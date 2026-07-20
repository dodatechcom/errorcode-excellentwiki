---
title: "[Solution] SQLite file is not a database"
description: "The file opened by SQLite does not contain a valid SQLite database header."
tools: ["sqlite"]
error-types: ["corruption-error"]
severities: ["error"]
---


# [Solution] SQLite file is not a database

SQLite encounters **file is not a database** when the file opened by sqlite does not contain a valid sqlite database header. These errors typically relate to the underlying file system and require careful recovery steps.

## Common Causes

- The file is not a SQLite database (e.g., it is a CSV or text file).
- The file was truncated or partially written.
- A non-SQLite file was renamed to .sqlite.

## How to Fix

### Verify the file type

```bash
file mydb.sqlite
# Should say: SQLite 3.x database
```

### Check the file header

```bash
xxd mydb.sqlite | head -1
# Should start with: 53 51 4c 69 74 65 20 66 6f 72 6d 61 74 20 31 00
```

### Restore from backup if the file is corrupted

```bash
cp backup.db mydb.sqlite
```

## Examples

```bash
sqlite3 fake.sqlite "SELECT 1;"
-- Error: file is not a database
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
