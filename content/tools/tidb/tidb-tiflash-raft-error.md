---
title: "[Solution] TiDB TiFlash Raft Error"
description: "How to fix TiDB TiFlash raft errors"
tools: ["tidb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Raft group not healthy
- Raft leader not elected
- Raft log lag too high

## How to Fix

```sql
SELECT * FROM information_schema.tiflash_replica;
```

## Examples

```sql
SHOW TABLE mytable TIFLASH REPLICA;
```
