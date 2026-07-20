---
title: "[Solution] SQLite schema changed since last read"
description: "A prepared statement is still active while the schema of a table it references was modified."
tools: ["sqlite"]
error-types: ["schema-error"]
severities: ["error"]
---


# [Solution] SQLite schema changed since last read

SQLite raises **'schema changed since last read'** when a prepared statement is still active while the schema of a table it references was modified. This is a common schema-related error that prevents the statement from executing.

## Common Causes

- Another connection modified the schema while a query was pending.
- An ALTER TABLE was executed in the same connection while stepping through results.
- A trigger modified the schema during execution.

## How to Fix

### Re-prepare the statement after schema changes

```sql
-- Re-prepare and re-execute after DDL changes
```

### Use sqlite3_reset() before re-executing

```python
cursor.execute("SELECT * FROM users")
# schema changes here
cursor.execute("SELECT * FROM users")  # auto-reset and re-prepare
```

### Avoid schema changes while queries are active

```sql
-- Complete all SELECT operations before running ALTER TABLE
```

## Examples

```sql
-- Connection A: prepares a statement
PREPARE stmt AS SELECT * FROM users;
-- Connection B: alters the table
ALTER TABLE users ADD COLUMN age INT;
-- Connection A: tries to step — SQLITE_SCHEMA (17)
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
