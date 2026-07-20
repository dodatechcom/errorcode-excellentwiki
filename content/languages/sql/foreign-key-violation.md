---
title: "[Solution] Foreign Key Constraint Fails"
description: "Fix 'Foreign key constraint fails' when a referenced row does not exist or a dependent row prevents deletion."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "sql"
tags: ["sql", "constraint, foreign-key, referential-integrity"]
severity: "error"
---

# Foreign Key Constraint Fails

## Error Message

```
ERROR 1452: Cannot add or update a child row: a foreign key constraint fails — The referenced parent row does not exist, or the referenced row cannot be deleted because dependent rows exist.
```

## Common Causes

- INSERT or UPDATE references a parent row that does not exist in the referenced table
- DELETE or UPDATE on a parent row that has dependent child rows without CASCADE
- Column data types between parent and child tables do not match
- The foreign key index was dropped or never created

## Solutions

### Solution 1: Ensure parent rows exist before inserting child rows

Verify the referenced value exists in the parent table before inserting into the child table.

```sql
-- Check if the parent row exists
SELECT * FROM departments WHERE id = 5;

-- Insert parent first, then child
INSERT INTO departments (id, name) VALUES (5, 'Engineering');
INSERT INTO employees (name, department_id) VALUES ('Alice', 5);

-- Use INSERT with subquery to verify existence
INSERT INTO employees (name, department_id)
SELECT 'Alice', id FROM departments WHERE name = 'Engineering';
```

### Solution 2: Delete or update child rows before removing the parent

Remove dependent rows first, or use CASCADE to handle them automatically.

```sql
-- Option 1: Delete child rows first
DELETE FROM employees WHERE department_id = 5;
DELETE FROM departments WHERE id = 5;

-- Option 2: Add ON DELETE CASCADE to the foreign key
ALTER TABLE employees
DROP FOREIGN KEY fk_department;

ALTER TABLE employees
ADD CONSTRAINT fk_department
FOREIGN KEY (department_id) REFERENCES departments(id)
ON DELETE CASCADE ON UPDATE CASCADE;

-- Option 3: Set NULL when parent is deleted
ALTER TABLE employees
ADD CONSTRAINT fk_department
FOREIGN KEY (department_id) REFERENCES departments(id)
ON DELETE SET NULL;
```

### Solution 3: Verify matching data types between tables

Foreign key columns must have identical data types and character sets.

```sql
-- Wrong: INT vs BIGINT mismatch
CREATE TABLE parent (id INT PRIMARY KEY);
CREATE TABLE child (parent_id BIGINT REFERENCES parent(id));

-- Correct: match data types
CREATE TABLE parent (id INT PRIMARY KEY);
CREATE TABLE child (parent_id INT REFERENCES parent(id));

-- Wrong: character set mismatch in MySQL
CREATE TABLE parent (id VARCHAR(10) CHARACTER SET utf8mb4);
CREATE TABLE child (parent_id VARCHAR(10) CHARACTER SET latin1);

-- Correct: use same character set
CREATE TABLE child (
    parent_id VARCHAR(10) CHARACTER SET utf8mb4
);
```

## Prevention Tips

- Always design foreign keys with ON DELETE and ON UPDATE actions (CASCADE, SET NULL, or RESTRICT)
- Use transactions when inserting into both parent and child tables to ensure consistency
- Run SHOW CREATE TABLE to verify foreign key definitions when troubleshooting constraint failures

## Related Errors

- [Not Null Constraint]({{< relref "/languages/sql/not-null-constraint.md" >}})
- [Primary Key Violation]({{< relref "/languages/sql/primary-key-violation.md" >}})
- [Foreign Key]({{< relref "/languages/sql/foreign-key.md" >}})
