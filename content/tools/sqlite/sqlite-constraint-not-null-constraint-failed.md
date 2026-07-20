---
title: "[Solution] SQLite NOT NULL constraint failed"
description: "A NOT NULL column received a NULL value during INSERT or UPDATE."
tools: ["sqlite"]
error-types: ["constraint-error"]
severities: ["error"]
---


# [Solution] SQLite NOT NULL constraint failed

SQLite raises a **NOT NULL constraint failed** error when a not null column received a null value during insert or update. This is one of the most common classes of errors encountered in SQLite databases.

## Common Causes

- Attempting to insert NULL into a column defined as NOT NULL.
- A trigger sets a column to NULL violating the constraint.
- DEFAULT value expression evaluates to NULL when it should not.

## How to Fix

### Ensure the column receives a valid non-NULL value

```sql
INSERT INTO users (id, name) VALUES (1, 'Alice');
-- 'name' must not be NULL
```

### Use a DEFAULT value in the table definition

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL DEFAULT 'Unknown'
);
```

### Add a CHECK constraint as a safety net

```sql
ALTER TABLE users ADD CONSTRAINT chk_name CHECK (name IS NOT NULL);
```

## Examples

```sql
INSERT INTO users (id, name) VALUES (1, NULL);
-- Error: NOT NULL constraint failed: users.name
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
