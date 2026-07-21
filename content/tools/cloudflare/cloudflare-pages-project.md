---
title: "[Solution] Cloudflare Pages Project Error"
description: "Fix Cloudflare Pages project errors. Resolve deployment and configuration issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Pages Project Error can prevent your application from working correctly.

## Common Causes

- Project not connected to repository
- Build command incorrect
- Output directory wrong
- Project name taken

## How to Fix

### Create Project

```bash
npx wrangler pages project create my-project
```

### Deploy

```bash
npx wrangler pages deploy dist/
```

