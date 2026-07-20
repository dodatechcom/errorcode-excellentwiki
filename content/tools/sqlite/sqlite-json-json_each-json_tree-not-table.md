---
title: "[Solution] SQLite json_each()/json_tree() not table"
description: "The json_each() or json_tree() function is used in a context that does not return a table."
tools: ["sqlite"]
error-types: ["query-error"]
severities: ["error"]
---


# [Solution] SQLite json_each()/json_tree() not table

SQLite JSON1 extension produces **json_each()/json_tree() not table** when the json_each() or json_tree() function is used in a context that does not return a table. The JSON1 extension provides powerful JSON manipulation functions for SQLite.

## Common Causes

- The function is not used in a FROM clause.
- The input is not valid JSON.
- The path argument is incorrect.

## How to Fix

### Use json_each() in a FROM clause

```sql
SELECT * FROM json_each('[1,2,3]');
```

### Use json_tree() for recursive traversal

```sql
SELECT * FROM json_tree('{"a": {"b": 1}}');
```

### Provide valid JSON input

```sql
SELECT * FROM json_each('{"a": 1, "b": 2}');
```

## Examples

```sql
SELECT json_each('[1,2,3]');
-- Error: json_each() can only be used in the FROM clause of a SELECT
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
