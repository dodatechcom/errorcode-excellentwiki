---
title: "[Solution] TiDB Stale Read Error"
description: "How to fix TiDB stale read errors"
tools: ["tidb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Stale read time too old
- Stale read not supported for query
- GC not cleaned old data

## How to Fix

```sql
SELECT * FROM mytable AS OF TIMESTAMP NOW() - INTERVAL 5 SECOND;
```

## Examples

```sql
SELECT * FROM mytable AS OF TIMESTAMP '2024-01-15 10:00:00';
```
