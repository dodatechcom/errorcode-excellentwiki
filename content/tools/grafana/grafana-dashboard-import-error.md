---
title: "[Solution] Grafana Dashboard Import Error"
description: "How to fix Grafana dashboard import errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Dashboard JSON invalid
- Datasource references not matching
- Plugin dependencies missing

## How to Fix

```bash
python3 -m json.tool dashboard.json > /dev/null && echo "Valid JSON"
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer API_KEY" -d @dashboard.json http://localhost:3000/api/dashboards/db
```

## Examples

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer API_KEY" -d '{"dashboard":{"id":null},"overwrite":true}' http://localhost:3000/api/dashboards/import
```
