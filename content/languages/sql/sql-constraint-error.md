---
title: "[Solution] SQL CHECK Constraint Violation Error Fix"
description: "Fix 'CHECK constraint violation' in SQL. Resolve data validation errors by understanding and correcting constraint rules."
languages: ["sql"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# SQL CHECK Constraint Violation Error Fix

The `CHECK constraint violation` error occurs when an INSERT or UPDATE operation provides data that fails a CHECK constraint's validation rule.

## What This Error Means

CHECK constraints enforce data integrity by validating that column values meet specific conditions. When you try to insert or update data that violates the condition, the database rejects the operation.

A typical error:

```
ERROR: new row violates check constraint "employees_salary_check"
DETAIL: Failing row contains (1, John, -5000)
```

## Why It Happens

Common causes include:

- **Negative values where positives required** — Salary or price columns with CHECK >= 0.
- **Values outside allowed range** — Age between 0 and 150, percentage 0-100.
- **Invalid format** — Email format or phone number patterns.
- **NULL values in NOT NULL + CHECK** — Some databases treat CHECK differently with NULL.
- **Bulk insert with bad data** — Staging table contains invalid values.

## How to Fix It

### Fix 1: Check constraint definition

```sql
-- Find the constraint
SELECT conname, pg_get_constraintdef(oid)
FROM pg_constraint
WHERE conname LIKE '%salary%';

-- MySQL
SELECT CHECK_clause 
FROM information_schema.CHECK_CONSTRAINTS 
WHERE CONSTRAINT_NAME = 'employees_salary_check';
```

### Fix 2: Fix the data before inserting

```sql
-- WRONG: Negative salary violates CHECK
INSERT INTO employees (name, salary) VALUES ('John', -5000);

-- RIGHT: Ensure data meets constraints
INSERT INTO employees (name, salary) VALUES ('John', 50000);
```

### Fix 3: Modify constraint if needed

```sql
-- RIGHT: Drop and recreate with new rule
ALTER TABLE employees DROP CONSTRAINT employees_salary_check;
ALTER TABLE employees ADD CONSTRAINT employees_salary_check 
    CHECK (salary >= 0 AND salary <= 1000000);
```

### Fix 4: Disable constraints temporarily for bulk loads

```sql
-- RIGHT: Disable for bulk operations
ALTER TABLE employees DISABLE CHECK CONSTRAINT employees_salary_check;

-- Perform bulk insert
INSERT INTO employees SELECT * FROM staging_employees;

-- Re-enable
ALTER TABLE employees ENABLE CHECK CONSTRAINT employees_salary_check;
```

### Fix 5: Use INSERT with ON CONFLICT

```sql
-- RIGHT: Handle constraint violations gracefully
INSERT INTO employees (name, salary)
VALUES ('John', 50000)
ON CONFLICT DO NOTHING;

-- Or update on conflict
INSERT INTO products (name, price)
VALUES ('Widget', 9.99)
ON CONFLICT (name) 
DO UPDATE SET price = EXCLUDED.price;
```

## Common Mistakes

- **Not checking constraint before INSERT** — Query the constraint definition first.
- **Assuming CHECK allows NULL** — NULL values bypass CHECK in some databases.
- **Forgetting composite CHECK constraints** — Multiple columns may be validated together.

## Related Pages

- [SQL Constraint Error](sql-constraint-error) — General constraint issues
- [SQL Index Error](sql-index-error) — Index creation issues
- [SQL Identity Error](sql-identity-error) — Identity column issues
