---
title: "[Solution] Grafana Discord Notifier Error"
description: "How to fix Grafana Discord notification errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Invalid Discord webhook URL
- Webhook URL expired
- Bot not present in channel

## How to Fix

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer API_KEY" -d '{"name":"discord","type":"discord","settings":{"url":"https://discord.com/api/webhooks/YOUR_WEBHOOK"}}' http://localhost:3000/api/alert-notifications
```

## Examples

```bash
curl -X POST https://discord.com/api/webhooks/YOUR_WEBHOOK -H "Content-Type: application/json" -d '{"content":"Test alert"}'
```
