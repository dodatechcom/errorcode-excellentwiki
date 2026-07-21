---
title: "[Solution] Cloudflare R2 Public URL Error"
description: "Fix Cloudflare R2 public URL errors. Resolve public access issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare R2 Public URL Error can prevent your application from working correctly.

## Common Causes

- Public access not enabled
- Custom domain not configured
- CORS policy blocks access
- Bucket not configured for public access

## How to Fix

### Enable Public Access

1. Go to R2 in dashboard
2. Select bucket
3. Go to Settings
4. Enable Public Access

### Add Custom Domain

```bash
npx wrangler r2 bucket domain add my-bucket --domain assets.example.com
```

