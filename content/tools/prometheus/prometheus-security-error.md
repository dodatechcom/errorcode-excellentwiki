---
title: "[Solution] Prometheus Security Error"
description: "Fix Prometheus security errors. Learn why this happens and how to resolve it quickly."
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Prometheus Security Error

Prometheus security errors occur when authentication, authorization, or TLS configuration fails.

## Why This Happens

- TLS certificate expired
- Auth token invalid
- RBAC denied
- CORS blocked

## Common Error Messages

- `security_tls_error`
- `security_auth_error`
- `security_rbac_error`
- `security_cors_error`

## How to Fix It

### Solution 1: Configure TLS

Enable TLS:

```bash
prometheus --web.config.file=web-config.yml
```

### Solution 2: Set up authentication

Configure basic auth:

```yaml
basic_auth_users:
  prometheus: $2y$10$hash
```

### Solution 3: Fix CORS issues

Configure CORS headers if needed.


## Common Scenarios

- **TLS expired:** Renew certificates.
- **Auth failed:** Verify credentials.

## Prevent It

- Use TLS everywhere
- Rotate certificates
- Monitor security alerts
