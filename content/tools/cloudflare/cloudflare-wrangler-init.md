---
title: "[Solution] Cloudflare Wrangler Init Error"
description: "Fix Cloudflare wrangler init errors. Resolve new Worker project initialization issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Wrangler Init Error can prevent your application from working correctly.

## Common Causes

- Directory already contains files
- Template download failed
- Node.js version incompatible
- Permission denied

## How to Fix

### Initialize

```bash
npx wrangler init my-worker
```

### Initialize in Current Directory

```bash
npx wrangler init
```

