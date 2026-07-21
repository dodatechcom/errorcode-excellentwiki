---
title: "[Solution] Grafana Dashboard API Key Scopes Error"
description: "How to fix Grafana API key scope errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- API key scope too restricted
- Service account token missing required role

## How to Fix

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer ADMIN_KEY" -d '{"name":"read-only","role":"Viewer"}' http://localhost:3000/api/auth/keys
```

## Examples

```bash
curl -s -H "Authorization: Bearer ADMIN_KEY" http://localhost:3000/api/auth/keys | jq '.[] | {name: .name, role: .role}'
```
