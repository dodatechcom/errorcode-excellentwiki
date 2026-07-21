---
title: "[Solution] ClickHouse DateTime Type Error"
description: "How to fix ClickHouse DateTime type errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- DateTime format wrong
- DateTime timezone wrong
- DateTime overflow

## How to Fix

```sql
SELECT toDateTime('2024-01-15 10:30:00');
```

## Examples

```sql
SELECT now(), toStartOfHour(now()), toStartOfDay(now());
```
