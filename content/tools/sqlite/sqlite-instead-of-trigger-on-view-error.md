---
title: "[Solution] SQLite INSTEAD OF trigger on view error"
description: "An INSTEAD OF trigger fired on a view but the trigger body has an error."
tools: ["sqlite"]
error-types: ["query-error"]
severities: ["error"]
---


# [Solution] SQLite INSTEAD OF trigger on view error

SQLite produces **INSTEAD OF trigger on view error** when an instead of trigger fired on a view but the trigger body has an error. This error can occur in various contexts and requires understanding the specific trigger.

## Common Causes

- The INSTEAD OF trigger does not handle the operation correctly.
- The trigger tries to modify a read-only view.
- The trigger body references invalid columns.

## How to Fix

### Create proper INSTEAD OF triggers for views

```sql
CREATE TRIGGER insert_users INSTEAD OF INSERT ON user_view
BEGIN
    INSERT INTO users (id, name) VALUES (new.id, new.name);
END;
```

### Handle INSERT, UPDATE, and DELETE operations

```sql
CREATE TRIGGER delete_users INSTEAD OF DELETE ON user_view
BEGIN
    DELETE FROM users WHERE id = old.id;
END;
```

### Verify the trigger references valid columns

```sql
-- Use new.* for INSERT/UPDATE, old.* for UPDATE/DELETE
```

## Examples

```sql
CREATE VIEW user_view AS SELECT id, name FROM users;
-- Without an INSTEAD OF trigger, INSERT into user_view fails
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
