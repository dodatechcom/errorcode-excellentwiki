---
title: "[Solution] Grafana Dashboard Unit Error"
description: "How to fix Grafana panel unit errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Unit not matching data type
- Custom unit not displaying correctly

## How to Fix

```json
{
  "fieldConfig": {
    "defaults": {"unit": "bytes"}
  }
}
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/dashboards/uid/UID | jq '.dashboard.panels[].fieldConfig.defaults.unit'
```
