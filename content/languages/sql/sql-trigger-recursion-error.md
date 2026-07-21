---
title: "SQL TRIGGER Recursive Trigger Error"
description: "Fix SQL TRIGGER recursive trigger errors when triggers fire themselves creating infinite recursion loops."
languages: ["sql"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- UPDATE trigger on a table that updates the same table
- INSERT trigger that inserts into the same table
- Missing recursion guard condition in trigger
- Server setting allows recursive triggers when not intended
- Trigger updates a column that fires another trigger on same table

## How to Fix

```sql
-- WRONG: Trigger updates same table (infinite recursion)
CREATE TRIGGER trg_audit
AFTER UPDATE ON employees
FOR EACH ROW
BEGIN
    INSERT INTO employees (name, audit_flag)
    VALUES (NEW.name, 'updated');
    -- This INSERT fires trg_audit again!
END;

-- CORRECT: Use recursion guard
CREATE TRIGGER trg_audit
AFTER UPDATE ON employees
FOR EACH ROW
BEGIN
    IF NEW.audit_flag IS NULL THEN  -- guard condition
        INSERT INTO audit_log (emp_id, changed_at)
        VALUES (NEW.id, NOW());
    END IF;
END;
```

```sql
-- WRONG: SQL Server recursive trigger
ALTER DATABASE mydb SET RECURSIVE_TRIGGERS ON;
-- Trigger fires itself

-- CORRECT: Disable recursive triggers
ALTER DATABASE mydb SET RECURSIVE_TRIGGERS OFF;
-- or add TRIGGER_NESTLEVEL() check
```

## Examples

```sql
-- Example 1: MySQL recursion guard
DELIMITER //
CREATE TRIGGER trg_update_timestamp
BEFORE UPDATE ON orders
FOR EACH ROW
BEGIN
    IF OLD.updated_at = NEW.updated_at THEN
        SET NEW.updated_at = NOW();
    END IF;
END //
DELIMITER ;

-- Example 2: PostgreSQL using pg_trigger_depth()
CREATE OR REPLACE FUNCTION audit_func()
RETURNS TRIGGER AS $$
BEGIN
    IF pg_trigger_depth() = 1 THEN
        INSERT INTO audit(table_name, action, row_id)
        VALUES (TG_TABLE_NAME, TG_OP, NEW.id);
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Example 3: SQL Server using TRIGGER_NESTLEVEL()
CREATE TRIGGER trg_safe_update
ON employees
AFTER UPDATE
AS
BEGIN
    IF TRIGGER_NESTLEVEL() <= 1
        INSERT INTO audit_log SELECT * FROM inserted;
END;
```

## Related Errors

- [Trigger error](sql-trigger-error) -- trigger definition issues
- [Deadlock error](deadlock) -- trigger-related deadlocks
