---
title: "[Solution] Grafana Dashboard Value Mapping Error"
description: "How to fix Grafana value mapping errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Value map not matching returned values
- Range mapping boundaries incorrect
- Special value mapping not triggered

## How to Fix

```json
{
  "fieldConfig": {
    "defaults": {
      "mappings": [
        {"type": "value", "options": {"0": {"text": "DOWN"}, "1": {"text": "UP"}}}
      ]
    }
  }
}
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/dashboards/uid/UID | jq '.dashboard.panels[0].fieldConfig.defaults.mappings'
```
