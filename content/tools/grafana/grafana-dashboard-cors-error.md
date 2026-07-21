---
title: "[Solution] Grafana Dashboard CORS Error"
description: "How to fix Grafana CORS errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- CORS not configured
- Dashboard embed blocked by browser
- Iframe src not whitelisted

## How to Fix

```ini
[security]
allow_embedding = true
```

## Examples

```bash
curl -I -H "Origin: http://other.com" http://localhost:3000/api/health | grep -i access-control
```
