---
title: "[Solution] SQLite json_valid() not Boolean"
description: "The json_valid() function did not receive arguments it can evaluate."
tools: ["sqlite"]
error-types: ["query-error"]
severities: ["error"]
---


# [Solution] SQLite json_valid() not Boolean

SQLite JSON1 extension produces **json_valid() not Boolean** when the json_valid() function did not receive arguments it can evaluate. The JSON1 extension provides powerful JSON manipulation functions for SQLite.

## Common Causes

- The input is NULL.
- The function is used in a context expecting a different type.
- The argument count is wrong.

## How to Fix

### Pass a single string argument

```sql
SELECT json_valid('{"a": 1}');  -- returns 1
SELECT json_valid('not json');    -- returns 0
```

### Handle NULL input

```sql
SELECT json_valid(COALESCE(col, ''));
```

### Use in WHERE clause to filter valid JSON

```sql
SELECT * FROM t WHERE json_valid(json_col);
```

## Examples

```sql
SELECT json_valid(NULL);
-- Returns NULL (not an error, but unexpected)
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
