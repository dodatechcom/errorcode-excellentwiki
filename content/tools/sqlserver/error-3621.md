---
title: "[Solution] SQL Server Error 3621: The Statement Has Been Terminated"
description: "Fix SQL Server Error 3621 statement terminated errors. Understand cascading terminations from constraint violations."
tools: ["sqlserver"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Error 3621: The Statement Has Been Terminated

Error 3621 is a follow-up error that occurs after a constraint violation (like error 547 or 8152). SQL Server terminates the entire statement because it cannot complete the operation that violated the constraint.

## Common Causes

- A CHECK constraint was violated (follows error 547)
- String data would be truncated (follows error 8152)
- A NOT NULL constraint was violated
- A foreign key constraint was violated (follows error 547)

## How to Fix

### Look at the Preceding Error

```
-- Error 3621 is ALWAYS preceded by another error
-- Fix the root cause error, not error 3621 itself

-- Example sequence:
-- Msg 547: CHECK constraint violated
-- Msg 3621: The statement has been terminated
```

### Fix the Constraint Violation

```sql
-- If CHECK constraint failed (error 547):
SELECT name, definition
FROM sys.check_constraints
WHERE parent_object_id = OBJECT_ID('your_table');

-- Fix the data to satisfy the constraint
```

### Fix Truncation Issues

```sql
-- If string truncation (error 8152):
-- Widen the column
ALTER TABLE your_table ALTER COLUMN name VARCHAR(255);
```

### Fix NULL Constraint Violations

```sql
-- If NOT NULL constraint violated:
-- Provide a value or set a default
ALTER TABLE your_table ADD CONSTRAINT DF_name DEFAULT '' FOR name;
```

### Use TRY/CATCH for Graceful Handling

```sql
BEGIN TRY
    INSERT INTO users (name, email) VALUES ('Alice', 'invalid');
END TRY
BEGIN CATCH
    PRINT ERROR_MESSAGE();  -- Shows root cause, not just error 3621
END CATCH
```

## Examples

```sql
-- CHECK constraint failure
ALTER TABLE orders ADD CONSTRAINT CK_amount CHECK (amount > 0);
INSERT INTO orders (amount) VALUES (-10);
-- Msg 547: The INSERT statement conflicted with the CHECK constraint "CK_amount"
-- Msg 3621: The statement has been terminated
-- Fix: check the amount value satisfies the constraint

-- NOT NULL without default
INSERT INTO users (id) VALUES (1);
-- Msg 515: Cannot insert the value NULL into column 'name'
-- Msg 3621: The statement has been terminated
-- Fix: provide value for 'name' or add DEFAULT constraint
```

## Related Errors

- [Error 547]({{< relref "/tools/sqlserver/error-547" >}}) — CHECK constraint failed (root cause)
- [Error 8152]({{< relref "/tools/sqlserver/error-8152" >}}) — string truncation (root cause)
- [Error 1205]({{< relref "/tools/sqlserver/error-1205" >}}) — deadlock victim
