---
title: "[Solution] SQLite page_size too small"
description: "The PRAGMA page_size was set to a value below the minimum allowed (512 bytes)."
tools: ["sqlite"]
error-types: ["database-error"]
severities: ["error"]
---


# [Solution] SQLite page_size too small

SQLite reports **page_size too small** when the pragma page_size was set to a value below the minimum allowed (512 bytes). VACUUM and PRAGMA are powerful maintenance tools that require careful use.

## Common Causes

- The value is less than 512.
- The value is not a power of 2.
- page_size was set after the database already has tables.

## How to Fix

### Use a valid page size (power of 2, 512-65536)

```sql
PRAGMA page_size = 4096;  -- 4KB is common default
```

### Set page_size on an empty database only

```sql
-- Create a fresh database, set page_size, then create tables
PRAGMA page_size = 8192;
CREATE TABLE t (x INTEGER);
```

### Use VACUUM to change page_size of existing database

```sql
VACUUM;  -- rebuilds with current page_size
```

## Examples

```sql
CREATE TABLE t (x INTEGER);
PRAGMA page_size = 512;
-- Error: page_size must be set before any tables are created
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
