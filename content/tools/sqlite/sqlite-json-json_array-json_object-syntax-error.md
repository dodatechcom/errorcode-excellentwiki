---
title: "[Solution] SQLite json_array()/json_object() syntax error"
description: "The json_array() or json_object() function received incorrect arguments."
tools: ["sqlite"]
error-types: ["query-error"]
severities: ["error"]
---


# [Solution] SQLite json_array()/json_object() syntax error

SQLite JSON1 extension produces **json_array()/json_object() syntax error** when the json_array() or json_object() function received incorrect arguments. The JSON1 extension provides powerful JSON manipulation functions for SQLite.

## Common Causes

- An odd number of arguments for json_object().
- An argument is not a valid JSON value.
- A key in json_object() is not a string.

## How to Fix

### Ensure json_object() has an even number of arguments

```sql
SELECT json_object('name', 'Alice', 'age', 30);
```

### Use json_array() for ordered lists

```sql
SELECT json_array(1, 'two', 3.0, NULL);
```

### Validate argument types

```sql
-- Keys must be strings, values can be any JSON type
```

## Examples

```sql
SELECT json_object('name', 'Alice', 'age');
-- Error: json_object() requires an even number of arguments
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
