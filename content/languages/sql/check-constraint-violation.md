---
title: "[Solution] Check Constraint Violation"
description: "Fix 'Check constraint violation' when a value fails a CHECK constraint condition."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "sql"
tags: ["sql", "constraint, check"]
severity: "error"
---

# Check Constraint Violation

## Error Message

```
ERROR 3819: Check constraint 'constraint_name' is violated — The inserted or updated value does not satisfy the CHECK condition.
```

## Common Causes

- The inserted value does not satisfy the CHECK constraint's logical condition
- UPDATE modifies a column to a value that violates the CHECK constraint
- CHECK constraint definition contains incorrect logic or boundary values
- NULL values bypass CHECK constraints in some databases (MySQL before 8.0.16 ignores CHECK)

## Solutions

### Solution 1: Review and fix the data to satisfy the constraint

Ensure the values you are inserting or updating meet the CHECK constraint's requirements.

```sql
-- Example: age must be between 0 and 150
CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT CHECK (age >= 0 AND age <= 150)
);

-- Wrong: violates CHECK constraint
INSERT INTO users (id, name, age) VALUES (1, 'Alice', -5);

-- Correct: satisfy the constraint
INSERT INTO users (id, name, age) VALUES (1, 'Alice', 30);

-- Correct: update to a valid value
UPDATE users SET age = 25 WHERE id = 1;
```

### Solution 2: Modify or drop the CHECK constraint if requirements change

Alter the constraint definition if business rules have changed.

```sql
-- View existing constraints
SELECT constraint_name, check_clause
FROM information_schema.check_constraints
WHERE table_name = 'users';

-- Drop the constraint
ALTER TABLE users DROP CHECK chk_age;

-- Add a new constraint with updated logic
ALTER TABLE users
ADD CONSTRAINT chk_age CHECK (age >= 0 AND age <= 200);

-- PostgreSQL: rename and recreate
ALTER TABLE users DROP CONSTRAINT chk_age;
ALTER TABLE users ADD CONSTRAINT chk_age_range CHECK (age BETWEEN 0 AND 200);
```

### Solution 3: Use application-level validation alongside CHECK constraints

Validate data in your application before sending it to the database.

```sql
-- Application-level check before INSERT (pseudocode)
-- if user.age < 0 or user.age > 150:
--     raise ValidationError("Age must be between 0 and 150")

-- Complex CHECK constraint with multiple conditions
CREATE TABLE orders (
    id INT PRIMARY KEY,
    total DECIMAL(10,2),
    discount DECIMAL(10,2),
    final_amount DECIMAL(10,2),
    CHECK (discount >= 0 AND discount <= total),
    CHECK (final_amount = total - discount),
    CHECK (final_amount >= 0)
);
```

## Prevention Tips

- Use CHECK constraints to enforce business rules at the database level for data integrity
- Name your CHECK constraints descriptively so error messages are easy to interpret
- Test CHECK constraints with edge cases including boundary values and NULL before deploying to production

## Related Errors

- [Not Null Constraint]({{< relref "/languages/sql/not-null-constraint.md" >}})
- [Default Constraint Error]({{< relref "/languages/sql/default-constraint-error.md" >}})
- [Unique Constraint Violation]({{< relref "/languages/sql/unique-constraint-violation.md" >}})
