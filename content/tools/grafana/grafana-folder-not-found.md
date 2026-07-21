---
title: "[Solution] Grafana Folder Not Found"
description: "How to fix Grafana folder not found errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Folder deleted
- Wrong folder UID
- Provisioned folder in different org

## How to Fix

```bash
curl -s -H "Authorization: Bearer ADMIN_KEY" http://localhost:3000/api/folders | jq '.[].title'
```

## Examples

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer ADMIN_KEY" -d '{"title":"Monitoring"}' http://localhost:3000/api/folders
```
