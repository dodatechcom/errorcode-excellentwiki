---
title: "[Solution] TiDB TiFlash Replica Error"
description: "How to fix TiDB TiFlash replica errors"
tools: ["tidb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Replica count wrong
- Replica not syncing
- Replica lag too high

## How to Fix

```sql
ALTER TABLE mytable SET TIFLASH REPLICA 1;
```

## Examples

```sql
SELECT * FROM information_schema.tiflash_replica;
```
