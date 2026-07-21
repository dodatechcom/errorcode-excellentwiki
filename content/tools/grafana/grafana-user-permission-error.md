---
title: "[Solution] Grafana User Permission Error"
description: "How to fix Grafana user permission denied errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- User role insufficient
- Datasource permission restrictions
- Folder permissions blocking access

## How to Fix

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer ADMIN_KEY" -d '{"userId":2,"role":"Editor"}' http://localhost:3000/api/org/users
```

## Examples

```bash
curl -s -H "Authorization: Bearer ADMIN_KEY" http://localhost:3000/api/folders/1/permissions | jq '.'
```
