---
title: "[Solution] Grafana Dashboard Data Link Error"
description: "How to fix Grafana data link errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Data link URL not interpolating variables
- Data link title empty
- Target blank not opening new tab

## How to Fix

```json
{
  "links": [{
    "title": "Drilldown",
    "url": "/d/other?var-instance=${__value.raw}",
    "targetBlank": true
  }]
}
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/dashboards/uid/UID | jq '.dashboard.panels[0].links[]'
```
