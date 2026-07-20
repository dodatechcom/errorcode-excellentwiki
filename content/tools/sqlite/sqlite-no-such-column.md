---
title: "[Solution] SQLite no such column"
description: "An SQL statement references a column that does not exist in the specified table."
tools: ["sqlite"]
error-types: ["schema-error"]
severities: ["error"]
---


# [Solution] SQLite no such column

SQLite raises **'no such column'** when an sql statement references a column that does not exist in the specified table. This is a common schema-related error that prevents the statement from executing.

## Common Causes

- The column was never added to the table.
- A typo in the column name.
- The table schema changed since the query was written.

## How to Fix

### Check the table's column definitions

```sql
PRAGMA table_info(users);
```

### Add the missing column

```sql
ALTER TABLE users ADD COLUMN phone TEXT;
```

### Use ALTER TABLE to rename if the column was renamed

```sql
ALTER TABLE users RENAME COLUMN old_name TO new_name;
```

## Examples

```sql
SELECT username FROM users;
-- Error: no such column: users.username
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
