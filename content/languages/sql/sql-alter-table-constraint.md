---
title: "SQL ALTER TABLE Add Column Constraint Error"
description: "Fix SQL ALTER TABLE errors when adding columns with constraints that conflict with existing data."
languages: ["sql"]
error-types: ["syntax-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- Adding NOT NULL column without DEFAULT value on table with existing rows
- Adding UNIQUE constraint when duplicate values already exist
- Column name conflicts with existing column
- Adding foreign key to table with invalid references
- Using wrong data type for constraint (e.g., VARCHAR length too short)

## How to Fix

```sql
-- WRONG: NOT NULL without DEFAULT on populated table
ALTER TABLE users ADD COLUMN phone VARCHAR(20) NOT NULL;
-- ERROR: Table has existing rows

-- CORRECT: Add with DEFAULT first
ALTER TABLE users ADD COLUMN phone VARCHAR(20) DEFAULT '' NOT NULL;
-- or
ALTER TABLE users ADD COLUMN phone VARCHAR(20);
UPDATE users SET phone = '' WHERE phone IS NULL;
ALTER TABLE users ALTER COLUMN phone SET NOT NULL;
```

```sql
-- WRONG: UNIQUE constraint on data with duplicates
ALTER TABLE users ADD CONSTRAINT uq_email UNIQUE (email);
-- ERROR: Duplicate emails exist

-- CORRECT: Fix data first
UPDATE users SET email = CONCAT(email, '_dup')
WHERE id IN (
    SELECT id FROM (
        SELECT id, ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) AS rn
        FROM users
    ) t WHERE rn > 1
);
ALTER TABLE users ADD CONSTRAINT uq_email UNIQUE (email);
```

## Examples

```sql
-- Example 1: Add column safely
ALTER TABLE employees ADD COLUMN middle_name VARCHAR(50) NULL;

-- Example 2: Add column with default
ALTER TABLE products ADD COLUMN is_active BOOLEAN DEFAULT TRUE;

-- Example 3: Add foreign key constraint
ALTER TABLE orders ADD CONSTRAINT fk_customer
    FOREIGN KEY (customer_id) REFERENCES customers(id)
    ON DELETE SET NULL;
```

## Related Errors

- [Not null constraint error](not-null-constraint) -- NULL constraint violations
- [Foreign key error](foreign-key) -- FK constraint issues
