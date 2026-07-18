---
title: "[Solution] SQL Trigger Execution Error Fix"
description: "Fix 'trigger execution error' in SQL. Resolve trigger firing issues, recursive triggers, and mutating table errors."
languages: ["sql"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# SQL Trigger Execution Error Fix

The `trigger execution error` occurs when a trigger fails during its execution, causing the entire transaction to fail. This includes recursive trigger issues, mutating table errors, and logic failures.

## What This Error Means

Triggers are stored procedures that automatically fire on table events (INSERT, UPDATE, DELETE). When a trigger contains errors, violates constraints, or references tables that are being modified, the trigger fails and rolls back the operation.

A typical error:

```
ORA-04091: table HR.EMPLOYEES is mutating, trigger/function may not see it
```

Or:

```
ERROR: trigger execution failed
```

## Why It Happens

Common causes include:

- **Mutating table reference** — Trigger reads from the same table being modified.
- **Recursive triggers** — Trigger causes another trigger to fire in a loop.
- **Constraint violations** — Trigger inserts data violating constraints.
- **Missing exception handling** — Unhandled errors in trigger code.
- **Deadlock** — Multiple triggers lock each other.

## How to Fix It

### Fix 1: Avoid mutating table references

```sql
-- WRONG: Reading from same table in row-level trigger
CREATE TRIGGER check_salary
AFTER UPDATE ON employees
FOR EACH ROW
BEGIN
    SELECT AVG(salary) INTO avg_sal FROM employees;
END;

-- RIGHT: Use statement-level trigger or temp table
CREATE TRIGGER check_salary
AFTER UPDATE ON employees
FOR EACH STATEMENT
BEGIN
    -- Statement-level trigger can read the table
    PERFORM audit_log();
END;
```

### Fix 2: Add exception handling

```sql
-- RIGHT: Wrap trigger code in exception handler
CREATE OR REPLACE FUNCTION audit_changes()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO audit_log (table_name, record_id, changed_at)
    VALUES (TG_TABLE_NAME, NEW.id, NOW());
    RETURN NEW;
EXCEPTION WHEN OTHERS THEN
    RAISE WARNING 'Audit failed: %', SQLERRM;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```

### Fix 3: Prevent recursive triggers

```sql
-- RIGHT: Disable recursive trigger temporarily
CREATE TRIGGER prevent_recursive
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    -- Use session variable to prevent recursion
    IF current_setting('app.trigger_active', true) IS DISTINCT FROM '1' THEN
        PERFORM set_config('app.trigger_active', '1', true);
        -- Do work here
        PERFORM set_config('app.trigger_active', '0', true);
    END IF;
END;
```

### Fix 4: Use AFTER triggers for read consistency

```sql
-- RIGHT: AFTER trigger sees committed data
CREATE TRIGGER update_summary
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE customer_summary
    SET total_orders = total_orders + 1,
        total_amount = total_amount + NEW.amount
    WHERE customer_id = NEW.customer_id;
END;
```

### Fix 5: Disable triggers temporarily

```sql
-- RIGHT: Disable during bulk operations
ALTER TABLE employees DISABLE TRIGGER ALL;

-- Perform bulk insert
INSERT INTO employees SELECT * FROM staging_employees;

-- Re-enable triggers
ALTER TABLE employees ENABLE TRIGGER ALL;
```

## Common Mistakes

- **Not handling NULL values in triggers** — NEW or OLD values can be NULL.
- **Using BEFORE triggers for reads** — BEFORE triggers should not read other tables.
- **Forgetting to return NEW or OLD** — Triggers must return the correct row value.

## Related Pages

- [SQL Procedure Error](sql-procedure-error) — Stored procedure issues
- [SQL Constraint Error](sql-constraint-error) — Constraint violations
- [SQL Savepoint Error](sql-savepoint-error) — Transaction savepoint issues
