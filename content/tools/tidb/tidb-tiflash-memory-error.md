---
title: "[Solution] TiDB TiFlash Memory Error"
description: "How to fix TiDB TiFlash memory errors"
tools: ["tidb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- TiFlash OOM
- TiFlash memory limit too low
- TiFlash query using too much memory

## How to Fix

```ini
[flash]
tiflash_task_pool_size = 16
```

## Examples

```bash
free -h
```
