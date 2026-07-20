---
title: "[Solution] SQLite PRAGMA not recognized"
description: "An unrecognized PRAGMA name was used."
tools: ["sqlite"]
error-types: ["database-error"]
severities: ["error"]
---


# [Solution] SQLite PRAGMA not recognized

SQLite reports **PRAGMA not recognized** when an unrecognized pragma name was used. VACUUM and PRAGMA are powerful maintenance tools that require careful use.

## Common Causes

- A typo in the PRAGMA name.
- The PRAGMA is not supported in the current SQLite version.
- An extension PRAGMA is used without loading the extension.

## How to Fix

### Check the SQLite documentation for valid PRAGMA names

```sql
PRAGMA compile_options;  -- lists available features
```

### Verify the PRAGMA name spelling

```sql
PRAGMA journal_mode;  -- correct
PRAGMA journl_mode;   -- typo
```

### Check the SQLite version

```sql
SELECT sqlite_version();
```

## Examples

```sql
PRAGMA journl_mode = WAL;
-- Error: unrecognized pragma name: journl_mode
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
