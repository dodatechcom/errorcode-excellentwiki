---
title: "[Solution] ClickHouse Map Error"
description: "How to fix ClickHouse Map type errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Map key type wrong
- Map value type mismatch
- Map too large

## How to Fix

```sql
SELECT map('key1', 1, 'key2', 2);
```

## Examples

```sql
SELECT mapKeys(map('a', 1, 'b', 2)), mapValues(map('a', 1, 'b', 2));
```
