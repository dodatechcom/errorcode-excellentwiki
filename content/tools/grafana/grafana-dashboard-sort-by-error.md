---
title: "[Solution] Grafana Dashboard Sort By Transform Error"
description: "How to fix Grafana sort by transformation errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Sort field not found
- Sort direction not applied

## How to Fix

```json
{
  "id": "sortBy",
  "options": {
    "sort": [{"field": "Value", "desc": true}]
  }
}
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/dashboards/uid/UID | jq '.dashboard.panels[] | .transformations[] | select(.id == "sortBy")'
```
