---
title: "[Solution] Vercel Output Directory Error"
description: "Fix Vercel output directory errors. Resolve build output location issues."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["error"]
---

Vercel Output Directory Error can prevent your application from working correctly.

## Common Causes

- Output directory does not exist after build
- Wrong directory specified
- Build output in unexpected location
- Framework default output differs

## How to Fix

### Check Output

```bash
ls -la dist/
ls -la build/
ls -la .next/
```

### Configure

```json
{"outputDirectory": "dist"}
```

### Framework Defaults

- Next.js: `.next`
- CRA: `build`
- Vite: `dist`
- Nuxt: `.output`

