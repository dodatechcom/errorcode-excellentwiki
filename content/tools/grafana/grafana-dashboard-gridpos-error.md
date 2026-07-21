---
title: "[Solution] Grafana Dashboard GridPos Error"
description: "How to fix Grafana grid position errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Panel gridPos values overlap
- Panel position outside bounds
- Panel height or width zero

## How to Fix

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/dashboards/uid/UID | jq '.dashboard.panels[] | {title: .title, gridPos: .gridPos}'
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/dashboards/uid/UID | jq '.dashboard.panels[] | .gridPos | "\\(.x)x\\(.y) \\(.w)x\\(.h)"'
```
