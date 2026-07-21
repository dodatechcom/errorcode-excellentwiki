---
title: "[Solution] Grafana Dashboard Datasource Migration Error"
description: "How to fix Grafana datasource migration errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Datasource UIDs changed after migration
- Old datasource references in panels

## How to Fix

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/dashboards/uid/UID | jq '.dashboard.panels[].datasource | select(.uid == null)'
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/datasources | jq '.[] | {name: .name, uid: .uid}'
```
