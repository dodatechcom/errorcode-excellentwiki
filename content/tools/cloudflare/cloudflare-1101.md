---
title: "[Solution] Cloudflare 1101 Error — Worker Threw Exception"
description: "Fix Cloudflare Error 1101 when a Cloudflare Worker throws a runtime error. Debug JavaScript exceptions, check Worker code, and enable error logging."
tools: ["cloudflare"]
error-types: ["worker-error"]
severities: ["error"]
weight: 5
---

Cloudflare Error 1101 occurs when a Cloudflare Worker throws an unhandled JavaScript exception. The Worker crashes during request processing.

## What This Error Means

The Worker code threw an exception that was not caught. Cloudflare returns a 1101 error page to the visitor.

## Why It Happens

- JavaScript runtime error (TypeError, ReferenceError, SyntaxError)
- Unhandled Promise rejection inside a fetch event handler
- Calling undefined functions or accessing undefined properties
- JSON parsing failure on invalid input
- Network timeout when calling fetch() from inside the Worker
- Exceeding CPU time limit (10ms on free plan, 50ms on paid)
- Using Node.js APIs not available in the Workers runtime

## How to Fix It

### Check Worker Logs

```bash
wrangler tail
```

### Add Global Error Handling

```javascript
addEventListener('fetch', event => {
  event.respondWith(handleRequest(event).catch(error => {
    console.error('Worker error:', error);
    return new Response('Internal Error', { status: 500 });
  }));
});

async function handleRequest(event) {
  // Your logic here
}
```

### Debug with Response Headers

```javascript
async function handleRequest(request) {
  try {
    const result = await processRequest(request);
    return result;
  } catch (error) {
    return new Response(error.stack, {
      status: 500,
      headers: { 'Content-Type': 'text/plain' }
    });
  }
}
```

### Validate Incoming Data

```javascript
async function handleRequest(request) {
  try {
    const body = await request.json();
    // Validate body before using
    if (!body.name) throw new Error('Missing name');
  } catch (e) {
    return new Response('Invalid JSON', { status: 400 });
  }
}
```

### Test Locally Before Deploying

```bash
wrangler dev
# Test all endpoints locally
```

### Check for Unsupported APIs

```javascript
// Do not use Node.js-specific APIs:
// fs, path, crypto (use Web Crypto instead)
// process.env (use env vars via wrangler.toml)
```

## Common Mistakes

- Not adding a catch-all error handler in the fetch event listener
- Using Node.js APIs that are not available in the Workers runtime
- Not validating incoming request bodies before parsing JSON
- Assuming fetch() always succeeds without handling timeout or network errors

## Related Pages

- [Cloudflare 1102 Error]({{< relref "/tools/cloudflare/cloudflare-1102" >}}) -- Worker script error
- [Cloudflare 1019 Error]({{< relref "/tools/cloudflare/cloudflare-1019" >}}) -- Memory limit exceeded
- [Cloudflare 1020 Error]({{< relref "/tools/cloudflare/cloudflare-1020" >}}) -- Access denied
