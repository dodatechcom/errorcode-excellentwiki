---
title: "[Solution] Grafana Team Not Found"
description: "How to fix Grafana team not found errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Team deleted or not created
- Wrong team ID or name
- Team in different organization

## How to Fix

```bash
curl -s -H "Authorization: Bearer ADMIN_KEY" http://localhost:3000/api/teams/search | jq '.teams[].name'
```

## Examples

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer ADMIN_KEY" -d '{"name":"DevOps","email":"devops@example.com"}' http://localhost:3000/api/teams
```
