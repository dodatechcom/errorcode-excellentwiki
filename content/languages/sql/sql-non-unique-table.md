---
title: "[Solution] SQL Not Unique Table or Alias Fix"
description: "Fix 'Not unique table or alias in query' when the same table appears multiple times without unique aliases."
languages: ["sql"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["alias", "unique-table", "self-join", "ambiguous-reference"]
weight: 5
---

This error occurs when a query references the same table more than once without assigning unique aliases to each reference.

## What This Error Means

The database needs unique identifiers for each table reference in a query. When the same table appears multiple times (e.g., in self-joins), each must have a distinct alias.

## Common Causes

- Self-join without unique aliases
- Subquery referencing the same table as the outer query
- UNION query with same table names

## How to Fix

### Fix 1: Assign unique aliases

```sql
-- Wrong
SELECT a.name, b.salary
FROM employees a, employees b
WHERE a.id = b.id;

-- Correct
SELECT e.name, e.salary
FROM employees e
JOIN employees m ON e.manager_id = m.id;
```

### Fix 2: Use table prefixes everywhere

```sql
SELECT e.name AS employee, m.name AS manager
FROM employees AS e
INNER JOIN employees AS m ON e.manager_id = m.id;
```

## Examples

```sql
SELECT * FROM orders, orders WHERE orders.id = orders.user_id;
-- ERROR 1066: Not unique table/alias: 'orders'
```

## Related Errors

- [Multiple Tables Error](multiple-tables.md) — related alias issue
- [Column Not Found](column-not-found.md) — ambiguous column reference
