---
title: "[Solution] Grafana Dashboard Basic Auth Error"
description: "How to fix Grafana basic auth errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Basic auth disabled
- Credentials wrong

## How to Fix

```ini
[auth.basic]
enabled = true
```

## Examples

```bash
curl -u admin:admin http://localhost:3000/api/org | jq '.name'
```
