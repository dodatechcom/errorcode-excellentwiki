---
title: "[Solution] PostgreSQL Null Value Violates Not-Null Constraint - Fix Column Errors"
description: "Fix PostgreSQL null value in column violates not-null constraint by adding default values, fixing application logic, and using proper INSERT patterns"
tools: ["postgresql"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# PostgreSQL Null Value Violates Not-Null Constraint

This error occurs when an `INSERT` or `UPDATE` statement attempts to set a column to `NULL` when the column has a `NOT NULL` constraint. PostgreSQL enforces this constraint at the row level and rejects any operation that would violate it.

## What This Error Means

PostgreSQL returns this error when a `NOT NULL` constraint is violated:

```
ERROR: null value in column "email" violates not-null constraint
DETAIL: Failing row contains (1, null, ...).
```

The error message identifies the column name, the constraint type, and the full row data that was rejected. `NOT NULL` constraints can be defined inline in a `CREATE TABLE` statement, added later via `ALTER TABLE`, or implicitly created by a `PRIMARY KEY` constraint.

## Why It Happens

- The application does not provide a value for a required column
- A `DEFAULT` expression is missing and no value is supplied
- An `INSERT` statement omits a column that has no default
- A `SET` clause in an `UPDATE` statement references a variable that evaluates to `NULL`
- A trigger that is supposed to fill in a value fails silently
- The column was altered to add `NOT NULL` after existing rows contained `NULL` values
- Bulk import data has `NULL` values in columns that require data

## How to Fix It

### 1. Provide Explicit Values

```sql
-- WRONG: omitting the email column when it has NOT NULL
INSERT INTO users (name) VALUES ('John');

-- CORRECT: provide a value for the NOT NULL column
INSERT INTO users (name, email) VALUES ('John', 'john@example.com');
```

### 2. Add a DEFAULT Value

```sql
-- Add a default so future inserts succeed even without a value
ALTER TABLE users
    ALTER COLUMN email SET DEFAULT 'unknown@example.com';

-- Or use a more meaningful default
ALTER TABLE users
    ALTER COLUMN status SET DEFAULT 'pending';
```

### 3. Use COALESCE in Application Logic

```sql
-- Handle NULLs in queries that feed into INSERT/UPDATE
INSERT INTO users (name, email)
VALUES ('John', COALESCE(:email, 'no-email@example.com'));
```

### 4. Fix Existing NULLs Before Adding the Constraint

```sql
-- Find rows with NULLs in the target column
SELECT * FROM users WHERE email IS NULL;

-- Update them with a default value
UPDATE users SET email = 'unknown@example.com' WHERE email IS NULL;

-- Now safely add the constraint
ALTER TABLE users ALTER COLUMN email SET NOT NULL;
```

### 5. Use INSERT ON CONFLICT for Upserts

```sql
-- Ensure all required columns have values
INSERT INTO users (name, email)
VALUES ('John', 'john@example.com')
ON CONFLICT (email) DO UPDATE
SET name = EXCLUDED.name;
```

## Common Mistakes

- Adding `NOT NULL` to a column that already contains `NULL` values -- the `ALTER TABLE` will fail
- Assuming `DEFAULT` values are always applied -- they are only used when the column is omitted from the `INSERT`
- Not checking trigger functions for errors -- a failing trigger can cause the column to remain `NULL`
- Using `NOT NULL` without a `DEFAULT` on columns that applications frequently omit
- Importing CSV data with empty strings that PostgreSQL interprets as `NULL` for certain column types

## Related Pages

- [PostgreSQL Duplicate Key](/tools/postgresql/pg-duplicate-key)
- [PostgreSQL Foreign Key Violation](/tools/postgresql/pg-foreign-key-violation)
- [PostgreSQL Syntax Error](/tools/postgresql/pg-syntax-error)
- [MySQL Data Too Long](/tools/mysql/mysql-data-too-long)
