---
title: "[Solution] Grafana Dashboard Proxy Error"
description: "How to fix Grafana datasource proxy errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Datasource proxy URL incorrect
- Authentication failing through proxy
- Proxy timeout too short

## How to Fix

```bash
curl -H "Authorization: Bearer API_KEY" "http://localhost:3000/api/datasources/proxy/DS_UID/api/v1/query?query=up"
```

## Examples

```bash
curl -H "Authorization: Bearer API_KEY" "http://localhost:3000/api/datasources/proxy/DS_UID/api/v1/status/config"
```
