---
title: "[Solution] Grafana Dashboard Grafana.com Error"
description: "How to fix Grafana grafana.com integration errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Grafana.com account not linked
- Plugin marketplace unreachable

## How to Fix

```bash
curl -s https://grafana.com/api/health | jq .
```

## Examples

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer API_KEY" -d '{"dashboard":null,"overwrite":false}' http://localhost:3000/api/dashboards/import/1
```
