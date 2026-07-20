---
title: "[Solution] SQLite no such table"
description: "An SQL statement references a table that does not exist in the current database schema."
tools: ["sqlite"]
error-types: ["schema-error"]
severities: ["error"]
---


# [Solution] SQLite no such table

SQLite raises **'no such table'** when an sql statement references a table that does not exist in the current database schema. This is a common schema-related error that prevents the statement from executing.

## Common Causes

- The table was never created.
- A typo in the table name.
- The table exists in a different attached database.

## How to Fix

### List all tables in the database

```sql
SELECT name FROM sqlite_master WHERE type='table';
```

### Check the correct database name for attached databases

```sql
SELECT * FROM attached_db.my_table;
```

### Verify the table name is spelled correctly

```sql
SELECT sql FROM sqlite_master WHERE name='users';
```

## Examples

```sql
SELECT * FROM userss;
-- Error: no such table: userss
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
