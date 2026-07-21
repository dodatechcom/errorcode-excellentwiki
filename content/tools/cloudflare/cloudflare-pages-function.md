---
title: "[Solution] Cloudflare Pages Function Error"
description: "Fix Cloudflare Pages function errors. Resolve serverless function issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Pages Function Error can prevent your application from working correctly.

## Common Causes

- Function file not in correct location
- Function export syntax incorrect
- Binding not configured
- Function exceeds limits

## How to Fix

### Create Function

```javascript
// functions/api/hello.js
export async function onRequestGet(context) {
  return new Response(JSON.stringify({ hello: "world" }));
}
```

### Test

```bash
npx wrangler pages dev dist/
```

