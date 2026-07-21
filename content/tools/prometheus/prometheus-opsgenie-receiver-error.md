---
title: "[Solution] Prometheus Alertmanager OpsGenie Receiver Error"
description: "How to fix Alertmanager OpsGenie notification errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Invalid OpsGenie API key
- API endpoint misconfigured
- Message priority not set correctly
- Teams or responders not found in OpsGenie

## How to Fix

Configure OpsGenie receiver:

```yaml
receivers:
  - name: 'opsgenie'
    opsgenie_configs:
      - api_key: 'your-opsgenie-api-key'
        message: '{{ .CommonAnnotations.summary }}'
        description: '{{ .CommonAnnotations.description }}'
        teams: 'operations'
        priority: '{{ if eq .CommonLabels.severity "critical" }}P1{{ else }}P2{{ end }}'
```

## Examples

```bash
# Test OpsGenie API
curl -X POST https://api.opsgenie.com/v2/alerts   -H "Authorization: GenieKey YOUR_API_KEY"   -H "Content-Type: application/json"   -d '{"message":"Test alert","alias":"test-alert","priority":"P2"}'
```
