---
title: "[Solution] SQL Trigger Error Fix"
description: "Fix 'Trigger X doesn't exist' or trigger execution errors in MySQL."
languages: ["sql"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["trigger", "before-insert", "after-update", "event", "dml"]
weight: 5
---

This error occurs when a SQL trigger cannot be found or fails during execution. The message reads: `Trigger 'X' doesn't exist` or `Can't create or update trigger in stored function`.

## What This Error Means

Triggers are stored programs that execute automatically when a table is modified. They can fail if the trigger doesn't exist, has syntax errors, or tries to perform disallowed operations.

## Common Causes

- Trigger was dropped or never created
- Trigger name misspelled
- Trigger tries to update the same table that fired it (MySQL restriction)
- Trigger contains a stored function call that modifies data

## How to Fix

### Fix 1: Verify trigger exists

```sql
SHOW TRIGGERS WHERE `table` = 'orders';
-- or
SELECT trigger_name, event_manipulation, event_object_table
FROM information_schema.triggers
WHERE trigger_schema = DATABASE();
```

### Fix 2: Create the trigger if missing

```sql
CREATE TRIGGER before_order_insert
BEFORE INSERT ON orders
FOR EACH ROW
BEGIN
    SET NEW.created_at = NOW();
    SET NEW.status = 'pending';
END;
```

### Fix 3: Avoid updating the same table in trigger

```sql
-- Wrong: triggers cannot modify the firing table
CREATE TRIGGER before_update
BEFORE UPDATE ON orders
FOR EACH ROW
BEGIN
    UPDATE orders SET updated_at = NOW() WHERE id = NEW.id;
    -- ERROR: Can't update table 'orders' in stored function/trigger
END;

-- Correct: use SET on NEW
CREATE TRIGGER before_update
BEFORE UPDATE ON orders
FOR EACH ROW
BEGIN
    SET NEW.updated_at = NOW();
END;
```

## Examples

```sql
DROP TRIGGER IF EXISTS old_trigger;
-- Then recreate if needed
CREATE TRIGGER new_trigger AFTER INSERT ON users
FOR EACH ROW INSERT INTO audit_log (user_id, action) VALUES (NEW.id, 'created');
```

## Related Errors

- [Stored Procedure Error](stored-procedure.md) — related programmatic SQL
- [View Error](view-error.md) — dependent object issue
