---
title: "[Solution] SQLite json_group_array() error"
description: "The json_group_array() aggregate function received an invalid argument or context."
tools: ["sqlite"]
error-types: ["query-error"]
severities: ["error"]
---


# [Solution] SQLite json_group_array() error

SQLite JSON1 extension produces **json_group_array() error** when the json_group_array() aggregate function received an invalid argument or context. The JSON1 extension provides powerful JSON manipulation functions for SQLite.

## Common Causes

- The function is used outside an aggregate context.
- The input values are not valid JSON.
- The function is nested incorrectly.

## How to Fix

### Use json_group_array() with GROUP BY

```sql
SELECT dept, json_group_array(name) AS members
FROM employees
GROUP BY dept;
```

### Ensure input values are valid JSON

```sql
SELECT json_group_array(json_object('id', id, 'name', name))
FROM employees;
```

### Use json_group_object() for key-value aggregation

```sql
SELECT json_group_object(id, name) FROM employees;
```

## Examples

```sql
SELECT json_group_array(name) FROM employees;
-- Error: misuse of aggregate function json_group_array()
-- Must have GROUP BY or use in aggregate context
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
