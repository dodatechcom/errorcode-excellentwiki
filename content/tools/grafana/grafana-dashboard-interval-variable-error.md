---
title: "[Solution] Grafana Dashboard Interval Variable Error"
description: "How to fix Grafana interval variable errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Interval auto calculation wrong
- Interval not matching query step
- Selected interval not valid

## How to Fix

```json
{
  "name": "interval",
  "type": "interval",
  "query": "1m,5m,15m,30m,1h",
  "auto": true,
  "auto_min": "1m"
}
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/dashboards/uid/UID | jq '.dashboard.templating.list[] | select(.type == "interval") | {query: .query, auto: .auto}'
```
