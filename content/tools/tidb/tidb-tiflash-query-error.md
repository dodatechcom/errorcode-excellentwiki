---
title: "[Solution] TiDB TiFlash Query Error"
description: "How to fix TiDB TiFlash query errors"
tools: ["tidb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Query not using TiFlash replica
- TiFlash query timeout
- TiFlash query plan wrong

## How to Fix

```sql
SELECT /*+ READ_FROM_STORAGE(TIFLASH[mytable]) */ * FROM mytable;
```

## Examples

```sql
EXPLAIN SELECT * FROM mytable;
```
