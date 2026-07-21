---
title: "[Solution] Grafana Annotation Tag Filter Error"
description: "How to fix Grafana annotation tag filtering errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Tag name case sensitivity
- Too many tags causing timeout
- Tag filter syntax incorrect

## How to Fix

```bash
curl -s -H "Authorization: Bearer API_KEY" "http://localhost:3000/api/annotations?tags=deployment&tags=production"
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" "http://localhost:3000/api/annotations?tags=deploy"
```
