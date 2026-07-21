---
title: "[Solution] Vercel Reference Environment Error"
description: "Fix Vercel reference environment errors. Resolve env var reference issues."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["error"]
---

Vercel Reference Environment Error can prevent your application from working correctly.

## Common Causes

- Reference target does not exist
- Circular reference
- Reference syntax incorrect
- Target variable deleted

## How to Fix

### Create Reference

```bash
npx vercel env add MY_VAR production --reference TARGET_VAR
```

