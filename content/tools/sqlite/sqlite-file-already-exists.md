---
title: "[Solution] SQLite file already exists"
description: "An attempt to create a database failed because the file already exists and was not expected to."
tools: ["sqlite"]
error-types: ["io-error"]
severities: ["error"]
---


# [Solution] SQLite file already exists

SQLite encounters **file already exists** when an attempt to create a database failed because the file already exists and was not expected to. These errors typically relate to the underlying file system and require careful recovery steps.

## Common Causes

- The database file was already created.
- A previous creation attempt left the file.
- Missing IF NOT EXISTS equivalent (SQLite does not have this for file creation).

## How to Fix

### Remove the existing file if a fresh database is needed

```bash
rm -f mydb.sqlite
sqlite3 mydb.sqlite "CREATE TABLE t (x INTEGER);"
```

### Check if the existing file is valid

```bash
sqlite3 mydb.sqlite '.tables'
```

### Use a different filename

```bash
sqlite3 mydb_v2.sqlite "CREATE TABLE t (x INTEGER);"
```

## Examples

```bash
touch mydb.sqlite
sqlite3 mydb.sqlite "CREATE TABLE t (x INTEGER);"
# File exists but may be empty — SQLite will try to open it
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
