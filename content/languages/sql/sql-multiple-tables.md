---
title: "[Solution] SQL Not Unique Table or Alias Fix"
description: "Fix 'Not unique table or alias' when a table is referenced multiple times in a query without aliases."
languages: ["sql"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

This error occurs when a query references the same table multiple times without using different aliases. The message reads: `Not unique table/alias: 'X'`.

## What This Error Means

When joining a table to itself or referencing the same table multiple times, each reference must have a unique alias so the database can distinguish between them.

## Common Causes

- Self-join without aliases
- Subquery references the same table as outer query
- Multiple joins to the same table without distinct aliases

## How to Fix

### Fix 1: Use unique aliases for self-joins

```sql
-- Wrong: same table referenced twice without alias
SELECT a.name, b.name
FROM employees a, employees b
WHERE a.manager_id = b.id;

-- Correct
SELECT e.name AS employee, m.name AS manager
FROM employees e
JOIN employees m ON e.manager_id = m.id;
```

### Fix 2: Use different aliases in subqueries

```sql
-- Wrong
SELECT * FROM orders o
WHERE o.user_id IN (SELECT id FROM orders WHERE total > 100);

-- Correct — use different alias
SELECT * FROM orders o
WHERE o.user_id IN (SELECT o2.user_id FROM orders o2 WHERE o2.total > 100);
```

### Fix 3: Use table prefixes in SELECT

```sql
SELECT u.id, u.name, o.id, o.total
FROM users u
JOIN orders o ON u.id = o.user_id;
```

## Examples

```sql
SELECT e.name, m.name
FROM employees e
JOIN employees ON e.manager_id = employees.id;
-- ERROR 1066: Not unique table/alias: 'employees'
```

## Related Errors

- [Column Not Found](column-not-found.md) — ambiguous column
- [Multiple Tables Error](multiple-tables.md) — related alias issue
