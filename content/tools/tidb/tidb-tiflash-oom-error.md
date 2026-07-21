---
title: "[Solution] TiDB TiFlash OOM Error"
description: "How to fix TiDB TiFlash out of memory errors"
tools: ["tidb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- TiFlash OOM
- Query using too much memory
- Memory limit too low

## How to Fix

```ini
[flash]
tiflash_task_pool_size = 16
```

## Examples

```bash
free -h
```
