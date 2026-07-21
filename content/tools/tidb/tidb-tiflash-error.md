---
title: "[Solution] TiDB TiFlash Error"
description: "How to fix TiDB TiFlash errors"
tools: ["tidb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- TiFlash replica not available
- TiFlash not synced
- TiFlash query failing

## How to Fix

```sql
ALTER TABLE mytable SET TIFLASH REPLICA 1;
```

## Examples

```sql
SELECT * FROM information_schema.tiflash_replica;
```
