---
title: "[Solution] Grafana Dashboard Version Conflict"
description: "How to fix Grafana dashboard save conflict"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Two users editing simultaneously
- Provisioning overwriting manual edits
- API call with stale version

## How to Fix

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/dashboards/uid/UID | jq '.dashboard.version'
```

## Examples

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer API_KEY" -d '{"dashboard":{"uid":"UID","version":5},"overwrite":true}' http://localhost:3000/api/dashboards/db
```
