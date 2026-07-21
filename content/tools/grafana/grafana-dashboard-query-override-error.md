---
title: "[Solution] Grafana Dashboard Query Override Error"
description: "How to fix Grafana query override errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Query target not referencing correct datasource
- Override rules conflicting
- Query refId mismatch

## How to Fix

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/dashboards/uid/UID | jq '.dashboard.panels[0].targets[] | {refId: .refId, expr: .expr}'
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/dashboards/uid/UID | jq '.dashboard.panels[] | {title: .title, datasource: .datasource}'
```
