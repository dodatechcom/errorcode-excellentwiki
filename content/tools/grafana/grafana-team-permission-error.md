---
title: "[Solution] Grafana Team Permission Error"
description: "How to fix Grafana team permission errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Team does not have access to folder
- Team role insufficient
- External group sync not working

## How to Fix

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer ADMIN_KEY" -d '{"items":[{"teamId":1,"permission":2}]}' http://localhost:3000/api/folders/1/permissions
```

## Examples

```bash
curl -s -H "Authorization: Bearer ADMIN_KEY" http://localhost:3000/api/teams/1/members | jq '.[].login'
```
