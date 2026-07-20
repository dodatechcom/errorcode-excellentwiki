---
title: "[Solution] SQLite view already exists"
description: "A CREATE VIEW statement tries to create a view that already exists in the database."
tools: ["sqlite"]
error-types: ["schema-error"]
severities: ["error"]
---


# [Solution] SQLite view already exists

SQLite raises **'view already exists'** when a create view statement tries to create a view that already exists in the database. This is a common schema-related error that prevents the statement from executing.

## Common Causes

- The view was created by a previous operation.
- A migration script ran twice.
- Missing IF NOT EXISTS clause.

## How to Fix

### Use CREATE VIEW IF NOT EXISTS

```sql
CREATE VIEW IF NOT EXISTS active_users AS SELECT * FROM users WHERE active = 1;
```

### Drop and recreate the view

```sql
DROP VIEW IF EXISTS active_users;
CREATE VIEW active_users AS SELECT * FROM users WHERE active = 1;
```

### Check existing views

```sql
SELECT name FROM sqlite_master WHERE type='view';
```

## Examples

```sql
CREATE VIEW active_users AS SELECT * FROM users WHERE active = 1;
CREATE VIEW active_users AS SELECT * FROM users WHERE active = 1;
-- Error: view active_users already exists
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
