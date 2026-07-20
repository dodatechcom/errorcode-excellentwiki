---
title: "[Solution] SQLite no such trigger"
description: "An SQL statement references a trigger that does not exist in the database."
tools: ["sqlite"]
error-types: ["schema-error"]
severities: ["error"]
---


# [Solution] SQLite no such trigger

SQLite raises **'no such trigger'** when an sql statement references a trigger that does not exist in the database. This is a common schema-related error that prevents the statement from executing.

## Common Causes

- The trigger was dropped or never created.
- A typo in the trigger name.
- The trigger is defined on a different table.

## How to Fix

### List all triggers

```sql
SELECT name FROM sqlite_master WHERE type='trigger';
```

### Recreate the trigger

```sql
CREATE TRIGGER audit_insert AFTER INSERT ON users
BEGIN
    INSERT INTO audit_log (op, rowid) VALUES ('INSERT', new.id);
END;
```

### Verify the trigger fires on the correct table

```sql
SELECT sql FROM sqlite_master WHERE type='trigger' AND name='audit_insert';
```

## Examples

```sql
SELECT * FROM sqlite_master WHERE type='trigger' AND name='nonexistent';
-- Returns empty result
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
