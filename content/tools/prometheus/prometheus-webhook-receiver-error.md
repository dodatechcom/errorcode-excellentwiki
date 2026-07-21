---
title: "[Solution] Prometheus Alertmanager Webhook Receiver Error"
description: "How to fix Alertmanager webhook receiver errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Webhook endpoint URL unreachable
- HTTP timeout when sending notification
- Invalid JSON payload
- Webhook endpoint returning non-2xx status
- TLS certificate verification failure

## How to Fix

Configure webhook receiver:

```yaml
receivers:
  - name: 'webhook'
    webhook_configs:
      - url: 'http://webhook-handler:5001/alerts'
        send_resolved: true
        http_config:
          follow_redirects: true
```

Test webhook endpoint:

```bash
curl -X POST http://webhook-handler:5001/alerts -H 'Content-Type: application/json' -d '{"status":"firing","alerts":[]}'
```

## Examples

```bash
# Check webhook notification logs
curl http://localhost:9093/metrics | grep "alertmanager_notifications_failed_total"

# Test webhook endpoint
curl -v http://webhook-handler:5001/alerts

# View notification errors
amtool --alertmanager.url=http://localhost:9093 silence query
```
