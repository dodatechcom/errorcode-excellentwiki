---
title: "[Solution] Grafana Dashboard Reduce Transform Error"
description: "How to fix Grafana reduce transformation errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Reduce operation on non-numeric data
- Empty input producing NaN

## How to Fix

```json
{
  "id": "reduce",
  "options": {
    "mode": "reduceFields",
    "reducers": ["lastNotNull", "mean", "max"]
  }
}
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/dashboards/uid/UID | jq '.dashboard.panels[] | .transformations[] | select(.id == "reduce")'
```
