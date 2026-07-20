---
title: "[Solution] SQLite subquery returns more than 1 row"
description: "A scalar subquery used in a comparison returns more than one row."
tools: ["sqlite"]
error-types: ["query-error"]
severities: ["error"]
---


# [Solution] SQLite subquery returns more than 1 row

SQLite raises **subquery returns more than 1 row** when a scalar subquery used in a comparison returns more than one row. This error prevents the query from executing correctly.

## Common Causes

- A subquery in = comparison returns multiple rows.
- The subquery should use LIMIT 1 or an aggregate.
- IN was forgotten — the developer meant to use IN instead of =.

## How to Fix

### Use IN for multi-row subqueries

```sql
SELECT * FROM employees WHERE dept_id IN (SELECT id FROM departments WHERE active = 1);
```

### Add LIMIT 1 for scalar contexts

```sql
SELECT * FROM employees WHERE dept_id = (SELECT id FROM departments LIMIT 1);
```

### Use an aggregate for scalar contexts

```sql
SELECT * FROM employees WHERE salary = (SELECT MAX(salary) FROM employees);
```

## Examples

```sql
SELECT * FROM employees WHERE dept_id = (SELECT id FROM departments);
-- Error: subquery returns more than 1 row
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
