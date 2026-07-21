---
title: "[Solution] Cloudflare Pages Deploy Error"
description: "Fix Cloudflare Pages deploy errors. Resolve deployment issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Pages Deploy Error can prevent your application from working correctly.

## Common Causes

- Build failed
- Deployment limit reached
- Project not configured
- API token lacks permissions

## How to Fix

### Deploy

```bash
npx wrangler pages deploy dist/
```

### With Project Name

```bash
npx wrangler pages deploy dist/ --project-name=my-project
```

