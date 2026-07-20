---
title: "[Solution] SQLite no such view"
description: "An SQL statement references a view that does not exist in the current database."
tools: ["sqlite"]
error-types: ["schema-error"]
severities: ["error"]
---


# [Solution] SQLite no such view

SQLite raises **'no such view'** when an sql statement references a view that does not exist in the current database. This is a common schema-related error that prevents the statement from executing.

## Common Causes

- The view was dropped or never created.
- A typo in the view name.
- The view exists in a different attached database.

## How to Fix

### List all views

```sql
SELECT name FROM sqlite_master WHERE type='view';
```

### Recreate the view

```sql
CREATE VIEW active_users AS SELECT * FROM users WHERE active = 1;
```

### Check the view's underlying query

```sql
SELECT sql FROM sqlite_master WHERE type='view' AND name='active_users';
```

## Examples

```sql
SELECT * FROM active_users_v2;
-- Error: no such view: active_users_v2
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
