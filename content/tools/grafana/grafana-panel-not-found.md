---
title: "[Solution] Grafana Panel Not Found"
description: "How to fix Grafana panel not found errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Panel deleted from dashboard
- Panel ID changed after reimport
- JSON model corrupted

## How to Fix

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/dashboards/uid/UID | jq '.dashboard.panels[] | {id: .id, title: .title}'
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/dashboards/uid/UID | jq '.dashboard.panels[] | "\\(.id): \\(.title)"'
```
