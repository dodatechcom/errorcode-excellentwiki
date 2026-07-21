---
title: "[Solution] Grafana Dashboard Legend Error"
description: "How to fix Grafana legend errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Legend showing raw label values
- Legend table not displaying columns
- Legend position overlapping panel

## How to Fix

```json
{
  "options": {
    "legend": {
      "displayMode": "table",
      "placement": "right",
      "calcs": ["mean", "max"]
    }
  }
}
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/dashboards/uid/UID | jq '.dashboard.panels[0].options.legend'
```
