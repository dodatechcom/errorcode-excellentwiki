---
title: "[Solution] Vercel Cross-Origin Error"
description: "Fix Vercel cross-origin errors. Resolve cross-origin resource sharing issues."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["error"]
---

Vercel Cross-Origin Error can prevent your application from working correctly.

## Common Causes

- CORS headers missing
- Origin not allowed
- Preflight request failed
- Credentials not included

## How to Fix

### Add CORS Headers

```javascript
export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,POST');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
}
```

