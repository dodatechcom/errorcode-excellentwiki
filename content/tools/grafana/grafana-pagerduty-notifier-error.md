---
title: "[Solution] Grafana PagerDuty Notifier Error"
description: "How to fix Grafana PagerDuty notification errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Integration key invalid
- Severity level not set
- API endpoint unreachable

## How to Fix

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer API_KEY" -d '{"name":"pd","type":"pagerduty","settings":{"integrationKey":"key","severity":"critical"}}' http://localhost:3000/api/alert-notifications
```

## Examples

```bash
journalctl -u grafana-server | grep -i pagerduty
```
