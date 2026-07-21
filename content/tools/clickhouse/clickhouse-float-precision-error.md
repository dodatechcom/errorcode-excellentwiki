---
title: "[Solution] ClickHouse Float Precision Error"
description: "Fix ClickHouse floating point precision errors when decimal values lose accuracy"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Float Precision Error

Float precision errors occur when ClickHouse floating point operations produce unexpected rounding.

## Common Causes

- Float32 precision insufficient for financial data
- Division producing repeating decimals
- Comparing float values for equality
- Aggregate functions accumulating rounding errors

## How to Fix

Use Decimal type for precision:

```sql
CREATE TABLE prices (amount Decimal64(2)) ENGINE = MergeTree() ORDER BY id;
```

Round explicitly:

```sql
SELECT round(amount, 2) AS rounded_amount FROM my_table;
```

Compare with epsilon:

```sql
SELECT * FROM my_table WHERE abs(value - 1.0) < 0.0001;
```

## Examples

```sql
SELECT id, toDecimal64(amount, 2) AS precise_amount FROM orders;
```
