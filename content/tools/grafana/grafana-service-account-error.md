---
title: "[Solution] Grafana Service Account Error"
description: "Fix Grafana service account errors. Learn why this happens and how to resolve it quickly."
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Grafana Service Account Error

Grafana service account errors occur when service accounts fail to authenticate or have incorrect permissions.

## Why This Happens

- Service account not found
- Token invalid
- Permission denied
- Token expired

## Common Error Messages

- `sa_not_found_error`
- `sa_token_error`
- `sa_permission_error`
- `sa_expired_error`

## How to Fix It

### Solution 1: Create service account

Create a service account:

```bash
curl -X POST http://grafana:3000/api/serviceaccounts -d '{"name":"my-sa"}'
```

### Solution 2: Generate tokens

Create tokens for service accounts.

### Solution 3: Set permissions

Assign appropriate roles.


## Common Scenarios

- **Service account not found:** Check the service account name.
- **Token invalid:** Regenerate the token.

## Prevent It

- Use service accounts for automation
- Set minimal permissions
- Rotate tokens
