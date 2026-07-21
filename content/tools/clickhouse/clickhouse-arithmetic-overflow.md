---
title: "[Solution] ClickHouse Arithmetic Overflow Error"
description: "How to fix ClickHouse arithmetic overflow errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Integer overflow in calculations
- UInt32 value exceeds max
- Float precision loss

## How to Fix

Use larger types:

```sql
SELECT toUInt64(large_value) * large_multiplier;
```

Check overflow:

```sql
SELECT toUInt32(4294967295) + 1;  -- overflow!
SELECT toUInt64(4294967295) + 1;  -- OK
```

## Examples

```sql
SELECT max(toUInt32(id)) FROM my_table;
SELECT toInt128(value) * multiplier FROM my_table;
```
