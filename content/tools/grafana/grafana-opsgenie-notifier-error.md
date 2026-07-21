---
title: "[Solution] Grafana OpsGenie Notifier Error"
description: "How to fix Grafana OpsGenie notification errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Invalid API key
- Wrong API URL (EU vs US)
- Missing message field

## How to Fix

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer API_KEY" -d '{"name":"opsgenie","type":"opsgenie","settings":{"apiKey":"key","apiUrl":"https://api.opsgenie.com"}}' http://localhost:3000/api/alert-notifications
```

## Examples

```bash
journalctl -u grafana-server | grep -i opsgenie
```
