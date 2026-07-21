---
title: "[Solution] PostgreSQL Enum Value Error"
description: "Fix PostgreSQL enum type value errors. Resolve invalid or duplicate enum value insertion issues."
tools: ["postgresql"]
error-types: ["tool-error"]
severities: ["error"]
---

# PostgreSQL Enum Value Error

ERROR: invalid input value for enum / duplicate enum value

This error occurs when inserting a value into an enum column that does not match any defined enum label, or when trying to add a duplicate label.

## Common Causes

- The inserted string does not match any existing enum label
- Attempting to add a label that already exists
- Case sensitivity mismatch between inserted value and enum label
- Code deploying new enum values without running the migration

## How to Fix

1. Check existing enum values:

```sql
SELECT enum_range(NULL::order_status);
```

2. Add a new enum value without locking the table:

```sql
ALTER TYPE order_status ADD VALUE IF NOT EXISTS 'pending_review' BEFORE 'approved';
```

3. Insert data matching exact enum label casing:

```sql
-- If enum label is 'pending_review' (lowercase)
INSERT INTO orders (status) VALUES ('pending_review');

-- This will fail
INSERT INTO orders (status) VALUES ('Pending_Review');
```

## Examples

```bash
# List all enum types and their values in the database
psql -d mydb -c "
SELECT t.typname, e.enumlabel
FROM pg_type t
JOIN pg_enum e ON t.oid = e.enumtypid
ORDER BY t.typname, e.enumsortorder;"
```
