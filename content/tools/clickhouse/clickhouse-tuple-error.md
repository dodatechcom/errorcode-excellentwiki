---
title: "[Solution] ClickHouse Tuple Error"
description: "How to fix ClickHouse Tuple type errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Tuple element count mismatch
- Tuple element type mismatch
- Nested tuple issues

## How to Fix

```sql
SELECT (1, 'hello', 3.14);
```

## Examples

```sql
SELECT tupleElement((1, 'hello', 3.14), 2);
```
