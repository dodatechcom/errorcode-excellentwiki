---
title: "[Solution] SQLite recursive CTE limit exceeded"
description: "A recursive Common Table Expression (CTE) exceeded the maximum recursion depth (default 1000)."
tools: ["sqlite"]
error-types: ["query-error"]
severities: ["error"]
---


# [Solution] SQLite recursive CTE limit exceeded

SQLite raises **recursive CTE limit exceeded** when a recursive common table expression (cte) exceeded the maximum recursion depth (default 1000). This error prevents the query from executing correctly.

## Common Causes

- The recursive CTE has no proper termination condition.
- The data contains a cycle that was not handled.
- The default recursion limit is too low for the query.

## How to Fix

### Add a proper termination condition

```sql
WITH RECURSIVE cte AS (
    SELECT id, parent_id, 0 AS depth
    FROM tree WHERE parent_id IS NULL
    UNION ALL
    SELECT t.id, t.parent_id, c.depth + 1
    FROM tree t JOIN cte c ON t.parent_id = c.id
    WHERE c.depth < 100  -- termination condition
)
SELECT * FROM cte;
```

### Increase the recursion limit

```sql
-- In C API: sqlite3_limit(db, SQLITE_LIMIT_LENGTH, 100000);
-- In CLI: no direct way, must recompile
```

### Handle cycles with a visited set

```sql
-- Track visited nodes in a temp table to avoid cycles
```

## Examples

```sql
WITH RECURSIVE cnt(x) AS (
    SELECT 1
    UNION ALL
    SELECT x + 1 FROM cnt
)
SELECT * FROM cnt;
-- Error: recursion limit of 1000 exceeded
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
