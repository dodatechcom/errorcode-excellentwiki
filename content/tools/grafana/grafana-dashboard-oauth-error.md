---
title: "[Solution] Grafana Dashboard OAuth Error"
description: "How to fix Grafana OAuth errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- OAuth provider misconfigured
- Client ID or secret wrong
- Callback URL mismatch

## How to Fix

```ini
[auth.generic_oauth]
enabled = true
client_id = YOUR_ID
client_secret = YOUR_SECRET
auth_url = https://provider.com/authorize
token_url = https://provider.com/token
```

## Examples

```bash
curl -s http://localhost:3000/api/login/generic_oauth -v 2>&1 | grep -i location
```
