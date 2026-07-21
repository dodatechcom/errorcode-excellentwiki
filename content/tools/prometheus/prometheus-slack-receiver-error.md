---
title: "[Solution] Prometheus Alertmanager Slack Receiver Error"
description: "How to fix Alertmanager Slack notification errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Slack webhook URL expired or revoked
- Invalid channel name
- Message payload too large
- Slack API rate limit exceeded
- Webhook URL missing or malformed

## How to Fix

Configure Slack receiver:

```yaml
receivers:
  - name: 'slack'
    slack_configs:
      - channel: '#alerts'
        api_url: 'https://hooks.slack.com/services/T00/B00/xxx'
        send_resolved: true
        title: '{{ .GroupLabels.alertname }}'
        text: '{{ range .Alerts }}{{ .Annotations.description }}{{ end }}'
```

Test webhook URL:

```bash
curl -X POST https://hooks.slack.com/services/T00/B00/xxx   -H 'Content-Type: application/json'   -d '{"text":"Test alert notification"}'
```

## Examples

```bash
# Test Slack webhook
curl -X POST https://hooks.slack.com/services/T00/B00/xxx -d '{"text":"Alert test from Prometheus"}'

# Check Slack notification status
curl http://localhost:9093/metrics | grep "alertmanager_notifications_total"
```
