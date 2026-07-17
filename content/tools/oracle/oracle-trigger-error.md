---
title: "Oracle Trigger Error"
description: "Oracle trigger fails during execution."
tools: ["oracle"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# Oracle Trigger Error

An Oracle trigger error occurs when a database trigger fails during execution. Triggers are stored procedures that automatically execute in response to DML events.

## Common Causes

- Trigger body has PL/SQL errors
- Mutating table error (ORA-04091)
- Trigger references non-existent table
- Recursion depth exceeded

## How to Fix

### Check Trigger Status

```sql
SELECT trigger_name, status FROM user_triggers;
```

### Compile Trigger

```sql
ALTER TRIGGER mytrigger COMPILE;
```

### Fix Mutating Table Error

```sql
-- Instead of querying the same table in a row trigger,
-- use a compound trigger (11g+)
CREATE OR REPLACE TRIGGER my_trigger
FOR INSERT ON my_table
COMPOUND TRIGGER
  TYPE t_count IS TABLE OF NUMBER INDEX BY PLS_INTEGER;
  v_count t_count;
AFTER EACH ROW IS
BEGIN
  v_count(:NEW.id) := 1;
END AFTER EACH ROW;
AFTER STATEMENT IS
BEGIN
  NULL;
END AFTER STATEMENT;
END my_trigger;
```

### Check for Compilation Errors

```sql
SHOW ERRORS TRIGGER mytrigger;
```

### Disable/Enable Trigger

```sql
ALTER TRIGGER mytrigger DISABLE;
ALTER TRIGGER mytrigger ENABLE;
```

### Check Trigger Event

```sql
SELECT trigger_event, triggering_event
FROM user_triggers
WHERE trigger_name = 'MYTRIGGER';
```

## Examples

```sql
CREATE TRIGGER audit_trigger
BEFORE INSERT ON users
FOR EACH ROW
BEGIN
  :NEW.created_at := SYSDATE;
END;
/
-- ORA-04084: cannot change NEW values for this trigger type
```

## Related Errors

- [View Error]({{< relref "/tools/oracle/view-error" >}}) — view issues
- [Synonym Error]({{< relref "/tools/oracle/synonym-error" >}}) — synonym issues
