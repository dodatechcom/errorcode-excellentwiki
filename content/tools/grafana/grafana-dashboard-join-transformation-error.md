---
title: "[Solution] Grafana Dashboard Join Transform Error"
description: "How to fix Grafana join transformation errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Join field names not matching
- Outer join producing too many rows

## How to Fix

```json
{
  "id": "joinByField",
  "options": {"byField": "Time", "mode": "outer"}
}
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/dashboards/uid/UID | jq '.dashboard.panels[] | .transformations[] | select(.id == "joinByField")'
```
