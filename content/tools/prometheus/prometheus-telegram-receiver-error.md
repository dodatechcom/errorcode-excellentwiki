---
title: "[Solution] Prometheus Alertmanager Telegram Receiver Error"
description: "How to fix Alertmanager Telegram notification errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Invalid bot token
- Chat ID not found or bot not added to group
- Telegram API rate limit exceeded
- Message too long for Telegram limit

## How to Fix

Configure Telegram receiver:

```yaml
receivers:
  - name: 'telegram'
    telegram_configs:
      - bot_token: 'your-bot-token'
        chat_id: -1001234567890
        parse_mode: 'HTML'
        message: '{{ .CommonAnnotations.summary }}'
```

## Examples

```bash
# Get bot updates to find chat ID
curl "https://api.telegram.org/botYOUR_TOKEN/getUpdates"

# Send test message
curl -X POST "https://api.telegram.org/botYOUR_TOKEN/sendMessage"   -d "chat_id=-1001234567890&text=Test alert from Prometheus"
```
