---
title: "[Solution] Grafana Dashboard TextBox Variable Error"
description: "How to fix Grafana textbox variable errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Textbox input not sanitizing special characters
- Empty textbox value causing query failure

## How to Fix

```json
{
  "name": "search",
  "type": "textbox",
  "query": "default-value"
}
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/dashboards/uid/UID | jq '.dashboard.templating.list[] | select(.type == "textbox") | {name: .name}'
```
