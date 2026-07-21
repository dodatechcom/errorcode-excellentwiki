---
title: "[Solution] Grafana Dashboard Calculate Field Error"
description: "How to fix Grafana calculate field transformation errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Field names in formula not found
- Divide by zero error
- Numeric conversion failing

## How to Fix

```json
{
  "id": "calculateField",
  "options": {
    "mode": "binaryOperation",
    "binaryOperation": {
      "leftField": "requests",
      "operator": "/",
      "rightField": "errors"
    }
  }
}
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/dashboards/uid/UID | jq '.dashboard.panels[] | .transformations[] | select(.id == "calculateField")'
```
