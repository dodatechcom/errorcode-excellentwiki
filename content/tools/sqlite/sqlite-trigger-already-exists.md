---
title: "[Solution] SQLite trigger already exists"
description: "A CREATE TRIGGER statement tries to create a trigger that already exists."
tools: ["sqlite"]
error-types: ["schema-error"]
severities: ["error"]
---


# [Solution] SQLite trigger already exists

SQLite raises **'trigger already exists'** when a create trigger statement tries to create a trigger that already exists. This is a common schema-related error that prevents the statement from executing.

## Common Causes

- The trigger was created by a previous operation.
- A migration script ran twice.
- Missing IF NOT EXISTS clause.

## How to Fix

### Use CREATE TRIGGER IF NOT EXISTS

```sql
CREATE TRIGGER IF NOT EXISTS audit_insert
AFTER INSERT ON users
BEGIN
    INSERT INTO audit_log (op) VALUES ('INSERT');
END;
```

### Drop and recreate the trigger

```sql
DROP TRIGGER IF EXISTS audit_insert;
CREATE TRIGGER audit_insert AFTER INSERT ON users
BEGIN
    INSERT INTO audit_log (op) VALUES ('INSERT');
END;
```

### List existing triggers

```sql
SELECT name FROM sqlite_master WHERE type='trigger';
```

## Examples

```sql
CREATE TRIGGER audit_insert AFTER INSERT ON users BEGIN SELECT 1; END;
CREATE TRIGGER audit_insert AFTER INSERT ON users BEGIN SELECT 1; END;
-- Error: trigger audit_insert already exists
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
