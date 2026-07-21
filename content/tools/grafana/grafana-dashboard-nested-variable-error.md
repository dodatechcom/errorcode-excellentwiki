---
title: "[Solution] Grafana Dashboard Nested Variable Error"
description: "How to fix Grafana nested variable errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Dependent variable referencing non-existent parent
- Circular dependencies
- Variable query using wrong datasource

## How to Fix

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/dashboards/uid/UID | jq '.dashboard.templating.list[] | {name: .name, query: .query}'
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/dashboards/uid/UID | jq '.dashboard.templating.list[] | {name: .name, type: .type}'
```
