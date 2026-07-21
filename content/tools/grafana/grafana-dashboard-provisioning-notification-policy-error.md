---
title: "[Solution] Grafana Dashboard Provisioning Notification Policy Error"
description: "How to fix Grafana provisioning notification policy errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Notification policy tree malformed
- Route not matching alert labels

## How to Fix

```yaml
apiVersion: 1
policies:
  - orgId: 1
    receiver: default
    group_by: ['alertname', 'severity']
    group_wait: 30s
    group_interval: 5m
    repeat_interval: 4h
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/v1/provisioning/policies | jq '.'
```
