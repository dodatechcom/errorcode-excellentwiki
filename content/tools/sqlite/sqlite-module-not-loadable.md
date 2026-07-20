---
title: "[Solution] SQLite module not loadable"
description: "The load_extension() function could not load the specified extension module."
tools: ["sqlite"]
error-types: ["query-error"]
severities: ["error"]
---


# [Solution] SQLite module not loadable

SQLite produces **module not loadable** when the load_extension() function could not load the specified extension module. This error can occur in various contexts and requires understanding the specific trigger.

## Common Causes

- The extension file does not exist.
- The extension is not compatible with the SQLite version.
- Extension loading is disabled for security.

## How to Fix

### Verify the extension file path

```bash
ls -la /path/to/extension.so
```

### Enable extension loading

```sql
-- In application code:
-- conn.enable_load_extension(True)
```

### Check SQLite version compatibility

```sql
SELECT sqlite_version();
```

## Examples

```sql
SELECT load_extension('nonexistent_extension');
-- Error: unable to load extension
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
