---
title: "[Solution] Grafana VictorOps Notifier Error"
description: "How to fix Grafana VictorOps notification errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Invalid routing key
- VictorOps API URL wrong
- Webhook URL malformed

## How to Fix

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer API_KEY" -d '{"name":"victorops","type":"victorops","settings":{"url":"https://alert.victorops.com/integrations/generic/20131114/alert/ROUTING_KEY"}}' http://localhost:3000/api/alert-notifications
```

## Examples

```bash
journalctl -u grafana-server | grep -i victorops
```
