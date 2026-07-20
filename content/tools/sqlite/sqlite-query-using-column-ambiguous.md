---
title: "[Solution] SQLite USING column ambiguous"
description: "A JOIN USING clause specifies a column that appears in multiple tables, causing ambiguity."
tools: ["sqlite"]
error-types: ["query-error"]
severities: ["error"]
---


# [Solution] SQLite USING column ambiguous

SQLite raises **USING column ambiguous** when a join using clause specifies a column that appears in multiple tables, causing ambiguity. This error prevents the query from executing correctly.

## Common Causes

- Both tables have multiple columns with the same name.
- SELECT * after USING makes the shared column ambiguous.
- The USING column is referenced by table qualifier in SELECT.

## How to Fix

### Use explicit ON instead of USING

```sql
SELECT e.name, d.name AS dept
FROM employees e
JOIN departments d ON e.dept_id = d.id;
```

### Reference the USING column without table qualifier

```sql
SELECT name, dept_id FROM employees JOIN departments USING (dept_id);
```

### Select specific columns to avoid ambiguity

```sql
SELECT e.name, d.name AS dept_name FROM employees e JOIN departments d ON e.dept_id = d.id;
```

## Examples

```sql
SELECT employees.name FROM employees JOIN departments USING (id);
-- Error: ambiguous column name: id
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
