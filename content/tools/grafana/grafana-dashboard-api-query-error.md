---
title: "[Solution] Grafana Dashboard API Query Error"
description: "How to fix Grafana API query errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Query endpoint incorrect
- Query body malformed
- Datasource UID wrong

## How to Fix

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer API_KEY" -d '{"queries":[{"refId":"A","datasource":{"type":"prometheus","uid":"prometheus"},"expr":"up"}],"from":"now-1h","to":"now"}' http://localhost:3000/api/ds/query
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" "http://localhost:3000/api/datasources/uid/prometheus/health" | jq '.status'
```
