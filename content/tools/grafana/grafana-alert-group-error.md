---
title: "[Solution] Grafana Alert Group Error"
description: "How to fix Grafana alert group errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Alert group contains no rules
- Group interval too short
- Rules within group conflicting

## How to Fix

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/v1/rules | jq '.data.groups[] | {name: .name}'
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/v1/rules | jq '.data.groups[] | select(.name == "my-group") | .rules[] | {name: .name, state: .state}'
```
