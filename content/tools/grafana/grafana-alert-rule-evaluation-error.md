---
title: "[Solution] Grafana Alert Rule Evaluation Error"
description: "How to fix Grafana alert rule evaluation failures"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Datasource query timing out
- Insufficient data for evaluation
- Expression returning no data

## How to Fix

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/v1/rules | jq '.data.groups[].rules[] | select(.health == "error")'
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/v1/rules | jq '.data.groups[].rules[] | {name: .name, health: .health, state: .state}'
```
