---
title: "[Solution] Grafana Dashboard API Search Error"
description: "How to fix Grafana API search errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Search query syntax wrong
- Type filter not matching

## How to Fix

```bash
curl -s -H "Authorization: Bearer API_KEY" "http://localhost:3000/api/search?query=production&type=dash-db" | jq '.[].title'
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" "http://localhost:3000/api/search?tag=team-ops" | jq '.[].title'
```
