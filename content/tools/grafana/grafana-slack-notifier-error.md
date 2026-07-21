---
title: "[Solution] Grafana Slack Notifier Error"
description: "How to fix Grafana Slack notification errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Slack webhook URL revoked
- Channel name incorrect
- Message format exceeding limits

## How to Fix

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer API_KEY" -d '{"name":"slack","type":"slack","settings":{"url":"https://hooks.slack.com/services/T00/B00/xxx","recipient":"#alerts"}}' http://localhost:3000/api/alert-notifications
```

## Examples

```bash
curl -X POST https://hooks.slack.com/services/T00/B00/xxx -H 'Content-Type: application/json' -d '{"text":"Test from Grafana"}'
```
