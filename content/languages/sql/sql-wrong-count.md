---
title: "[Solution] SQL Wrong Count Column Fix"
description: "Fix 'Operand should contain 1 column' when COUNT or aggregate returns multiple columns."
languages: ["sql"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

This error occurs when COUNT or another aggregate function is used with multiple columns or a subquery that returns multiple columns. The message reads: `Operand should contain 1 column(s)`.

## What This Error Means

Aggregate functions like COUNT, SUM, and MAX expect a single column expression. Passing multiple columns or a subquery returning multiple columns triggers this error.

## Common Causes

- COUNT used with multiple column names
- Subquery in COUNT returns multiple columns
- Using COUNT(*) with explicit column mixup

## How to Fix

### Fix 1: Count a single column or use COUNT(*)

```sql
-- Wrong
SELECT COUNT(id, name) FROM users;

-- Correct
SELECT COUNT(*) FROM users;
-- or
SELECT COUNT(id) FROM users;
```

### Fix 2: Fix subquery to return single column

```sql
-- Wrong
SELECT COUNT((SELECT id, name FROM users WHERE active = 1)) FROM dual;

-- Correct
SELECT COUNT(*) FROM users WHERE active = 1;
```

### Fix 3: Use separate aggregates

```sql
-- Wrong
SELECT COUNT(id, email) FROM users;

-- Correct
SELECT COUNT(id), COUNT(email) FROM users;
```

## Examples

```sql
SELECT COUNT(id, name) FROM users;
-- ERROR 1124: Operand should contain 1 column(s)
```

## Related Errors

- [GROUP BY Error](group-by-error.md) — aggregation issue
- [Syntax Error](syntax-error.md) — malformed SQL
