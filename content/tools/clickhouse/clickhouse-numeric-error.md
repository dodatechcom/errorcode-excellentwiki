---
title: "[Solution] ClickHouse Numeric Overflow Error"
description: "How to fix ClickHouse numeric overflow errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- UInt8 overflow (max 255)
- Int8 underflow (min -128)
- Float precision loss

## How to Fix

```sql
SELECT toUInt8(256);
```

## Examples

```sql
SELECT toUInt8(255), toInt8(-128), toFloat64(1.0/3.0);
```
