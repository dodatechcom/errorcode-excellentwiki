---
title: "[Solution] TiDB TiFlash Metrics Error"
description: "How to fix TiDB TiFlash metrics errors"
tools: ["tidb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Metrics endpoint not accessible
- Metrics not showing data
- Prometheus not scraping TiFlash

## How to Fix

```bash
curl http://tiflash-host:9000/metrics
```

## Examples

```bash
curl http://tiflash-host:8123/metrics
```
