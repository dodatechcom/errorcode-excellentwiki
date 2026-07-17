---
title: "[Solution] SQL Recursive CTE Max Recursion Exceeded Error Fix"
description: "Fix SQL recursive CTE errors when the maximum recursion depth is exceeded."
languages: ["sql"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# SQL Recursive CTE Max Recursion Exceeded Error Fix

A SQL recursive CTE error occurs when a recursive Common Table Expression exceeds the maximum recursion depth.

## What This Error Means

Recursive CTEs iterate until a终止 condition is met. If the recursion doesn't terminate (circular references, missing base case), it hits the max recursion limit (default 100 in SQL Server, no limit in MySQL/PostgreSQL).

## Common Causes

- Circular references in data (parent references child)
- Missing终止 condition in recursion
- Infinite loops in hierarchical data
- MAXRECURSION too low for deep hierarchies

## How to Fix

### 1. Add proper终止 condition

```sql
-- CORRECT: Always have a终止 condition
WITH RECURSIVE org_chart AS (
    -- Base case (anchor)
    SELECT id, name, manager_id, 1 as level
    FROM employees
    WHERE manager_id IS NULL

    UNION ALL

    -- Recursive case
    SELECT e.id, e.name, e.manager_id, oc.level + 1
    FROM employees e
    JOIN org_chart oc ON e.manager_id = oc.id
    WHERE oc.level < 10  -- Terminates recursion
)
SELECT * FROM org_chart;
```

### 2. Increase recursion limit (SQL Server)

```sql
-- CORRECT: Increase MAXRECURSION
OPTION (MAXRECURSION 0);  -- No limit (use carefully)
-- Or
OPTION (MAXRECURSION 1000);
```

### 3. Detect circular references

```sql
-- CORRECT: Track visited nodes
WITH RECURSIVE tree AS (
    SELECT id, name, parent_id,
           CAST(id AS VARCHAR(1000)) as path
    FROM nodes
    WHERE parent_id IS NULL

    UNION ALL

    SELECT n.id, n.name, n.parent_id,
           CONCAT(t.path, '->', n.id)
    FROM nodes n
    JOIN tree t ON n.parent_id = t.id
    WHERE FIND_IN_SET(n.id, t.path) = 0  -- No cycles
)
SELECT * FROM tree;
```

### 4. Use iterative approach for complex hierarchies

```sql
-- CORRECT: Use temp table for iterative traversal
CREATE TEMPORARY TABLE hierarchy (
    id INT, name VARCHAR(255), level INT
);

INSERT INTO hierarchy
SELECT id, name, 0 FROM employees WHERE manager_id IS NULL;

SET @level = 0;
WHILE ROW_COUNT() > 0 DO
    SET @level = @level + 1;
    INSERT INTO hierarchy
    SELECT e.id, e.name, @level
    FROM employees e
    JOIN hierarchy h ON e.manager_id = h.id
    WHERE h.level = @level - 1;
END WHILE;
```

## Related Errors

- [SQL Subquery Error](sql-subquery-error-v2) — subquery issues
- [SQL Window Function Error](sql-window-function-v2) — window functions
- [SQL Syntax Error](sql-syntax-error-v2) — syntax issues
