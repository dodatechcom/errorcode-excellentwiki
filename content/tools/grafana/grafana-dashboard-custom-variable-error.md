---
title: "[Solution] Grafana Dashboard Custom Variable Error"
description: "How to fix Grafana custom variable errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Custom values not matching format
- Multi-value selection not working
- All value option not configured

## How to Fix

```json
{
  "name": "severity",
  "type": "custom",
  "query": "info,warning,error,critical"
}
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/dashboards/uid/UID | jq '.dashboard.templating.list[] | select(.type == "custom") | {name: .name}'
```
