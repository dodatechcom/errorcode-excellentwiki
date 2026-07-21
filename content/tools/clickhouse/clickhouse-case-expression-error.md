---
title: "[Solution] ClickHouse Case Expression Error"
description: "Fix ClickHouse CASE expression errors when conditional logic produces type mismatches"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Case Expression Error

CASE expression errors occur when CASE/WHEN produces incompatible types in different branches.

## Common Causes

- Different return types in CASE branches
- WHEN condition returns non-boolean
- Too many nested CASE levels
- Missing ELSE clause with NULL result

## How to Fix

Ensure consistent types:

```sql
SELECT
  CASE status
    WHEN 'active' THEN 'Active'
    WHEN 'inactive' THEN 'Inactive'
    ELSE 'Unknown'
  END AS status_label
FROM my_table;
```

Cast mixed types:

```sql
SELECT
  CASE WHEN amount > 100 THEN toFloat64(amount) ELSE 0.0 END AS safe_amount
FROM orders;
```

## Examples

```sql
SELECT id,
  CASE
    WHEN score >= 90 THEN 'A'
    WHEN score >= 80 THEN 'B'
    WHEN score >= 70 THEN 'C'
    ELSE 'F'
  END AS grade
FROM students;
```
