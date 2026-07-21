---
title: "[Solution] Grafana Dashboard Alerting Migration Error"
description: "How to fix Grafana alerting migration errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Legacy alerts not converted
- Notification channels lost

## How to Fix

```bash
journalctl -u grafana-server | grep -i "alert migration"
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/v1/rules | jq '.data.groups[].rules[] | .title'
```
