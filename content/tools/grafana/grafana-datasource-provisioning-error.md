---
title: "[Solution] Grafana Datasource Provisioning Error"
description: "How to fix Grafana datasource provisioning errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Datasource URL unreachable during provisioning
- Authentication credentials wrong
- Duplicate datasource names

## How to Fix

```yaml
apiVersion: 1
datasources:
  - name: Prometheus
    type: prometheus
    access: proxy
    url: http://prometheus:9090
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/datasources | jq '.[].name'
```
