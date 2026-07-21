---
title: "[Solution] Grafana Datasource Not Found"
description: "How to fix Grafana datasource not found errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Datasource deleted from Grafana
- Wrong datasource UID in panel
- Datasource provisioned under different org

## How to Fix

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/datasources | jq '.[].name'
```

## Examples

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer API_KEY" -d '{"name":"Prometheus","type":"prometheus","url":"http://prometheus:9090","access":"proxy"}' http://localhost:3000/api/datasources
```
