---
title: "[Solution] ClickHouse Division by Zero Error"
description: "Fix ClickHouse division by zero errors when arithmetic operations encounter zero denominators"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Division by Zero Error

Division by zero errors occur when a SQL expression attempts to divide by zero.

## Common Causes

- Aggregate result returning zero for denominator
- Column value is zero in computed expression
- Missing WHERE clause filtering zero values
- Division in CASE statement without zero check

## How to Fix

Use divideOrZero function:

```sql
SELECT id, divideOrZero(numerator, denominator) AS result FROM my_table;
```

Filter zero values:

```sql
SELECT id, value / denominator AS result
FROM my_table WHERE denominator != 0;
```

Use conditional division:

```sql
SELECT id,
  CASE WHEN denominator > 0 THEN value / denominator ELSE 0 END AS result
FROM my_table;
```

## Examples

```sql
SELECT id, divideOrZero(total, count) AS avg_value FROM metrics;
```
