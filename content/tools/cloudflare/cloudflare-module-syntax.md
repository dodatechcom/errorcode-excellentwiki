---
title: "[Solution] Cloudflare Worker Module Syntax Error"
description: "Fix Cloudflare Worker module syntax errors. Resolve ES module format issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Worker Module Syntax Error can prevent your application from working correctly.

## Common Causes

- Mixing Service Worker and Module syntax
- Import statements in Service Worker format
- Missing type module in wrangler.toml
- CommonJS require not supported

## How to Fix

### Use Module Syntax

```javascript
export default {
  async fetch(request, env, ctx) {
    return new Response("Hello World");
  }
};
```

### Configure

```toml
main = "src/index.js"
type = "javascript-module"
```

