---
title: "[Solution] TiDB TiFlash Scaling Error"
description: "How to fix TiDB TiFlash scaling errors"
tools: ["tidb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- TiFlash scaling taking too long
- TiFlash replica rebalancing failing
- TiFlash node not joining cluster

## How to Fix

```sql
ALTER TABLE mytable SET TIFLASH REPLICA 1;
```

## Examples

```sql
SELECT * FROM information_schema.tiflash_replica;
```
