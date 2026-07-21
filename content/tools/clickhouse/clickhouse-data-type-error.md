---
title: "[Solution] ClickHouse Data Type Error"
description: "How to fix ClickHouse data type errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Implicit type conversion failure
- Overflow during cast
- Wrong data type for column

## How to Fix

```sql
SELECT CAST('123' AS UInt64);
```

## Examples

```sql
SELECT toUInt64('123'), toFloat64('3.14'), toString(123);
```
