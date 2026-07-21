---
title: "[Solution] Cloudflare R2 Object Error"
description: "Fix Cloudflare R2 object errors. Resolve uploading or downloading R2 objects."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare R2 Object Error can prevent your application from working correctly.

## Common Causes

- Object exceeds size limit
- Bucket does not exist
- Permission denied
- Content-Type not set

## How to Fix

### Upload

```bash
npx wrangler r2 object put my-bucket/my-file.txt --file=./local-file.txt
```

### Download

```bash
npx wrangler r2 object get my-bucket/my-file.txt --file=./downloaded.txt
```

