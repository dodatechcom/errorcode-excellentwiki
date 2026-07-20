---
title: "[Solution] SQLite json_set() not valid"
description: "The json_set() function received invalid arguments or produced invalid JSON."
tools: ["sqlite"]
error-types: ["query-error"]
severities: ["error"]
---


# [Solution] SQLite json_set() not valid

SQLite JSON1 extension produces **json_set() not valid** when the json_set() function received invalid arguments or produced invalid json. The JSON1 extension provides powerful JSON manipulation functions for SQLite.

## Common Causes

- The value to set is not valid JSON.
- The path does not exist and cannot be created.
- The arguments have incorrect types.

## How to Fix

### Provide valid JSON values

```sql
SELECT json_set('{"a": 1}', '$.a', 2);  -- {"a": 2}
```

### Use json_insert() to add new keys

```sql
SELECT json_insert('{}', '$.b', 3);  -- {"b": 3}
```

### Use json_remove() then json_set() for replacements

```sql
SELECT json_set(json_remove('{"a":1}', '$.a'), '$.a', 2);
```

## Examples

```sql
SELECT json_set('{"a": 1}', '$.a', json('invalid'));
-- Error: invalid JSON value
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
