---
title: "[Solution] SQLite JOIN syntax error"
description: "A JOIN clause contains a syntax error or uses incompatible join types."
tools: ["sqlite"]
error-types: ["query-error"]
severities: ["error"]
---


# [Solution] SQLite JOIN syntax error

SQLite raises **JOIN syntax error** when a join clause contains a syntax error or uses incompatible join types. This error prevents the query from executing correctly.

## Common Causes

- Missing ON clause for INNER JOIN.
- Incorrect join type keyword.
- Parentheses used incorrectly in complex joins.

## How to Fix

### Provide an ON clause for INNER JOIN

```sql
SELECT e.name, d.name
FROM employees e
INNER JOIN departments d ON e.dept_id = d.id;
```

### Use correct JOIN keywords

```sql
-- Valid: INNER JOIN, LEFT JOIN, CROSS JOIN, NATURAL JOIN
-- Invalid: INNER OUTER JOIN
```

### Parenthesize complex joins

```sql
SELECT * FROM (a INNER JOIN b ON a.id = b.a_id) INNER JOIN c ON b.id = c.b_id;
```

## Examples

```sql
SELECT * FROM employees JOIN departments;
-- Error: JOIN without ON clause (in strict mode)
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
