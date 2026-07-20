---
title: "[Solution] SQLite mmap_size limit exceeded"
description: "The PRAGMA mmap_size was set higher than the system limit or available memory."
tools: ["sqlite"]
error-types: ["database-error"]
severities: ["error"]
---


# [Solution] SQLite mmap_size limit exceeded

SQLite reports **mmap_size limit exceeded** when the pragma mmap_size was set higher than the system limit or available memory. VACUUM and PRAGMA are powerful maintenance tools that require careful use.

## Common Causes

- The value exceeds /proc/sys/vm/mmap_max_bytes.
- Insufficient virtual address space.
- The database file is smaller than the mmap size.

## How to Fix

### Check the system mmap limit

```bash
cat /proc/sys/vm/mmap_max_bytes
```

### Set mmap_size to a reasonable value

```sql
PRAGMA mmap_size = 268435456;  -- 256 MB
```

### Disable mmap if not needed

```sql
PRAGMA mmap_size = 0;
```

## Examples

```sql
PRAGMA mmap_size = 10737418240;
-- Error: mmap size exceeds system limit
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
