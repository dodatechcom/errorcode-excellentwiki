---
title: "[Solution] PostgreSQL Recursive Query Limit Exceeded"
description: "Fix PostgreSQL recursive query limit error. Resolve CTE recursion depth issues in hierarchical queries."
tools: ["postgresql"]
error-types: ["tool-error"]
severities: ["error"]
---

# PostgreSQL Recursive Query Limit Exceeded

ERROR: recursive query limit exceeded

This error occurs when a recursive Common Table Expression (CTE) exceeds PostgreSQL's default recursion depth limit of 100 iterations.

## Common Causes

- Infinite recursion due to circular references in parent-child relationships
- Missing termination condition in the recursive CTE
- Very deep hierarchical data structures exceeding the default limit

## How to Fix

1. Check your recursive CTE for circular references:

```sql
WITH RECURSIVE org_tree AS (
  SELECT id, name, parent_id, 1 AS depth
  FROM employees
  WHERE parent_id IS NULL
  UNION ALL
  SELECT e.id, e.name, e.parent_id, t.depth + 1
  FROM employees e
  JOIN org_tree t ON e.parent_id = t.id
  WHERE t.depth < 20
)
SELECT * FROM org_tree;
```

2. Increase the recursion limit for the session:

```sql
SET max_recursive_iterations = 1000;
```

3. Add a cycle detection column to prevent infinite loops:

```sql
WITH RECURSIVE tree AS (
  SELECT id, name, ARRAY[id] AS path
  FROM categories WHERE parent_id IS NULL
  UNION ALL
  SELECT c.id, c.name, t.path || c.id
  FROM categories c
  JOIN tree t ON c.parent_id = t.id
  WHERE c.id <> ALL(t.path)
)
SELECT * FROM tree;
```

## Examples

```sql
-- Detect circular references in your data
WITH RECURSIVE cycle_check AS (
  SELECT id, parent_id, ARRAY[id] AS visited
  FROM categories
  UNION ALL
  SELECT c.id, c.parent_id, cc.visited || c.id
  FROM categories c
  JOIN cycle_check cc ON c.parent_id = cc.id
  WHERE c.id <> ALL(cc.visited)
)
SELECT id, visited
FROM cycle_check
WHERE array_length(visited, 1) > 100;
```
