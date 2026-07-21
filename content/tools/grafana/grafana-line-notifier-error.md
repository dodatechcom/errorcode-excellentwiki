---
title: "[Solution] Grafana LINE Notifier Error"
description: "How to fix Grafana LINE notification errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Invalid channel access token
- Channel ID incorrect
- LINE Notify API unreachable

## How to Fix

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer API_KEY" -d '{"name":"line","type":"line","settings":{"token":"TOKEN"}}' http://localhost:3000/api/alert-notifications
```

## Examples

```bash
curl -X POST https://notify-api.line.me/api/notify -H "Authorization: Bearer TOKEN" -d "message=Test from Grafana"
```
