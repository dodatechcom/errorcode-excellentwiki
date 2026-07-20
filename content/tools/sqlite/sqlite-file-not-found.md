---
title: "[Solution] SQLite file not found"
description: "The database file specified in the connection string does not exist."
tools: ["sqlite"]
error-types: ["io-error"]
severities: ["error"]
---


# [Solution] SQLite file not found

SQLite encounters **file not found** when the database file specified in the connection string does not exist. These errors typically relate to the underlying file system and require careful recovery steps.

## Common Causes

- The file path is incorrect.
- The file was deleted.
- The file is in a different directory than expected.

## How to Fix

### Use the absolute path

```bash
sqlite3 /full/path/to/mydb.sqlite
```

### Check the current directory

```bash
pwd
ls *.sqlite
```

### Create the file if it should exist

```bash
sqlite3 mydb.sqlite "SELECT 1;"
# Creates the file if it does not exist
```

## Examples

```bash
sqlite3 /wrong/path/mydb.sqlite
-- Error: unable to open database file
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
