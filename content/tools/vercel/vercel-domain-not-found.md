---
title: "[Solution] Vercel Domain Not Found Error"
description: "Fix Vercel domain not found errors. Resolve domain configuration issues."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["error"]
---

Vercel Domain Not Found Error can prevent your application from working correctly.

## Common Causes

- Domain not added to project
- DNS not configured
- Domain spelling incorrect
- Domain not verified

## How to Fix

### Add Domain

```bash
npx vercel domains add example.com
```

### Verify DNS

```bash
dig example.com CNAME +short
```

