---
title: "SQLite SQLITE_CORRUPT (Error 11)"
description: "Understand and resolve SQLite SQLITE_CORRUPT (result code 11): Database disk image is malformed."
tools: ["sqlite"]
error-types: ["corruption-error"]
severities: ["error"]
---


# SQLite SQLITE_CORRUPT (Error 11)

SQLite returns **SQLITE_CORRUPT** (result code 11) when database disk image is malformed. This result code is one of the primary error codes defined in the SQLite C API and is commonly encountered when interacting with SQLite databases from applications.

## Common Causes

- The operation triggered an internal corrupt condition.
- Misuse of the SQLite API or incorrect parameter values.
- Environmental constraints such as insufficient disk space or permissions.

## How to Fix

### Check the exact error message

```bash
sqlite3 mydb.sqlite "SELECT * FROM test;"
-- Read the full error text to pinpoint the issue
```

### Use PRAGMA integrity_check to diagnose corruption

```sql
PRAGMA integrity_check;
```

### Review your SQL statement for syntax and logic errors

```sql
-- Example: verify table and column names
PRAGMA table_info(my_table);
```

## Examples

```bash
sqlite3 mydb.sqlite "SELECT * FROM nonexistent;"
-- Error: no such table: nonexistent
-- This can surface as SQLITE_CORRUPTION_ERROR under certain conditions
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
