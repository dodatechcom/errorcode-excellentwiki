---
title: "[Solution] Grafana Folder Permission Error"
description: "How to fix Grafana folder permission denied errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- User not granted access to folder
- Team permissions not configured
- Default folder permissions too restrictive

## How to Fix

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer ADMIN_KEY" -d '{"items":[{"userId":2,"permission":2}]}' http://localhost:3000/api/folders/FOLDER_UID/permissions
```

## Examples

```bash
curl -s -H "Authorization: Bearer ADMIN_KEY" http://localhost:3000/api/folders/FOLDER_UID/permissions | jq '.items[]'
```
