---
title: "[Solution] Grafana Pushover Notifier Error"
description: "How to fix Grafana Pushover notification errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Invalid user key or API token
- Message priority too high
- Device name not specified

## How to Fix

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer API_KEY" -d '{"name":"pushover","type":"pushover","settings":{"userKey":"KEY","apiToken":"TOKEN","priority":"0"}}' http://localhost:3000/api/alert-notifications
```

## Examples

```bash
journalctl -u grafana-server | grep -i pushover
```
