---
title: "[Solution] Grafana Threema Notifier Error"
description: "How to fix Grafana Threema notification errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Invalid gateway ID or secret
- Recipient Threema ID wrong
- Message format error

## How to Fix

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer API_KEY" -d '{"name":"threema","type":"threema","settings":{"gateway_id":"*GATEWAY","recipient_id":"RECIPIENT","secret":"SECRET"}}' http://localhost:3000/api/alert-notifications
```

## Examples

```bash
journalctl -u grafana-server | grep -i threema
```
