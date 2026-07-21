---
title: "[Solution] Prometheus Alertmanager Discord Receiver Error"
description: "How to fix Alertmanager Discord notification errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Invalid Discord webhook URL
- Webhook URL expired or deleted
- Message embeds exceeding Discord limits
- Bot permissions insufficient

## How to Fix

Configure Discord receiver:

```yaml
receivers:
  - name: 'discord'
    discord_configs:
      - api_url: 'https://discord.com/api/webhooks/YOUR_WEBHOOK'
        message: '{{ .CommonAnnotations.summary }}'
```

## Examples

```bash
# Test Discord webhook
curl -X POST https://discord.com/api/webhooks/YOUR_WEBHOOK   -H "Content-Type: application/json"   -d '{"content":"Test alert from Prometheus"}'
```
