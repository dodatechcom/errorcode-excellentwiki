---
title: "[Solution] Grafana Dashboard Provisioning Sync Error"
description: "How to fix Grafana provisioning sync errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Provisioned dashboard modified in UI not syncing
- File changes not picked up

## How to Fix

```bash
sudo systemctl restart grafana-server
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/search | jq '.[] | select(.provisioned == true) | .title'
```
