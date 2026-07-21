---
title: "[Solution] Grafana Dashboard Screenshot Error"
description: "How to fix Grafana dashboard screenshot errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Screenshot service not configured
- Dashboard too large for screenshot
- Authentication failing for render endpoint

## How to Fix

```ini
[rendering]
renderer = plugin
concurrent_render_request_limit = 4
```

## Examples

```bash
curl -H "Authorization: Bearer API_KEY" "http://localhost:3000/render/d/UID?orgId=1&width=1920&height=1080&scale=2" -o screenshot.png
```
