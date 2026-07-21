---
title: "[Solution] Grafana Dashboard Cache Error"
description: "How to fix Grafana cache errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Cache backend unreachable
- Cache invalidation not working

## How to Fix

```ini
[caching]
enabled = true
backend = memory
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/frontend/settings | jq '.caching'
```
