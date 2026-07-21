---
title: "[Solution] Grafana Dashboard Ad Hoc Variable Error"
description: "How to fix Grafana ad-hoc filter variable errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Ad-hoc filter datasource mismatch
- Filter keys not available
- Too many filters slowing queries

## How to Fix

```json
{
  "name": "filters",
  "type": "adhoc",
  "datasource": {"type": "prometheus", "uid": "prometheus"}
}
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/dashboards/uid/UID | jq '.dashboard.templating.list[] | select(.type == "adhoc")'
```
