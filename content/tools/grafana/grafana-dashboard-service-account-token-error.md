---
title: "[Solution] Grafana Dashboard Service Account Token Error"
description: "How to fix Grafana service account token errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Service account does not exist
- Token rotation not configured
- Token expired

## How to Fix

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer ADMIN_KEY" -d '{"name":"dashboard-automation","role":"Editor"}' http://localhost:3000/api/serviceaccounts
```

## Examples

```bash
curl -s -H "Authorization: Bearer ADMIN_KEY" http://localhost:3000/api/serviceaccounts | jq '.items[].name'
```
