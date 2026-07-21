---
title: "[Solution] Grafana Dashboard API Annotation Error"
description: "How to fix Grafana API annotation errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Annotation data too large
- Time range invalid

## How to Fix

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer API_KEY" -d '{"time":1609459200000,"text":"Deployment","tags":["deploy"]}' http://localhost:3000/api/annotations
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" "http://localhost:3000/api/annotations?from=1609459200000&to=1609462800000" | jq '.[].text'
```
