---
title: "[Solution] SQLite function not found"
description: "An SQL statement references a function that does not exist in the current SQLite build."
tools: ["sqlite"]
error-types: ["query-error"]
severities: ["error"]
---


# [Solution] SQLite function not found

SQLite produces **function not found** when an sql statement references a function that does not exist in the current sqlite build. This error can occur in various contexts and requires understanding the specific trigger.

## Common Causes

- The function requires an extension that is not loaded.
- A typo in the function name.
- The function is not available in the compiled SQLite version.

## How to Fix

### Load the required extension

```sql
SELECT load_extension('extension_name');
```

### Check available functions

```sql
PRAGMA compile_options;  -- lists compiled features
```

### Use an equivalent built-in function

```sql
-- Instead of custom: use SUBSTR, INSTR, etc.
```

## Examples

```sql
SELECT REGEXP('abc', 'b');
-- Error: no such function: REGEXP
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
