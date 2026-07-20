---
title: "[Solution] SQLite LEFT JOIN ON clause error"
description: "A LEFT JOIN is used without a proper ON clause, or the ON clause references wrong columns."
tools: ["sqlite"]
error-types: ["query-error"]
severities: ["error"]
---


# [Solution] SQLite LEFT JOIN ON clause error

SQLite raises **LEFT JOIN ON clause error** when a left join is used without a proper on clause, or the on clause references wrong columns. This error prevents the query from executing correctly.

## Common Causes

- Missing ON clause.
- ON clause uses = instead of IS when comparing with NULL.
- Wrong column references in the ON condition.

## How to Fix

### Always provide an ON clause with LEFT JOIN

```sql
SELECT e.name, d.name AS dept
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.id;
```

### Use IS NOT NULL for NULL comparisons in ON

```sql
SELECT * FROM a LEFT JOIN b ON a.id = b.a_id AND b.status IS NOT NULL;
```

### Verify column names exist in both tables

```sql
PRAGMA table_info(employees);
PRAGMA table_info(departments);
```

## Examples

```sql
SELECT * FROM employees LEFT JOIN departments;
-- Error: LEFT JOIN requires an ON clause
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
