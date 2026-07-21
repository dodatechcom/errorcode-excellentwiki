---
title: "[Solution] Grafana Dashboard Not Found"
description: "How to fix Grafana dashboard not found errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Dashboard deleted or moved
- Wrong dashboard UID in URL
- Dashboard provisioned under different org

## How to Fix

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/search?query=my-dashboard | jq '.[].uid'
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/search | jq '.[].title'
```
