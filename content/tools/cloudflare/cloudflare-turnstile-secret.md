---
title: "[Solution] Cloudflare Turnstile Secret Key Error"
description: "Fix Cloudflare Turnstile secret key errors. Resolve server-side token verification failures."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Turnstile Secret Key Error can prevent your application from working correctly.

## Common Causes

- Secret key exposed in client-side code
- Secret key incorrect or malformed
- Token verification endpoint misconfigured
- Secret key rotated without updating server

## How to Fix

### Verify

```bash
curl -X POST "https://challenges.cloudflare.com/turnstile/v0/siteverify" \
  -d "secret={secret_key}&response={turnstile_token}"
```

### Store Securely

Never expose secret key in client-side code.

