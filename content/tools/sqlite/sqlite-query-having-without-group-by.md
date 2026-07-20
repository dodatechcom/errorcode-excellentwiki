---
title: "[Solution] SQLite HAVING without GROUP BY"
description: "A HAVING clause is used without a corresponding GROUP BY clause."
tools: ["sqlite"]
error-types: ["query-error"]
severities: ["error"]
---


# [Solution] SQLite HAVING without GROUP BY

SQLite raises **HAVING without GROUP BY** when a having clause is used without a corresponding group by clause. This error prevents the query from executing correctly.

## Common Causes

- The query uses HAVING but omits GROUP BY.
- The developer intended to filter groups but forgot GROUP BY.
- SQLite treats an ungrouped query as a single group, which may be confusing.

## How to Fix

### Add a GROUP BY clause

```sql
SELECT department, COUNT(*)
FROM employees
GROUP BY department
HAVING COUNT(*) > 5;
```

### Use WHERE instead if filtering individual rows

```sql
SELECT * FROM employees WHERE department = 'Engineering';
```

### Understand that without GROUP BY, HAVING filters the entire result

```sql
-- This works but filters all rows as one group:
SELECT COUNT(*) FROM employees HAVING COUNT(*) > 0;
```

## Examples

```sql
SELECT department, COUNT(*) FROM employees HAVING COUNT(*) > 5;
-- Error: HAVING clause without GROUP BY
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
