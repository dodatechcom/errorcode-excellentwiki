---
title: "SQL CROSS JOIN Unexpected Cartesian Product Error"
description: "Fix SQL CROSS JOIN errors when accidental cartesian products produce millions of unexpected result rows."
languages: ["sql"]
error-types: ["logic-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- Missing JOIN condition turns intended INNER JOIN into CROSS JOIN
- FROM clause has multiple tables without WHERE relationship
- Implicit join syntax (comma-separated tables) without WHERE
- UNION of queries with different column counts
- Accidental CROSS JOIN used instead of INNER JOIN

## How to Fix

```sql
-- WRONG: Missing join condition
SELECT e.name, d.name
FROM employees e, departments d;
-- Returns every combination (cartesian product)

-- CORRECT: Add join condition
SELECT e.name, d.name
FROM employees e
INNER JOIN departments d ON e.dept_id = d.id;
```

```sql
-- WRONG: Accidental CROSS JOIN
SELECT * FROM products CROSS JOIN categories;
-- 1000 products * 50 categories = 50000 rows

-- CORRECT: Use INNER JOIN with condition
SELECT * FROM products p
INNER JOIN categories c ON p.category_id = c.id;
```

## Examples

```sql
-- Example 1: Fix implicit cross join
-- BAD
SELECT * FROM orders, customers;
-- GOOD
SELECT * FROM orders o JOIN customers c ON o.customer_id = c.id;

-- Example 2: Intentional CROSS JOIN for combinations
SELECT s.day, t.time_slot
FROM days s
CROSS JOIN time_slots t
ORDER BY s.day, t.time_slot;

-- Example 3: Check result cardinality
SELECT COUNT(*) FROM orders o, customers c;
-- If this is much larger than expected, you have a cartesian product
```

## Related Errors

- [Join error](join-error) -- JOIN clause issues
- [Multiple tables error](sql-multiple-tables) -- table reference problems
