---
title: "[Solution] Grafana Dashboard Share Error"
description: "How to fix Grafana dashboard share errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Share link not public
- Snapshot storage not configured
- Share link expired

## How to Fix

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer API_KEY" -d '{"dashboard":{},"expires":86400}' http://localhost:3000/api/snapshots
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/snapshots | jq '.url'
```
