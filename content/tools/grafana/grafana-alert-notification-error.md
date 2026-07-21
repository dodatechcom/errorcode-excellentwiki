---
title: "[Solution] Grafana Alert Notification Error"
description: "How to fix Grafana alert notification delivery errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Notification channel unreachable
- Webhook URL incorrect
- Email server not configured

## How to Fix

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/alert-notifications | jq '.[].name'
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer API_KEY" -d '{"id":1}' http://localhost:3000/api/alert-notifications/test
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/alert-notifications | jq '.[].name'
```
