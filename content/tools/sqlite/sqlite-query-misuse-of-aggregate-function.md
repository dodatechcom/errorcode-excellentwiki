---
title: "[Solution] SQLite misuse of aggregate function"
description: "An aggregate function (SUM, COUNT, AVG, etc.) is used in a context where it is not valid."
tools: ["sqlite"]
error-types: ["query-error"]
severities: ["error"]
---


# [Solution] SQLite misuse of aggregate function

SQLite raises **misuse of aggregate function** when an aggregate function (sum, count, avg, etc.) is used in a context where it is not valid. This error prevents the query from executing correctly.

## Common Causes

- Using an aggregate in a WHERE clause instead of HAVING.
- Mixing aggregate and non-aggregate columns without GROUP BY.
- Nesting aggregates incorrectly.

## How to Fix

### Use HAVING for aggregate conditions

```sql
SELECT department, COUNT(*) as cnt
FROM employees
GROUP BY department
HAVING COUNT(*) > 5;
```

### Include all non-aggregate columns in GROUP BY

```sql
SELECT department, name, COUNT(*)
FROM employees
GROUP BY department, name;
```

### Do not nest aggregates

```sql
-- Wrong: COUNT(SUM(x))
-- Right: compute step by step in a subquery
SELECT cnt FROM (SELECT COUNT(*) as cnt FROM t);
```

## Examples

```sql
SELECT name, COUNT(*) FROM users;
-- Error: misuse of aggregate function COUNT()
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
