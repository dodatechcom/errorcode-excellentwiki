---
title: "[Solution] Netlify Edge Functions Error — Fix Edge Function Runtime Failure"
description: "Fix Netlify Edge Functions errors when Deno-based edge functions fail to execute. Debug Deno runtime issues, module imports, and configuration problems."
tools: ["netlify"]
error-types: ["edge-function-error"]
severities: ["error"]
weight: 5
---

A Netlify Edge Functions error occurs when a Deno-based edge function fails to execute. The function may throw a runtime error, fail to import modules, or timeout.

## What This Error Means

Netlify Edge Functions run on Deno at the CDN edge. When they fail:

```
Error: Edge Function threw an exception
TypeError: Cannot read properties of undefined (reading 'headers')
```

## Why It Happens

- The function uses a Deno API incorrectly (request, response, fetch)
- An imported module does not exist or cannot be resolved
- The function exceeds the 50ms execution limit
- The function uses global variables that are not available in the Edge runtime
- The function references environment variables without the correct prefix
- The function tries to use Node.js built-in modules not available in Deno

## How to Fix It

### Check Function Syntax

```typescript
// netlify/edge-functions/hello.ts
import type { Context } from '@netlify/edge-functions';

export default async (request: Request, context: Context) => {
  const url = new URL(request.url);
  const name = url.searchParams.get('name') || 'World';
  return new Response(`Hello, ${name}!`);
};
```

### Use Correct Function Signature

```typescript
export default async (request: Request, context: Context) => {
  // context contains: geo, json, cookies, next, etc.
};
```

### Configure Edge Functions in netlify.toml

```toml
[[edge_functions]]
function = "hello"
path = "/api/hello"
```

### Avoid Node.js Modules

```typescript
// Do NOT use:
// import fs from 'node:fs';
// import path from 'node:path';

// DO use:
// Web APIs: Request, Response, URL, fetch
// Deno APIs: Deno.env, Deno.readTextFile
```

### Add Error Handling

```typescript
export default async (request: Request, context: Context) => {
  try {
    const data = await request.json();
    return new Response(JSON.stringify(data));
  } catch (error) {
    return new Response(`Error: ${error.message}`, { status: 500 });
  }
};
```

### Set Environment Variables

```toml
[build]
environment = { MY_VAR = "value" }
```

Access via `Deno.env.get('MY_VAR')`.

## Common Mistakes

- Using Node.js modules in Deno-based Edge Functions
- Not wrapping async operations in try/catch for error handling
- Exceeding the 50ms execution time limit for Edge Functions
- Forgetting to return a Response object from the function

## Related Pages

- [Netlify Functions Error]({{< relref "/tools/netlify/netlify-functions-error" >}}) -- Serverless function issues
- [Netlify Build Error]({{< relref "/tools/netlify/netlify-build-error" >}}) -- Build failures
- [Netlify Deploy Error]({{< relref "/tools/netlify/netlify-deploy-error" >}}) -- Deploy failures
