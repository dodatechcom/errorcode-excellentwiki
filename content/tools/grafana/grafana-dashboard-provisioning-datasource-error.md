---
title: "[Solution] Grafana Dashboard Provisioning Datasource Error"
description: "How to fix Grafana provisioning datasource errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Datasource not provisioned before dashboard
- Datasource URL unreachable at provision time

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
