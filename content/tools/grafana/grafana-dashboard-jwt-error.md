---
title: "[Solution] Grafana Dashboard JWT Auth Error"
description: "How to fix Grafana JWT auth errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- JWT token expired
- JWT secret not matching
- Claims not mapping to Grafana user

## How to Fix

```ini
[auth.jwt]
enabled = true
header_name = X-JWT-Assertion
email_claim = email
username_claim = sub
```

## Examples

```bash
echo "TOKEN" | cut -d'.' -f2 | base64 -d 2>/dev/null | jq .
```
