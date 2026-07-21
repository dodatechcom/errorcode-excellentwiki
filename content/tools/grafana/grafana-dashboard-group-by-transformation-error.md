---
title: "[Solution] Grafana Dashboard Group By Transform Error"
description: "How to fix Grafana group by transformation errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Group by field not found
- Aggregation function incompatible

## How to Fix

```json
{
  "id": "groupBy",
  "options": {
    "fields": {
      "instance": {"aggregations": [], "operation": "groupById"},
      "Value": {"aggregations": ["mean"], "operation": "aggregate"}
    }
  }
}
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/dashboards/uid/UID | jq '.dashboard.panels[] | .transformations[] | select(.id == "groupBy")'
```
