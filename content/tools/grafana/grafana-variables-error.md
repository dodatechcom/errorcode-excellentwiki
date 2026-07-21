---
title: "[Solution] Grafana Template Variables Error"
description: "How to fix Grafana variable errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Variable query returning empty results
- Variable values not updating
- Cross-variable dependency not configured

## How to Fix

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/dashboards/uid/UID | jq '.dashboard.templating.list[] | {name: .name, query: .query}'
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" "http://localhost:3000/api/datasources/proxy/ABC123/api/v1/label/__name__/values" | jq '.data'
```
