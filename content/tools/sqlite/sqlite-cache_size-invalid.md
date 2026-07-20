---
title: "[Solution] SQLite cache_size invalid"
description: "The PRAGMA cache_size was assigned an invalid value."
tools: ["sqlite"]
error-types: ["database-error"]
severities: ["error"]
---


# [Solution] SQLite cache_size invalid

SQLite reports **cache_size invalid** when the pragma cache_size was assigned an invalid value. VACUUM and PRAGMA are powerful maintenance tools that require careful use.

## Common Causes

- The value is zero or negative in an unexpected way.
- The value exceeds memory limits.
- The value type is incorrect.

## How to Fix

### Use a positive value for page count or negative for KB

```sql
PRAGMA cache_size = 2000;  -- 2000 pages
PRAGMA cache_size = -8000;  -- 8000 KB
```

### Set a reasonable cache size

```sql
-- Default is ~2MB (-2000)
-- For large databases, increase to 64MB:
PRAGMA cache_size = -65536;
```

### Verify the current cache size

```sql
PRAGMA cache_size;
```

## Examples

```sql
PRAGMA cache_size = 0;
-- Error: cache_size must be greater than 0
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
