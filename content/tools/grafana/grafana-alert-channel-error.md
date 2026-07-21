---
title: "[Solution] Grafana Alert Channel Error"
description: "How to fix Grafana alert channel configuration errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Channel type not supported
- Missing required settings
- Channel disabled or deleted

## How to Fix

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer API_KEY" -d '{"name":"slack","type":"slack","settings":{"url":"https://hooks.slack.com/services/T00/B00/xxx","recipient":"#alerts"}}' http://localhost:3000/api/alert-notifications
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/alert-notifications | jq '.[] | {id: .id, name: .name, type: .type}'
```
