---
title: "[Solution] Grafana Row Repeat Error"
description: "How to fix Grafana row repeat errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Repeat variable not defined
- Variable values empty
- Row not configured for repeat

## How to Fix

```json
{
  "type": "row",
  "repeat": "instance"
}
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/dashboards/uid/UID | jq '.dashboard.panels[] | select(.repeat != null) | {title: .title, repeat: .repeat}'
```
