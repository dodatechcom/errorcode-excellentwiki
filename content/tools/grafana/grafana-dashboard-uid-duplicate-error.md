---
title: "[Solution] Grafana Dashboard UID Duplicate Error"
description: "How to fix Grafana duplicate dashboard UID errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Multiple dashboards with same UID
- Provisioning creating duplicates
- Import creating duplicate UIDs

## How to Fix

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/search | jq -r '.[].uid' | sort | uniq -d
```

## Examples

```bash
curl -s -H "Authorization: Bearer API_KEY" http://localhost:3000/api/search | jq -r '.[].uid' | sort | uniq -c | sort -rn | head
```
