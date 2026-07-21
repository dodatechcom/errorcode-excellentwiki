---
title: "[Solution] Grafana Alert Silence Error"
description: "How to fix Grafana alert silence errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Silence matcher syntax wrong
- Start/end time in wrong format
- Insufficient permissions

## How to Fix

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer API_KEY" -d '{"matchers":[{"name":"alertname","value":"HighError","isRegex":false}],"startsAt":"2024-01-01T00:00:00Z","endsAt":"2024-01-02T00:00:00Z","createdBy":"admin","comment":"Maintenance"}' http://localhost:3000/api/alertmanager/grafana/api/v2/silences
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/alertmanager/grafana/api/v2/silences | jq '.data[] | {id: .id, matchers: .matchers}'
```
