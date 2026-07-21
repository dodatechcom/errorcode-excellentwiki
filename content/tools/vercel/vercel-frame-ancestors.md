---
title: "[Solution] Vercel Frame-Ancestors Error"
description: "Fix Vercel frame-ancestors errors. Resolve embedding restriction issues."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["error"]
---

Vercel Frame-Ancestors Error can prevent your application from working correctly.

## Common Causes

- Frame-ancestors blocking embedding
- Domain not in allowlist
- CSP directive incorrect
- Multiple domains not supported

## How to Fix

### Configure Frame-Ancestors

```json
{"headers": [{"source": "/(.*)", "headers": [{"key": "Content-Security-Policy", "value": "frame-ancestors 'self' https://trusted.com"}]}]}
```

