---
title: "[Solution] Grafana Dashboard Constant Variable Error"
description: "How to fix Grafana constant variable errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Constant variable value not set
- Variable name conflicts with reserved names

## How to Fix

```json
{
  "name": "ENVIRONMENT",
  "type": "constant",
  "query": "production",
  "current": {"text": "production", "value": "production"}
}
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/dashboards/uid/UID | jq '.dashboard.templating.list[] | select(.type == "constant") | {name: .name}'
```
