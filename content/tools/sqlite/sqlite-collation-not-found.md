---
title: "[Solution] SQLite collation not found"
description: "An SQL statement references a collation sequence that does not exist."
tools: ["sqlite"]
error-types: ["query-error"]
severities: ["error"]
---


# [Solution] SQLite collation not found

SQLite produces **collation not found** when an sql statement references a collation sequence that does not exist. This error can occur in various contexts and requires understanding the specific trigger.

## Common Causes

- The collation was defined in a different connection.
- A custom collation was not registered.
- A typo in the collation name.

## How to Fix

### Use a built-in collation

```sql
-- Built-in: BINARY, NOCASE, RTRIM
SELECT * FROM users ORDER BY name COLLATE NOCASE;
```

### Register a custom collation in the application

```python
conn.create_collation('MY_COLLATE', lambda a, b: (a > b) - (a < b))
```

### Check available collations

```sql
SELECT * FROM pragma_collation_list;
```

## Examples

```sql
SELECT * FROM users ORDER BY name COLLATE MY_CUSTOM;
-- Error: no such collation sequence: MY_CUSTOM
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
