---
title: "[Solution] TiDB TiFlash Schema Error"
description: "How to fix TiDB TiFlash schema errors"
tools: ["tidb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Schema not synced to TiFlash
- Schema version mismatch
- Schema change not propagated

## How to Fix

```sql
ALTER TABLE mytable SET TIFLASH REPLICA 1;
```

## Examples

```sql
SELECT * FROM information_schema.tiflash_replica;
```
