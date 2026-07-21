---
title: "[Solution] Grafana Dashboard Render Error"
description: "How to fix Grafana dashboard render errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Image renderer plugin missing
- Dashboard too complex for timeout
- Font rendering issues

## How to Fix

```bash
grafana-cli plugins install grafana-image-renderer
sudo systemctl restart grafana-server
```

## Examples

```bash
curl -H "Authorization: Bearer API_KEY" "http://localhost:3000/render/d/UID?orgId=1&width=1200&height=600" -o dashboard.png
```
