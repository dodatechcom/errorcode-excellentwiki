---
title: "[Solution] Grafana Dashboard Link Error"
description: "How to fix Grafana dashboard link errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Link pointing to wrong UID
- Variable not interpolated in link URL
- Link type incorrect

## How to Fix

```json
{
  "links": [{
    "title": "Overview",
    "type": "dashboards",
    "tags": ["overview"]
  }]
}
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/dashboards/uid/UID | jq '.dashboard.links[] | {title: .title, type: .type}'
```
