---
title: "[Solution] Grafana Datasource Not Working"
description: "How to fix Grafana datasource connection failures"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Datasource URL unreachable
- Authentication credentials expired
- TLS certificate verification failure

## How to Fix

```bash
curl -X POST -H "Authorization: Bearer API_KEY" http://localhost:3000/api/datasources/uid/ABC123/health | jq '.status'
```

## Examples

```bash
curl -H "Authorization: Bearer API_KEY" "http://localhost:3000/api/datasources/proxy/ABC123/api/v1/query?query=up"
```
