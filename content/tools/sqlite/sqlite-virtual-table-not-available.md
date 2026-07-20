---
title: "[Solution] SQLite virtual table not available"
description: "A virtual table module is not available or not loaded."
tools: ["sqlite"]
error-types: ["query-error"]
severities: ["error"]
---


# [Solution] SQLite virtual table not available

SQLite produces **virtual table not available** when a virtual table module is not available or not loaded. This error can occur in various contexts and requires understanding the specific trigger.

## Common Causes

- The FTS5 or other virtual table extension is not compiled in.
- A custom virtual table module was not loaded.
- The module name is misspelled.

## How to Fix

### Load the required extension

```sql
SELECT load_extension('fts5');
```

### Check available virtual table modules

```sql
PRAGMA compile_options;
-- Look for ENABLE_FTS5, etc.
```

### Use a built-in virtual table

```sql
CREATE VIRTUAL TABLE t USING fts5(content);
```

## Examples

```sql
CREATE VIRTUAL TABLE docs USING fts5(content);
-- Error: no such module: fts5 (if FTS5 not compiled)
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
