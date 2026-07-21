---
title: "[Solution] Grafana Dashboard Embed Error"
description: "How to fix Grafana dashboard embed errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Embedding disabled in configuration
- CSP blocking iframe
- Cookie SameSite blocking session

## How to Fix

```ini
[security]
allow_embedding = true
cookie_samesite = none
cookie_secure = true
```

## Examples

```bash
curl -s http://localhost:3000/api/frontend/settings | jq '.allowEmbedding'
```
