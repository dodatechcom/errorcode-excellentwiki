---
title: "[Solution] Grafana Dashboard UID Error"
description: "How to fix Grafana dashboard UID errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Duplicate dashboard UIDs
- UID contains invalid characters
- UID too long or too short

## How to Fix

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/search | jq -r '.[].uid' | sort | uniq -d
```

## Examples

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer API_KEY" -d '{"dashboard":{"uid":"my-unique-id","title":"My Dashboard"}}' http://localhost:3000/api/dashboards/db
```
