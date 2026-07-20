---
title: "[Solution] SQLite PRIMARY KEY constraint failed"
description: "An INSERT or UPDATE violated the PRIMARY KEY constraint by inserting a duplicate primary key value."
tools: ["sqlite"]
error-types: ["constraint-error"]
severities: ["error"]
---


# [Solution] SQLite PRIMARY KEY constraint failed

SQLite raises a **PRIMARY KEY constraint failed** error when an insert or update violated the primary key constraint by inserting a duplicate primary key value. This is one of the most common classes of errors encountered in SQLite databases.

## Common Causes

- Inserting a row with an ID that already exists.
- Manually specifying a primary key value that conflicts.
- Missing AUTOINCREMENT causing manual key management.

## How to Fix

### Use AUTOINCREMENT for automatic key generation

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
);
```

### Use INSERT OR REPLACE

```sql
INSERT OR REPLACE INTO users (id, name) VALUES (1, 'Alice');
```

### Let SQLite assign rowid automatically

```sql
INSERT INTO users (name) VALUES ('Alice');
-- id is assigned automatically
```

## Examples

```sql
INSERT INTO users (id, name) VALUES (1, 'Alice');
INSERT INTO users (id, name) VALUES (1, 'Bob');
-- Error: PRIMARY KEY constraint failed: users.id
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
