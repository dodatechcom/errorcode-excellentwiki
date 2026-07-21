---
title: "[Solution] Grafana Dashboard Frontend Error"
description: "How to fix Grafana frontend rendering errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Browser cache corrupted
- JavaScript disabled
- Frontend build corrupted

## How to Fix

```bash
sudo systemctl restart grafana-server
```

## Examples

```bash
curl -s http://localhost:3000/api/frontend/settings | jq '.buildInfo.version'
```
