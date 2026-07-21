---
title: "[Solution] Cloudflare R2 Bucket Error"
description: "Fix Cloudflare R2 bucket errors. Resolve R2 object storage bucket issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare R2 Bucket Error can prevent your application from working correctly.

## Common Causes

- Bucket name already taken
- Bucket name contains invalid characters
- API token lacks permissions
- Bucket limit exceeded

## How to Fix

### Create Bucket

```bash
npx wrangler r2 bucket create my-bucket
```

### List Buckets

```bash
npx wrangler r2 bucket list
```

