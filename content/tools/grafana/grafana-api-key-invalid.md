---
title: "[Solution] Grafana API Key Invalid"
description: "How to fix Grafana API key authentication errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- API key deleted or revoked
- API key expired
- Wrong API key format

## How to Fix

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer ADMIN_KEY" -d '{"name":"my-key","role":"Viewer"}' http://localhost:3000/api/auth/keys
```

## Examples

```bash
curl -s -H "Authorization: Bearer ADMIN_KEY" http://localhost:3000/api/auth/keys | jq '.[].name'
```
