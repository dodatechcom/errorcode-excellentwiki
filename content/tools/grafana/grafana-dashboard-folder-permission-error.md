---
title: "[Solution] Grafana Dashboard Folder Permission Error"
description: "How to fix Grafana dashboard folder permission errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- User not granted access to folder
- Team folder permissions not configured
- Default org role too restrictive

## How to Fix

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer API_KEY" -d '{"items":[{"teamId":1,"permission":2}]}' http://localhost:3000/api/folders/FOLDER_UID/permissions
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/folders/FOLDER_UID/permissions | jq '.items[]'
```
