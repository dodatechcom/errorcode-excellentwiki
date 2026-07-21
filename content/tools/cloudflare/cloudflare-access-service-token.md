---
title: "[Solution] Cloudflare Access Service Token Error"
description: "Fix Cloudflare Access service token errors. Resolve machine-to-machine authentication issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Access Service Token Error can prevent your application from working correctly.

## Common Causes

- Token expired
- Client ID or secret incorrect
- Token not attached to policy
- Service token not created

## How to Fix

### Create Token

1. Go to Zero Trust > Access > Service Tokens
2. Click Create Service Token

### Use Token

```bash
curl -H "CF-Access-Client-Id: {client_id}" \
  -H "CF-Access-Client-Secret: {client_secret}" \
  https://your-app.example.com
```

