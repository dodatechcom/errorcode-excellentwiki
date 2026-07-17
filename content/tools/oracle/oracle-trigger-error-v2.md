---
title: "Oracle - ORA-04091: table is mutating"
description: "Oracle trigger fails because it tries to query or modify the table that fired the trigger"
tools: ["oracle"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

ORA-04091: table is mutating occurs when a row-level trigger tries to read or modify the table that fired it. Oracle prevents this to avoid inconsistent reads during the trigger's execution.

## Common Causes

- Row-level trigger queries the same table
- Trigger tries to INSERT/UPDATE/DELETE the firing table
- Constraint validation queries the same table
- Compound triggers not used for cross-row operations
- Trying to enforce a running total or aggregate

## How to Fix

1. Use compound triggers (Oracle 11g+):

```sql
CREATE OR REPLACE TRIGGER emp_salary_check
FOR INSERT OR UPDATE ON employees
COMPOUND TRIGGER
  TYPE salary_rec IS RECORD (
    emp_id NUMBER,
    new_salary NUMBER
  );
  TYPE salary_list IS TABLE OF salary_rec;
  pending_changes salary_list := salary_list();

  AFTER EACH ROW IS
  BEGIN
    pending_changes.EXTEND;
    pending_changes(pending_changes.LAST).emp_id := :NEW.employee_id;
    pending_changes(pending_changes.LAST).new_salary := :NEW.salary;
  END AFTER EACH ROW;

  AFTER STATEMENT IS
  BEGIN
    FOR i IN 1 .. pending_changes.COUNT LOOP
      -- Safe to query table here (statement-level)
      NULL;
    END LOOP;
    pending_changes.DELETE;
  END AFTER STATEMENT;
END emp_salary_check;
```

2. Use a temporary table or PL/SQL collection to store values:

```sql
CREATE GLOBAL TEMPORARY TABLE temp_salary_check (
  emp_id NUMBER,
  new_salary NUMBER
) ON COMMIT DELETE ROWS;

CREATE OR REPLACE TRIGGER check_salary
AFTER INSERT OR UPDATE ON employees
FOR EACH ROW
BEGIN
  INSERT INTO temp_salary_check VALUES (:NEW.employee_id, :NEW.salary);
END;
```

3. Use autonomous transaction for isolated operations:

```sql
CREATE OR REPLACE PROCEDURE log_salary_change(
  p_emp_id NUMBER, p_new_salary NUMBER
) AS
  PRAGMA AUTONOMOUS_TRANSACTION;
BEGIN
  INSERT INTO salary_audit (emp_id, salary, changed_at)
  VALUES (p_emp_id, p_new_salary, SYSDATE);
  COMMIT;
END;
```

4. Move validation to application level instead of trigger.

## Examples

```sql
-- Error: ORA-04091: table EMPLOYEES is mutating
CREATE OR REPLACE TRIGGER check_emp_count
AFTER INSERT ON employees
FOR EACH ROW
BEGIN
  IF (SELECT COUNT(*) FROM employees) > 100 THEN
    RAISE_APPLICATION_ERROR(-20001, 'Too many employees');
  END IF;
END;

-- Fix: use compound trigger or statement-level check
CREATE OR REPLACE TRIGGER check_emp_count
FOR INSERT ON employees
COMPOUND TRIGGER
  AFTER STATEMENT IS
  BEGIN
    IF (SELECT COUNT(*) FROM employees) > 100 THEN
      RAISE_APPLICATION_ERROR(-20001, 'Too many employees');
    END IF;
  END AFTER STATEMENT;
END;
```

## Related Errors

- [Lock error]({{< relref "/tools/oracle/oracle-lock-error" >}})
- [Sequence error]({{< relref "/tools/oracle/oracle-sequence-error" >}})
