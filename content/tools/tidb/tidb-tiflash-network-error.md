---
title: "[Solution] TiDB TiFlash Network Error"
description: "How to fix TiDB TiFlash network errors"
tools: ["tidb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- TiFlash not reachable from TiDB
- Network latency too high
- Network partition

## How to Fix

```bash
nc -zv tiflash-host 9000
```

## Examples

```bash
ping tiflash-host
```
