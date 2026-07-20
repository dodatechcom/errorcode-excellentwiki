---
title: "[Solution] Composite Key Violation"
description: "Fix 'Composite key violation' when a combination of columns in a composite unique constraint is duplicated."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "sql"
tags: ["sql", "constraint, composite-key, unique"]
severity: "error"
---

# Composite Key Violation

## Error Message

```
ERROR 23505: duplicate key value violates unique constraint 'constraint_name' — The combination of values in the composite key columns already exists.
```

## Common Causes

- INSERT attempts to add a row where the combination of composite key columns already exists
- Partial composite key update creates a duplicate combination
- Composite unique index defined on columns that legitimately have repeated individual values
- Incorrect assumption that individual columns are unique rather than the combination

## Solutions

### Solution 1: Understand composite uniqueness

A composite unique constraint means the combination of columns must be unique, not each individual column.

```sql
-- Composite unique constraint: student_id + course_id combination must be unique
CREATE TABLE enrollments (
    id INT PRIMARY KEY,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    enrolled_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (student_id, course_id)
);

-- This is fine: different student, same course
INSERT INTO enrollments (id, student_id, course_id) VALUES (1, 101, 201);

-- This is fine: same student, different course
INSERT INTO enrollments (id, student_id, course_id) VALUES (2, 101, 202);

-- This fails: duplicate combination
INSERT INTO enrollments (id, student_id, course_id) VALUES (3, 101, 201);
-- ERROR 23505: duplicate key value violates unique constraint
```

### Solution 2: Use ON CONFLICT for composite keys

Handle composite key violations with upsert logic.

```sql
-- PostgreSQL: ON CONFLICT with composite key
INSERT INTO enrollments (student_id, course_id)
VALUES (101, 201)
ON CONFLICT (student_id, course_id)
DO UPDATE SET enrolled_at = CURRENT_TIMESTAMP;

-- MySQL: ON DUPLICATE KEY with composite unique
INSERT INTO enrollments (student_id, course_id)
VALUES (101, 201)
ON DUPLICATE KEY UPDATE enrolled_at = CURRENT_TIMESTAMP;

-- Check existing composite key values
SELECT student_id, course_id, COUNT(*)
FROM enrollments
GROUP BY student_id, course_id
HAVING COUNT(*) > 1;
```

### Solution 3: Use a junction table for many-to-many relationships

Composite keys are ideal for junction tables that link two entities.

```sql
-- Junction table with composite primary key
CREATE TABLE order_items (
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 1,
    PRIMARY KEY (order_id, product_id)
);

-- Insert a new line item
INSERT INTO order_items (order_id, product_id, quantity)
VALUES (1001, 501, 3);

-- Update quantity instead of inserting duplicate
INSERT INTO order_items (order_id, product_id, quantity)
VALUES (1001, 501, 5)
ON DUPLICATE KEY UPDATE quantity = quantity + VALUES(quantity);

-- PostgreSQL version
INSERT INTO order_items (order_id, product_id, quantity)
VALUES (1001, 501, 3)
ON CONFLICT (order_id, product_id)
DO UPDATE SET quantity = order_items.quantity + EXCLUDED.quantity;
```

## Prevention Tips

- Model many-to-many relationships using junction tables with composite primary keys
- Use ON CONFLICT or ON DUPLICATE KEY to handle upserts in junction tables gracefully
- Clearly document whether a unique constraint applies to individual columns or their combination

## Related Errors

- [Primary Key Violation]({{< relref "/languages/sql/primary-key-violation.md" >}})
- [Unique Constraint Violation]({{< relref "/languages/sql/unique-constraint-violation.md" >}})
- [Unique Index Error]({{< relref "/languages/sql/unique-index-error.md" >}})
