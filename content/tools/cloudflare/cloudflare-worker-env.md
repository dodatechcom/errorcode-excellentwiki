---
title: "[Solution] Cloudflare Worker Environment Error"
description: "Fix Cloudflare Worker environment variable errors. Resolve secrets and variables issues."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Worker Environment Error can prevent your application from working correctly.

## Common Causes

- Environment variable not set
- Secret not configured
- Variable name mismatch
- Environment differs between preview and production

## How to Fix

### Set Secret

```bash
npx wrangler secret put MY_SECRET
```

### Set Variable in wrangler.toml

```toml
[vars]
MY_VAR = "value"
```

### Access

```javascript
export default {
  async fetch(request, env) {
    return new Response(env.MY_SECRET ? "set" : "not set");
  }
};
```

