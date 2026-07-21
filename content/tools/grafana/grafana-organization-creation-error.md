---
title: "[Solution] Grafana Organization Creation Error"
description: "How to fix Grafana organization creation errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Organization name already exists
- Maximum org limit reached
- Insufficient admin permissions

## How to Fix

```bash
curl -s -H "Authorization: Bearer ADMIN_KEY" http://localhost:3000/api/orgs | jq '.[].name'
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer ADMIN_KEY" -d '{"name":"NewOrg"}' http://localhost:3000/api/orgs
```

## Examples

```bash
curl -s -H "Authorization: Bearer ADMIN_KEY" http://localhost:3000/api/orgs | jq '.[].name'
```
