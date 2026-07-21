---
title: "[Solution] Grafana Webhook Notifier Error"
description: "How to fix Grafana webhook notification errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Webhook URL unreachable
- HTTP timeout during notification
- Invalid JSON payload

## How to Fix

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer API_KEY" -d '{"name":"webhook","type":"webhook","settings":{"url":"http://handler:5001/alerts","httpMethod":"POST"}}' http://localhost:3000/api/alert-notifications
```

## Examples

```bash
curl -X POST http://handler:5001/alerts -H 'Content-Type: application/json' -d '{"title":"Test","state":"alerting","message":"Test"}'
```
