---
title: "[Solution] Grafana API Key Expired"
description: "How to fix Grafana API key expiration errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- API key reached max lifetime
- Default expiration policy
- Organization policy enforcing rotation

## How to Fix

```bash
curl -s -H "Authorization: Bearer ADMIN_KEY" http://localhost:3000/api/auth/keys | jq '.[] | {name: .name, expires: .expiration}'
```

## Examples

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer ADMIN_KEY" -d '{"name":"long-lived","role":"Viewer","secondsToLive":31536000}' http://localhost:3000/api/auth/keys
```
