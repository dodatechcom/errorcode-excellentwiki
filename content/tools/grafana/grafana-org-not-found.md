---
title: "[Solution] Grafana Organization Not Found"
description: "How to fix Grafana organization not found errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Organization deleted
- Wrong org ID in API request
- User not member of requested org

## How to Fix

```bash
curl -s -H "Authorization: Bearer ADMIN_KEY" http://localhost:3000/api/orgs | jq '.[].name'
```

## Examples

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer ADMIN_KEY" -d '{"name":"NewOrg"}' http://localhost:3000/api/orgs
```
