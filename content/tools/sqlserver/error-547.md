---
title: "[Solution] SQL Server Error 547: CHECK Constraint Failed"
description: "Fix SQL Server Error 547 CHECK constraint violations. Resolve data validation failures."
tools: ["sqlserver"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Error 547: CHECK Constraint Failed

Error 547 occurs when an INSERT or UPDATE violates a CHECK constraint defined on the table. The data value does not satisfy the constraint's validation rule.

## Common Causes

- The inserted value falls outside the allowed range
- The value does not match the required pattern or format
- A NULL value is inserted into a column with a CHECK constraint that excludes NULLs
- The constraint was added after existing data was already inconsistent

## How to Fix

### Identify the Constraint

```sql
-- Find CHECK constraints on the table
SELECT name, definition
FROM sys.check_constraints
WHERE parent_object_id = OBJECT_ID('your_table');
```

### View Constraint Definition

```sql
EXEC sp_helpconstraint 'your_table';
```

### Check Data Before Insert

```sql
-- See what values currently exist
SELECT DISTINCT column_name FROM your_table;
-- Verify the new value matches the constraint rules
```

### Modify the Constraint

```sql
-- Drop existing constraint
ALTER TABLE your_table DROP CONSTRAINT CK_column_range;

-- Add updated constraint
ALTER TABLE your_table
ADD CONSTRAINT CK_column_range CHECK (column_name >= 0 AND column_name <= 100);
```

### Temporarily Disable Constraint (Use Cautiously)

```sql
ALTER TABLE your_table NOCHECK CONSTRAINT CK_column_range;
-- Fix the data
-- Re-enable
ALTER TABLE your_table CHECK CONSTRAINT CK_column_range;
```

## Examples

```sql
-- Age range constraint
ALTER TABLE users ADD CONSTRAINT CK_age CHECK (age >= 0 AND age <= 150);
INSERT INTO users (name, age) VALUES ('Alice', 200);
-- Error 547: The INSERT statement conflicted with the CHECK constraint "CK_age"

-- Status constraint
ALTER TABLE orders ADD CONSTRAINT CK_status CHECK (status IN ('pending', 'shipped', 'delivered'));
INSERT INTO orders (status) VALUES ('unknown');
-- Error 547: CHECK constraint violated
```

## Related Errors

- [Error 8152]({{< relref "/tools/sqlserver/error-8152" >}}) — string data truncation
- [Error 1205]({{< relref "/tools/sqlserver/error-1205" >}}) — deadlock victim
