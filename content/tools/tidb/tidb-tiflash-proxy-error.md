---
title: "[Solution] TiDB TiFlash Proxy Error"
description: "How to fix TiDB TiFlash proxy errors"
tools: ["tidb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- TiFlash proxy not running
- Proxy port wrong
- Proxy TLS mismatch

## How to Fix

```bash
curl http://tiflash-host:8123/ping
```

## Examples

```bash
curl http://tiflash-host:9000/ping
```
