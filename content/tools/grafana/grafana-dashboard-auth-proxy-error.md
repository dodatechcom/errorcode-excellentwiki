---
title: "[Solution] Grafana Dashboard Auth Proxy Error"
description: "How to fix Grafana auth proxy errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Auth proxy headers not configured
- Username header mismatch

## How to Fix

```ini
[auth.proxy]
enabled = true
header_name = X-WEBAUTH-USER
header_property = username
auto_sign_up = true
```

## Examples

```bash
curl -H "X-WEBAUTH-USER: admin" http://localhost:3000/api/org
```
