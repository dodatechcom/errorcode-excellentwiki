---
title: "[Solution] SQL ORDER BY Position Out Of Range Error Fix"
description: "Fix 'ORDER BY position is out of range' in SQL. Use column names instead of positional references in ORDER BY clauses."
languages: ["sql"]
error-types: ["syntax-error"]
severities: ["error"]
weight: 5
---

# SQL ORDER BY Position Out Of Range Error Fix

The `ORDER BY position is out of range` error occurs when you reference a column position in ORDER BY that does not exist in the SELECT list.

## What This Error Means

SQL allows ordering by column position (e.g., `ORDER BY 1` for the first column). When you reference a position beyond the number of selected columns, the database reports this error.

A typical error:

```
ERROR: ORDER BY position 4 is out of range for SELECT with 3 columns
```

## Why It Happens

Common causes include:

- **Wrong position number** — Referencing `ORDER BY 5` when only 4 columns are selected.
- **Columns removed from SELECT** — Query was modified but ORDER BY was not updated.
- **Dynamic column lists** — Application generates different column counts.
- **Using positional ORDER BY with UNION** — Column count changes after UNION.
- **CTE or subquery with fewer columns** — Referencing outer positions in inner query.

## How to Fix It

### Fix 1: Use column names instead of positions

```sql
-- WRONG: Fragile positional reference
SELECT id, name, email FROM users ORDER BY 3;

-- RIGHT: Use column name
SELECT id, name, email FROM users ORDER BY email;
```

### Fix 2: Verify column count matches

```sql
-- RIGHT: Count columns carefully
SELECT id, name, email, created_at
FROM users
ORDER BY 4;  -- created_at is 4th column
```

### Fix 3: Use ORDER BY with expressions

```sql
-- RIGHT: Use expressions for complex sorting
SELECT id, name, email
FROM users
ORDER BY 
    CASE WHEN name IS NULL THEN 1 ELSE 0 END,
    name ASC,
    email DESC;
```

### Fix 4: Fix UNION ORDER BY

```sql
-- WRONG: Position 4 may not exist
SELECT id, name FROM users
UNION ALL
SELECT id, name FROM admins
ORDER BY 4;

-- RIGHT: Use column name
SELECT id, name FROM users
UNION ALL
SELECT id, name FROM admins
ORDER BY name;
```

### Fix 5: Use aliases for calculated columns

```sql
-- RIGHT: Order by alias
SELECT 
    id,
    name,
    salary * 12 AS annual_salary
FROM employees
ORDER BY annual_salary DESC;
```

## Common Mistakes

- **Using positional ORDER BY for readability** — Column names are clearer and less error-prone.
- **Not updating ORDER BY when SELECT changes** — Always verify position after query changes.
- **Assuming ORDER BY 0 works** — Position numbers start at 1.

## Related Pages

- [SQL Group By Error](sql-group-by-error) — GROUP BY expression issues
- [SQL Column Ambiguous](sql-column-ambiguous) — Ambiguous column references
- [SQL Window Function Error](sql-window-function-error) — Window function issues
