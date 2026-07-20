---
title: "[Solution] SQLite PRAGMA value out of range"
description: "A PRAGMA was assigned a value that is outside the acceptable range."
tools: ["sqlite"]
error-types: ["database-error"]
severities: ["error"]
---


# [Solution] SQLite PRAGMA value out of range

SQLite reports **PRAGMA value out of range** when a pragma was assigned a value that is outside the acceptable range. VACUUM and PRAGMA are powerful maintenance tools that require careful use.

## Common Causes

- The value exceeds the minimum or maximum allowed.
- A negative value was given where only positives are valid.
- The value type is wrong (string where integer is expected).

## How to Fix

### Check the valid range for the PRAGMA

```sql
-- page_size: 512 to 65536 (must be power of 2)
-- cache_size: negative = KB, positive = pages
-- busy_timeout: milliseconds (0+)
```

### Use valid values

```sql
PRAGMA page_size = 4096;  -- valid power of 2
PRAGMA cache_size = -8000;  -- 8000 KB
```

### Use the default if unsure

```sql
PRAGMA cache_size = -2000;  -- default ~2MB
```

## Examples

```sql
PRAGMA page_size = 1000;
-- Error: page_size must be a power of two between 512 and 65536
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
