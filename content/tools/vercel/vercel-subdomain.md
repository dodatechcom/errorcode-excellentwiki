---
title: "[Solution] Vercel Subdomain Error"
description: "Fix Vercel subdomain errors. Resolve subdomain configuration issues."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["error"]
---

Vercel Subdomain Error can prevent your application from working correctly.

## Common Causes

- Subdomain not configured
- CNAME record missing
- Subdomain already in use

## How to Fix

### Add Subdomain

```bash
npx vercel domains add app.example.com
```

### Configure DNS

Add CNAME record pointing to `cname.vercel-dns.com`.

