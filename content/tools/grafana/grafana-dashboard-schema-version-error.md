---
title: "[Solution] Grafana Dashboard Schema Version Error"
description: "How to fix Grafana dashboard schema version errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Dashboard exported from newer version
- Schema version too old
- Manual JSON edit broke schema

## How to Fix

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/dashboards/uid/UID | jq '.dashboard.schemaVersion'
grafana-cli --version
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/dashboards/uid/UID | jq '.dashboard.schemaVersion'
```
