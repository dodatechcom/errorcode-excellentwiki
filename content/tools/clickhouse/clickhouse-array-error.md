---
title: "[Solution] ClickHouse Array Error"
description: "How to fix ClickHouse Array type errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Array index out of bounds
- Array element type mismatch
- Array too large

## How to Fix

```sql
SELECT arrayElement([1, 2, 3], 2);
```

## Examples

```sql
SELECT arrayPushBack([1, 2], 3), arrayPopFront([1, 2, 3]);
```
