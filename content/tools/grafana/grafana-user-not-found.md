---
title: "[Solution] Grafana User Not Found"
description: "How to fix Grafana user not found errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Username or email does not exist
- User was deleted
- Searching in wrong organization

## How to Fix

```bash
curl -s -H "Authorization: Bearer ADMIN_KEY" "http://localhost:3000/api/users?query=admin" | jq '.[].login'
```

## Examples

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer ADMIN_KEY" -d '{"name":"John","email":"john@example.com","login":"john","password":"secret"}' http://localhost:3000/api/admin/users
```
