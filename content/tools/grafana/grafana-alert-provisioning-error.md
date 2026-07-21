---
title: "[Solution] Grafana Alert Provisioning Error"
description: "How to fix Grafana alert provisioning errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Alert rule references non-existent datasource
- Invalid query in alert rule
- Notification channel not provisioned

## How to Fix

```yaml
apiVersion: 1
groups:
  - orgId: 1
    name: Example
    folder: Alerting
    interval: 1m
    rules:
      - uid: alert-1
        title: High Error Rate
        condition: C
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/v1/provisioning/alert-rules | jq '.[].title'
```
