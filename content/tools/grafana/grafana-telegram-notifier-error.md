---
title: "[Solution] Grafana Telegram Notifier Error"
description: "How to fix Grafana Telegram notification errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Invalid bot token
- Chat ID not found
- Bot not added to group

## How to Fix

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer API_KEY" -d '{"name":"telegram","type":"telegram","settings":{"bottoken":"TOKEN","chatid":"-1001234567890"}}' http://localhost:3000/api/alert-notifications
```

## Examples

```bash
curl -X POST "https://api.telegram.org/botYOUR_TOKEN/sendMessage" -d "chat_id=-1001234567890&text=Test alert"
```
