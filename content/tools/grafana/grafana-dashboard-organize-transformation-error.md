---
title: "[Solution] Grafana Dashboard Organize Transform Error"
description: "How to fix Grafana organize transformation errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Hide operation not removing field
- Rename not applying to correct field

## How to Fix

```json
{
  "id": "organize",
  "options": {
    "excludeByName": {"Time": true},
    "renameByName": {"Value": "Response Time"}
  }
}
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/dashboards/uid/UID | jq '.dashboard.panels[] | .transformations[] | select(.id == "organize")'
```
