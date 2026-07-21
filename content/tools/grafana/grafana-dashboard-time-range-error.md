---
title: "[Solution] Grafana Dashboard Time Range Error"
description: "How to fix Grafana time range errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Time range not matching data retention
- Relative time range showing no data
- Time zone conversion wrong

## How to Fix

```json
{
  "time": {
    "from": "now-6h",
    "to": "now",
    "refresh_intervals": ["5s", "10s", "30s", "1m"]
  },
  "timezone": "browser"
}
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/dashboards/uid/UID | jq '.dashboard.time'
```
