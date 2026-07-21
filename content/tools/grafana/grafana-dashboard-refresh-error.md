---
title: "[Solution] Grafana Dashboard Auto Refresh Error"
description: "How to fix Grafana auto refresh errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Auto refresh interval not configured
- Refresh causing excessive queries

## How to Fix

```json
{
  "time": {
    "refresh_intervals": ["5s", "10s", "30s", "1m", "5m"]
  }
}
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/dashboards/uid/UID | jq '.dashboard.time.refresh_intervals'
```
