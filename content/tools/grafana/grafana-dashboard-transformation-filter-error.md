---
title: "[Solution] Grafana Dashboard Transform Filter Error"
description: "How to fix Grafana transformation filter errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Filter condition returning no rows
- Rename mapping not matching fields

## How to Fix

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/dashboards/uid/UID | jq '.dashboard.panels[0].transformations[]'
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/dashboards/uid/UID | jq '.dashboard.panels[] | {title: .title, transformations: (.transformations | length)}'
```
