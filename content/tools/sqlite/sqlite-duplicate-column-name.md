---
title: "[Solution] SQLite duplicate column name"
description: "An ALTER TABLE or CREATE TABLE statement tries to add a column that already exists."
tools: ["sqlite"]
error-types: ["schema-error"]
severities: ["error"]
---


# [Solution] SQLite duplicate column name

SQLite raises **'duplicate column name'** when an alter table or create table statement tries to add a column that already exists. This is a common schema-related error that prevents the statement from executing.

## Common Causes

- The column already exists in the table.
- A migration script ran twice.
- A CREATE TABLE statement specifies the same column name twice.

## How to Fix

### Check existing columns first

```sql
PRAGMA table_info(users);
```

### Skip adding the column if it already exists

```sql
-- Only run if column does not exist:
ALTER TABLE users ADD COLUMN phone TEXT;
```

### Use a migration framework to track applied changes

```bash
# Record each migration step to avoid duplicate runs
```

## Examples

```sql
ALTER TABLE users ADD COLUMN email TEXT;
ALTER TABLE users ADD COLUMN email TEXT;
-- Error: duplicate column name: email
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
