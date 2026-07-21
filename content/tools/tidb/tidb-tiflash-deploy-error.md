---
title: "[Solution] TiDB TiFlash Deploy Error"
description: "How to fix TiDB TiFlash deployment errors"
tools: ["tidb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- TiFlash not registered with PD
- TiFlash storage not initialized
- TiFlash config wrong

## How to Fix

```bash
tiflash-server --config-file /data/tiflash/tiflash.toml
```

## Examples

```bash
tiup ctl pd-ctl stores
```
