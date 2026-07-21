---
title: "[Solution] Grafana Dashboard Tooltip Error"
description: "How to fix Grafana tooltip errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Tooltip mode not showing all series
- Tooltip content missing fields

## How to Fix

```json
{
  "options": {
    "tooltip": {"mode": "multi", "sort": "desc"}
  }
}
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/dashboards/uid/UID | jq '.dashboard.panels[0].options.tooltip'
```
