---
title: "[Solution] SQLite table already exists"
description: "A CREATE TABLE statement tries to create a table that already exists in the database."
tools: ["sqlite"]
error-types: ["schema-error"]
severities: ["error"]
---


# [Solution] SQLite table already exists

SQLite raises **'table already exists'** when a create table statement tries to create a table that already exists in the database. This is a common schema-related error that prevents the statement from executing.

## Common Causes

- The table was created by a previous operation.
- A migration script ran twice.
- Missing IF NOT EXISTS clause.

## How to Fix

### Use CREATE TABLE IF NOT EXISTS

```sql
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT
);
```

### Drop the table first if a fresh copy is needed

```sql
DROP TABLE IF EXISTS users;
CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT);
```

### Check what tables exist

```sql
SELECT name FROM sqlite_master WHERE type='table';
```

## Examples

```sql
CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT);
-- Error: table users already exists
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
