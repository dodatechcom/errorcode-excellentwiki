---
title: "[Solution] Grafana Dashboard Threshold Override Error"
description: "How to fix Grafana threshold override errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Threshold steps incorrectly ordered
- Override threshold not applying
- Step value null position wrong

## How to Fix

```json
{
  "fieldConfig": {
    "defaults": {
      "thresholds": {
        "mode": "absolute",
        "steps": [
          {"color": "green", "value": null},
          {"color": "yellow", "value": 50},
          {"color": "red", "value": 80}
        ]
      }
    }
  }
}
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/dashboards/uid/UID | jq '.dashboard.panels[0].fieldConfig.defaults.thresholds'
```
