---
title: "[Solution] TiDB TiFlash Compaction Error"
description: "How to fix TiDB TiFlash compaction errors"
tools: ["tidb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Compaction lag
- Compaction failing
- Too many delta layers

## How to Fix

```sql
SELECT * FROM information_schema.tiflash_replica;
```

## Examples

```bash
curl http://tiflash-host:9000/debug/pprof
```
