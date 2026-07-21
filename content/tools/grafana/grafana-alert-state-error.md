---
title: "[Solution] Grafana Alert State Error"
description: "How to fix Grafana alert state management issues"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Alert stuck in Pending state
- Alert transitioning to Error state
- Alert not resolving when condition clears

## How to Fix

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/alertmanager/grafana/api/v2/alerts | jq '.[] | {labels: .labels, status: .status.state}'
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/alertmanager/grafana/api/v2/alerts | jq '.[] | select(.status.state == "active") | .labels.alertname'
```
