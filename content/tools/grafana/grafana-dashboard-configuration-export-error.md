---
title: "[Solution] Grafana Dashboard Export Error"
description: "How to fix Grafana dashboard export errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Export format not compatible
- Datasource UIDs not exported
- Variables not included

## How to Fix

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/dashboards/uid/UID | jq '.dashboard' > exported.json
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/dashboards/uid/UID | jq '.dashboard' > dashboard-export.json
```
