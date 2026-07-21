---
title: "[Solution] Grafana Dashboard Delete Error"
description: "How to fix Grafana dashboard deletion errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Dashboard is provisioned
- Insufficient permissions
- Dashboard referenced by alert rules

## How to Fix

```bash
curl -X DELETE -H "Authorization: Bearer ADMIN_KEY" http://localhost:3000/api/dashboards/db/DASHBOARD_UID
```

## Examples

```bash
curl -s -H "Authorization: Bearer ADMIN_KEY" http://localhost:3000/api/search?query=old | jq '.[].uid'
curl -X DELETE -H "Authorization: Bearer ADMIN_KEY" http://localhost:3000/api/dashboards/db/OLD_UID
```
