---
title: "SQL Recursive CTE Maximum Recursion Error"
description: "Fix SQL recursive CTE errors when maximum recursion depth is exceeded in common table expressions."
languages: ["sql"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- Recursive CTE does not have a proper termination condition (anchor)
- Circular references in hierarchical data create infinite loops
- MAXRECURSION limit set too low for deep hierarchies
- Self-referencing foreign keys without cycle detection
- UNION ALL used instead of UNION, preventing duplicate elimination

## How to Fix

```sql
-- WRONG: No termination condition
WITH RECURSIVE cte AS (
    SELECT id, name, parent_id FROM categories
    UNION ALL
    SELECT c.id, c.name, c.parent_id
    FROM categories c
    JOIN cte ON c.parent_id = cte.id  -- no cycle check
)
SELECT * FROM cte;
-- ERROR: maximum recursion depth exceeded

-- CORRECT: Add cycle detection
WITH RECURSIVE cte AS (
    SELECT id, name, parent_id, 0 AS depth
    FROM categories WHERE parent_id IS NULL
    UNION ALL
    SELECT c.id, c.name, c.parent_id, cte.depth + 1
    FROM categories c
    JOIN cte ON c.parent_id = cte.id
    WHERE cte.depth < 100  -- depth limit
)
SELECT * FROM cte;
```

```sql
-- WRONG: SQL Server default MAXRECURSION (100)
WITH cte AS (
    SELECT EmployeeID, ManagerID, 0 AS Level
    FROM Employees WHERE ManagerID IS NULL
    UNION ALL
    SELECT e.EmployeeID, e.ManagerID, c.Level + 1
    FROM Employees e
    JOIN cte c ON e.ManagerID = c.EmployeeID
)
SELECT * FROM cte
OPTION (MAXRECURSION 100);  -- too low

-- CORRECT: Increase limit or add OPTION
WITH cte AS (...)
SELECT * FROM cte
OPTION (MAXRECURSION 0);  -- unlimited (use with caution)
```

## Examples

```sql
-- Example 1: PostgreSQL recursive CTE
WITH RECURSIVE org_chart AS (
    SELECT id, name, manager_id, 1 AS level
    FROM employees WHERE manager_id IS NULL
    UNION ALL
    SELECT e.id, e.name, e.manager_id, oc.level + 1
    FROM employees e
    INNER JOIN org_chart oc ON e.manager_id = oc.id
    WHERE oc.level < 10
)
SELECT * FROM org_chart ORDER BY level;

-- Example 2: Generate number sequence
WITH RECURSIVE nums AS (
    SELECT 1 AS n
    UNION ALL
    SELECT n + 1 FROM nums WHERE n < 1000
)
SELECT n FROM nums OPTION (MAXRECURSION 1100);

-- Example 3: Bill of materials explosion
WITH RECURSIVE bom AS (
    SELECT part_id, quantity, parent_id
    FROM parts WHERE parent_id IS NULL
    UNION ALL
    SELECT p.part_id, p.quantity * bom.quantity, p.parent_id
    FROM parts p
    JOIN bom ON p.parent_id = bom.part_id
)
SELECT * FROM bom;
```

## Related Errors

- [Recursive CTE error](sql-recursive-cte) -- general recursive CTE issues
- [Recursive CTE v2](sql-recursive-cte-v2) -- advanced recursive queries
