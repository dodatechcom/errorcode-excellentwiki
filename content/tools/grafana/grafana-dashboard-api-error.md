---
title: "[Solution] Grafana Dashboard API Error"
description: "How to fix Grafana API errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- API endpoint incorrect
- Rate limiting too aggressive
- API key missing or invalid

## How to Fix

```bash
curl -s http://localhost:3000/api/health | jq '.'
```

## Examples

```bash
curl -s http://localhost:3000/api/frontend/settings | jq '.buildInfo.version'
```
