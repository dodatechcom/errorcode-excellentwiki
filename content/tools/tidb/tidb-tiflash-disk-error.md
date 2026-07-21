---
title: "[Solution] TiDB TiFlash Disk Error"
description: "How to fix TiDB TiFlash disk errors"
tools: ["tidb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- TiFlash disk full
- TiFlash data directory not writable
- TiFlash space reclaimed after GC

## How to Fix

```bash
du -sh /data/tiflash/
```

## Examples

```bash
ls -la /data/tiflash/
```
