---
title: "[Solution] Netlify Edge Middleware Error"
description: "Fix Netlify edge middleware errors. Resolve request processing middleware issues."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

Netlify Edge Middleware Error can prevent your application from working correctly.

## Common Causes

- Middleware not running
- Response not modified
- Middleware crashing

## How to Fix

### Create Middleware

```javascript
export default async (request, context) => {
  const url = new URL(request.url);
  if (url.pathname.startsWith('/admin')) {
    return new Response('Unauthorized', { status: 401 });
  }
};
```

