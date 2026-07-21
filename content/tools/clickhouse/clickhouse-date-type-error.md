---
title: "[Solution] ClickHouse Date Type Error"
description: "How to fix ClickHouse Date type errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Date format not parsing
- Date out of range
- Timezone mismatch

## How to Fix

```sql
SELECT toDate('2024-01-15');
```

## Examples

```sql
SELECT today(), yesterday(), toDayOfWeek(now());
```
