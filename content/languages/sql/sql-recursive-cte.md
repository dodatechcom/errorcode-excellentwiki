---
title: "[Solution] SQL Recursive CTE Maximum Recursion Fix"
description: "Fix 'Recursive CTE maximum recursion exceeded' when a CTE recursion depth limit is reached."
languages: ["sql"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["recursive-cte", "recursion", "common-table-expression", "hierarchy"]
weight: 5
---

This error occurs when a recursive Common Table Expression (CTE) exceeds the maximum recursion depth. The message reads: `Recursive CTE maximum recursion exceeded`.

## What This Error Means

Recursive CTEs iterate through hierarchical data by referencing themselves. The database enforces a recursion limit to prevent infinite loops from circular references in the data.

## Common Causes

- Circular reference in hierarchical data (A → B → A)
- Default recursion limit too low for deep hierarchies
- CTE lacks a proper termination condition
- Self-referencing foreign key creates infinite loop

## How to Fix

### Fix 1: Increase the recursion limit

```sql
SET SESSION cte_max_recursion_depth = 1000; -- default is 1000

-- Use the CTE
WITH RECURSIVE org_chart AS (
    SELECT id, name, manager_id, 1 AS level
    FROM employees WHERE manager_id IS NULL
    UNION ALL
    SELECT e.id, e.name, e.manager_id, oc.level + 1
    FROM employees e
    JOIN org_chart oc ON e.manager_id = oc.id
)
SELECT * FROM org_chart;
```

### Fix 2: Add a termination condition

```sql
WITH RECURSIVE tree AS (
    SELECT id, name, parent_id, 0 AS depth
    FROM categories WHERE id = 1
    UNION ALL
    SELECT c.id, c.name, c.parent_id, t.depth + 1
    FROM categories c
    JOIN tree t ON c.parent_id = t.id
    WHERE t.depth < 10  -- Prevent infinite recursion
)
SELECT * FROM tree;
```

### Fix 3: Detect circular references in data

```sql
-- Find circular references
WITH RECURSIVE paths AS (
    SELECT id, parent_id, CAST(id AS CHAR) AS path
    FROM categories
    WHERE parent_id IS NULL
    UNION ALL
    SELECT c.id, c.parent_id, CONCAT(p.path, '->', c.id)
    FROM categories c
    JOIN paths p ON c.parent_id = p.id
    WHERE FIND_IN_SET(c.id, p.path) = 0  -- Detect cycle
)
SELECT * FROM paths;
```

## Examples

```sql
WITH RECURSIVE cte AS (
    SELECT 1 AS n
    UNION ALL
    SELECT n + 1 FROM cte WHERE n < 2000
)
SELECT * FROM cte;
-- ERROR 3636: Recursive CTE maximum recursion exceeded (1000)
```

## Related Errors

- [Subquery Error](subquery-error.md) — related query issue
- [Syntax Error](syntax-error.md) — malformed SQL
