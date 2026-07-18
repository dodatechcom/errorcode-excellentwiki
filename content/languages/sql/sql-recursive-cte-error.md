---
title: "[Solution] SQL Recursive CTE Max Depth Exceeded Error Fix"
description: "Fix 'recursive CTE max depth exceeded' in SQL. Control recursion depth in Common Table Expressions with proper base cases."
languages: ["sql"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# SQL Recursive CTE Max Depth Exceeded Error Fix

The `recursive CTE max depth exceeded` error occurs when a recursive Common Table Expression runs beyond the database's maximum recursion depth limit.

## What This Error Means

Recursive CTEs repeatedly execute until no more rows are returned. If the recursion does not terminate (missing base case or circular references), the database hits its depth limit and stops execution.

A typical error:

```
ERROR: recursive query "org_hierarchy" depth limit exceeded
```

## Why It Happens

Common causes include:

- **Missing base case** — The anchor member does not limit recursion.
- **Circular references** — Parent-child relationships form a loop.
- **Self-referencing data** — A row references itself.
- **Too many hierarchy levels** — Legitimate deep hierarchy exceeds default limit.
- **Wrong join condition** — Recursion keeps matching the same rows.

## How to Fix It

### Fix 1: Add a depth counter

```sql
-- RIGHT: Track recursion depth
WITH RECURSIVE org_hierarchy AS (
    -- Anchor: top-level managers
    SELECT id, name, manager_id, 1 AS depth
    FROM employees
    WHERE manager_id IS NULL
    
    UNION ALL
    
    -- Recursive: subordinates
    SELECT e.id, e.name, e.manager_id, h.depth + 1
    FROM employees e
    JOIN org_hierarchy h ON e.manager_id = h.id
    WHERE h.depth < 10  -- Limit depth
)
SELECT * FROM org_hierarchy;
```

### Fix 2: Detect circular references

```sql
-- RIGHT: Track visited nodes
WITH RECURSIVE tree AS (
    SELECT id, name, parent_id, 
           ARRAY[id] AS visited
    FROM nodes
    WHERE id = 1
    
    UNION ALL
    
    SELECT n.id, n.name, n.parent_id,
           t.visited || n.id
    FROM nodes n
    JOIN tree t ON n.parent_id = t.id
    WHERE n.id <> ALL(t.visited)  -- Prevent cycles
)
SELECT * FROM tree;
```

### Fix 3: Increase depth limit

```sql
-- PostgreSQL
SET max_recursive_iterations = 10000;

-- SQL Server
OPTION (MAXRECURSION 10000);
```

### Fix 4: Add termination condition

```sql
-- RIGHT: Multiple termination conditions
WITH RECURSIVE traversal AS (
    SELECT id, data, 1 AS level, 'root' AS path
    FROM nodes WHERE parent_id IS NULL
    
    UNION ALL
    
    SELECT n.id, n.data, t.level + 1,
           t.path || ' -> ' || n.data
    FROM nodes n
    JOIN traversal t ON n.parent_id = t.id
    WHERE t.level < 20              -- Depth limit
    AND n.data <> t.data            -- Prevent self-loops
    AND n.data NOT LIKE t.path || '%' -- Prevent cycles
)
SELECT * FROM traversal;
```

### Fix 5: Use iterative approach for very deep hierarchies

```sql
-- RIGHT: Use temp table for iterative traversal
CREATE TEMP TABLE traversal (
    id INT, level INT, path TEXT
);

INSERT INTO traversal 
SELECT id, 0, name FROM nodes WHERE parent_id IS NULL;

-- Loop until no new rows
WHILE (SELECT COUNT(*) FROM traversal t 
       JOIN nodes n ON n.parent_id = t.id 
       WHERE t.level < 20) > 0
BEGIN
    INSERT INTO traversal
    SELECT n.id, t.level + 1, t.path || ' -> ' || n.name
    FROM traversal t
    JOIN nodes n ON n.parent_id = t.id
    WHERE t.level < 20;
END
```

## Common Mistakes

- **Not adding a depth counter** — Always limit recursion depth.
- **Forgetting circular reference detection** — Check for visited nodes.
- **Assuming default depth limit is sufficient** — Increase for deep hierarchies.

## Related Pages

- [SQL Recursive CTE Error](sql-recursive-cte-error) — CTE recursion issues
- [SQL Subquery Error](sql-subquery-error) — Subquery return issues
- [SQL Window Function Error](sql-window-function-error) — Window function issues
