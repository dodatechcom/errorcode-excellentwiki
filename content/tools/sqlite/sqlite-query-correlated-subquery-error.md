---
title: "[Solution] SQLite correlated subquery error"
description: "A correlated subquery references an outer table but is structured incorrectly."
tools: ["sqlite"]
error-types: ["query-error"]
severities: ["error"]
---


# [Solution] SQLite correlated subquery error

SQLite raises **correlated subquery error** when a correlated subquery references an outer table but is structured incorrectly. This error prevents the query from executing correctly.

## Common Causes

- The subquery references a column from the outer query that does not exist.
- The subquery is not correlated but should be (or vice versa).
- Performance issue: the correlated subquery executes for every outer row.

## How to Fix

### Verify outer column references

```sql
SELECT e.name FROM employees e
WHERE e.salary > (SELECT AVG(salary) FROM employees WHERE dept_id = e.dept_id);
```

### Rewrite as a JOIN for better performance

```sql
SELECT e.name
FROM employees e
JOIN (SELECT dept_id, AVG(salary) AS avg_sal FROM employees GROUP BY dept_id) d
  ON e.dept_id = d.dept_id
WHERE e.salary > d.avg_sal;
```

### Check that the correlated column is qualified with a table alias

```sql
-- Use e.dept_id, not just dept_id
```

## Examples

```sql
SELECT name FROM employees e
WHERE salary > (SELECT AVG(salary) FROM employees WHERE dept_id = dept_id);
-- dept_id is ambiguous — may not correlate correctly
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
