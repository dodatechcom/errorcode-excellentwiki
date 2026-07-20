---
title: "[Solution] SQLite JSON path syntax error"
description: "A JSON path expression uses invalid syntax for the JSON1 extension."
tools: ["sqlite"]
error-types: ["query-error"]
severities: ["error"]
---


# [Solution] SQLite JSON path syntax error

SQLite JSON1 extension produces **JSON path syntax error** when a json path expression uses invalid syntax for the json1 extension. The JSON1 extension provides powerful JSON manipulation functions for SQLite.

## Common Causes

- The path does not start with $.
- The path contains invalid characters.
- The path uses incorrect bracket notation.

## How to Fix

### Use correct JSON path syntax

```sql
-- Valid paths: $.key, $[0], $.key.subkey, $[0].key
SELECT json_extract('{"a":{"b":1}}', '$.a.b');
```

### Use bracket notation for array indices

```sql
SELECT json_extract('[1,2,3]', '$[1]');  -- returns 2
```

### Use wildcard for array elements

```sql
SELECT json_extract('[1,2,3]', '$[*]');  -- returns all
```

## Examples

```sql
SELECT json_extract('{"a": 1}', 'a');
-- Error: invalid JSON path: must begin with '$'
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
