---
title: "[Solution] Prometheus Alertmanager VictorOps Receiver Error"
description: "How to fix Alertmanager VictorOps notification errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Invalid VictorOps API key
- Routing key misconfigured
- VictorOps API endpoint unreachable
- Message format incompatible

## How to Fix

Configure VictorOps receiver:

```yaml
receivers:
  - name: 'victorops'
    victorops_configs:
      - api_key: 'your-victorops-api-key'
        routing_key: 'operations'
        message_type: '{{ if eq .CommonLabels.severity "critical" }}CRITICAL{{ else }}WARNING{{ end }}'
        state_message: '{{ .CommonAnnotations.summary }}'
```

## Examples

```bash
# Test VictorOps API
curl -X POST https://alert.victorops.com/integrations/generic/20131114/alert   -H "Content-Type: application/json"   -d '{"message_type":"CRITICAL","routing_key":"operations","state_message":"Test alert","entity_id":"test-123"}'
```
