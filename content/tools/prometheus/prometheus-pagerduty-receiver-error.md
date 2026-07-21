---
title: "[Solution] Prometheus Alertmanager PagerDuty Receiver Error"
description: "How to fix Alertmanager PagerDuty notification errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Invalid PagerDuty service key
- PagerDuty API endpoint unreachable
- Event payload exceeds size limit
- Service key rotated without updating config

## How to Fix

Configure PagerDuty receiver:

```yaml
receivers:
  - name: 'pagerduty'
    pagerduty_configs:
      - service_key: 'your-pagerduty-integration-key'
        description: '{{ .CommonAnnotations.summary }}'
        details:
          firing: '{{ .Alerts.Firing | len }}'
          resolved: '{{ .Alerts.Resolved | len }}'
```

Verify service key:

```bash
curl -X POST https://events.pagerduty.com/v2/enqueue   -H 'Content-Type: application/json'   -d '{"routing_key":"YOUR_KEY","event_action":"trigger","payload":{"summary":"Test","severity":"critical","source":"prometheus"}}'
```

## Examples

```bash
# Check PagerDuty notification status
curl http://localhost:9093/metrics | grep "pagerduty"

# Test integration
curl -X POST https://events.pagerduty.com/v2/enqueue -d '{"routing_key":"YOUR_KEY","event_action":"trigger","payload":{"summary":"Test alert","severity":"warning","source":"test"}}'
```
