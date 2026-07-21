---
title: "[Solution] TiDB TiFlash Config Error"
description: "How to fix TiDB TiFlash configuration errors"
tools: ["tidb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Config file syntax error
- Config parameter wrong
- Config requires restart

## How to Fix

```bash
cat /data/tiflash/tiflash.toml | grep -v '^#'
```

## Examples

```bash
tiflash-server --config-file /data/tiflash/tiflash.toml
```
