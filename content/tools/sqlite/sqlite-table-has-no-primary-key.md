---
title: "[Solution] SQLite table has no primary key"
description: "An operation requires a PRIMARY KEY but the table does not have one defined."
tools: ["sqlite"]
error-types: ["schema-error"]
severities: ["error"]
---


# [Solution] SQLite table has no primary key

SQLite raises **'table has no primary key'** when an operation requires a primary key but the table does not have one defined. This is a common schema-related error that prevents the statement from executing.

## Common Causes

- The table was created without a PRIMARY KEY.
- The PRIMARY KEY was defined inline and missed.
- ROWID tables were expected to behave like INTEGER PRIMARY KEY.

## How to Fix

### Add a primary key to the table

```sql
ALTER TABLE users ADD COLUMN id INTEGER PRIMARY KEY;
```

### Check the current table structure

```sql
PRAGMA table_info(users);
```

### Use the hidden rowid as a de facto primary key

```sql
SELECT rowid FROM users;
```

## Examples

```sql
CREATE TABLE users (name TEXT);
PRAGMA table_info(users);
-- 'pk' column is 0 for all columns — no primary key
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
