---
title: "[Solution] Grafana Dashboard Provisioning Error"
description: "How to fix Grafana dashboard provisioning failures"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Dashboard JSON syntax error
- Missing required fields
- Datasource references not matching

## How to Fix

```yaml
apiVersion: 1
providers:
  - name: 'default'
    orgId: 1
    folder: 'Monitoring'
    type: file
    options:
      path: /var/lib/grafana/dashboards
```

## Examples

```bash
python3 -m json.tool /var/lib/grafana/dashboards/my-dashboard.json
```
