---
title: "[Solution] SQLite attach filename not found"
description: "The ATTACH DATABASE statement cannot find the specified database file."
tools: ["sqlite"]
error-types: ["database-error"]
severities: ["error"]
---


# [Solution] SQLite attach filename not found

SQLite produces **attach filename not found** when the attach database statement cannot find the specified database file. The ATTACH/DETACH mechanism allows working with multiple databases simultaneously.

## Common Causes

- The file path is incorrect.
- The file does not exist.
- The path contains special characters or spaces.

## How to Fix

### Use the absolute path

```sql
ATTACH DATABASE '/home/user/data/mydb.sqlite' AS extra;
```

### Quote paths with spaces

```sql
ATTACH DATABASE '/path with spaces/db.sqlite' AS extra;
```

### Verify the file exists

```bash
ls -la /path/to/db.sqlite
```

## Examples

```sql
ATTACH DATABASE 'missing.sqlite' AS extra;
-- Error: unable to open database file
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
