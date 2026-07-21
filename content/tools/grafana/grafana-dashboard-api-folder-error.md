---
title: "[Solution] Grafana Dashboard API Folder Error"
description: "How to fix Grafana API folder errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Folder already exists with same name
- UID collision
- Insufficient permissions

## How to Fix

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer ADMIN_KEY" -d '{"title":"Engineering","uid":"eng-folder"}' http://localhost:3000/api/folders
```

## Examples

```bash
curl -s -H "Authorization: Bearer ADMIN_KEY" http://localhost:3000/api/folders | jq '.[] | {uid: .uid, title: .title}'
```
