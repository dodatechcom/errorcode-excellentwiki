---
title: "[Solution] SQLite json() parse error"
description: "The json() function could not parse the input string as valid JSON."
tools: ["sqlite"]
error-types: ["query-error"]
severities: ["error"]
---


# [Solution] SQLite json() parse error

SQLite JSON1 extension produces **json() parse error** when the json() function could not parse the input string as valid json. The JSON1 extension provides powerful JSON manipulation functions for SQLite.

## Common Causes

- The input string is not valid JSON.
- Trailing commas or missing quotes.
- The JSON contains invalid escape sequences.

## How to Fix

### Validate JSON input before calling json()

```sql
SELECT json_valid('{"a": 1}');  -- returns 1 (true)
```

### Fix common JSON syntax issues

```sql
-- Wrong: {a: 1}
-- Right: {"a": 1}
SELECT json('{"a": 1}');
```

### Use json_valid() as a guard

```sql
SELECT CASE WHEN json_valid(col) THEN json(col) ELSE NULL END FROM t;
```

## Examples

```sql
SELECT json('{a: 1}');
-- Error: malformed JSON
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
