---
title: "[Solution] Grafana Dashboard Annotation Query Error"
description: "How to fix Grafana annotation query errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Annotation datasource not configured
- Query returning no data
- Too many annotations cluttering graph

## How to Fix

```json
{
  "annotations": {
    "list": [{
      "name": "Deployments",
      "datasource": {"type": "grafana", "uid": "-- Grafana --"},
      "enable": true,
      "query": "deployments"
    }]
  }
}
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/dashboards/uid/UID | jq '.dashboard.annotations.list[] | {name: .name, query: .query}'
```
