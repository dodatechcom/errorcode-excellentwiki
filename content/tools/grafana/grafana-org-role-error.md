---
title: "[Solution] Grafana Organization Role Error"
description: "How to fix Grafana org role assignment errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Role level too low
- Default role assignment incorrect
- Missing Admin role

## How to Fix

```bash
curl -s -H "Authorization: Bearer ADMIN_KEY" http://localhost:3000/api/org/users | jq '.[] | {login: .login, role: .role}'
```

## Examples

```bash
curl -X PATCH -H "Content-Type: application/json" -H "Authorization: Bearer ADMIN_KEY" -d '{"role":"Admin"}' http://localhost:3000/api/org/users/2
```
