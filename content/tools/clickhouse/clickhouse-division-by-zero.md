---
title: "[Solution] ClickHouse Division By Zero Error"
description: "How to fix ClickHouse division by zero errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Denominator evaluates to zero
- Empty group in division
- NULL in denominator

## How to Fix

Guard against zero:

```sql
SELECT if(denom = 0, 0, numer / denom) FROM my_table;
SELECT numer / nullIf(denom, 0) FROM my_table;
```

## Examples

```sql
SELECT if(count = 0, 0, sum / count) AS avg_val FROM my_table;
SELECT sum(value) / nullIf(count(value), 0) FROM my_table;
```
