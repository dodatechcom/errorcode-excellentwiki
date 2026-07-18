---
title: "[Solution] Vercel Middleware Runtime Error — How to Fix"
description: "Fix Vercel middleware runtime errors. Resolve middleware execution failures, import issues, and edge compatibility problems."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["error"]
weight: 1
comments: true
---

A Vercel middleware runtime error occurs when your Edge Middleware encounters an error during execution. Middleware runs before a request is completed and can modify the response, but it must use edge-compatible APIs only.

## What This Error Means

Middleware in Next.js (and Vercel) runs at the edge before the request reaches your page or API route. It must be lightweight and use only Web-standard APIs (no Node.js modules). When middleware violates these constraints or throws an unhandled error, the request fails with an Edge Runtime Error.

## Why It Happens

- Middleware imports Node.js-only modules (fs, path, process)
- Middleware performs long-running operations (database queries, API calls)
- An unhandled exception occurs in the middleware
- Middleware is too large (exceeds 50 KB after minification)
- Missing or invalid `export const config` configuration
- Edge Runtime does not support the API being called
- The middleware tries to access request body without consuming it first
- The middleware returns an invalid Response object

## Common Error Messages

- `Edge Runtime Error` — The middleware threw a runtime error
- `MODULE_NOT_FOUND` — A required module is not available in Edge Runtime
- `Function has been terminated` — Middleware exceeded execution time
- `TypeError: ... is not a function` — Unsupported API usage in Edge Runtime
- `The edge function has already been responded to` — Double response error

## How to Fix It

### Use Only Edge-Compatible APIs

```javascript
// middleware.js (at project root)
import { NextResponse } from 'next/server';

// WRONG: Node.js-only module
import fs from 'fs';
const config = fs.readFileSync('./config.json');

// RIGHT: Use environment variables or inline config
export function middleware(request) {
  const config = {
    maintenanceMode: process.env.MAINTENANCE_MODE === 'true',
  };

  if (config.maintenanceMode) {
    return NextResponse.rewrite(new URL('/maintenance', request.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: ['/((?!api|_next/static|_next/image|favicon.ico).*)'],
};
```

### Keep Middleware Lightweight

```javascript
// WRONG: Heavy middleware with API calls
import { NextResponse } from 'next/server';

export async function middleware(request) {
  // This is too slow for middleware
  const user = await fetch('https://api.example.com/user', {
    headers: { Authorization: request.headers.get('Authorization') },
  });

  if (!user.ok) {
    return NextResponse.redirect('/login');
  }

  return NextResponse.next();
}

// RIGHT: Do minimal work in middleware, delegate to pages
import { NextResponse } from 'next/server';

export function middleware(request) {
  const token = request.cookies.get('session-token');

  // Quick check only
  if (!token) {
    return NextResponse.redirect(new URL('/login', request.url));
  }

  // Detailed auth check happens in the page/API route
  return NextResponse.next();
}
```

### Handle Edge Runtime Limitations

```javascript
// Available in Edge Runtime
import { NextResponse } from 'next/server';

// These work:
// - fetch()
// - Request/Response/Headers
// - TextEncoder/TextDecoder
// - crypto.subtle
// - URL/URLSearchParams
// - JSON
// - console.log/warn/error

// These do NOT work in Edge:
// - fs, path, os, child_process
// - require() or dynamic imports of Node modules
// - process.env (use Next.js env config instead)
// - Buffer (use ArrayBuffer or Uint8Array)
// - Node.js crypto (use Web Crypto API)

export function middleware(request) {
  // Use Web Crypto API instead of Node crypto
  const hash = await crypto.subtle.digest(
    'SHA-256',
    new TextEncoder().encode(request.url)
  );

  return NextResponse.next();
}
```

### Set Proper Config Matcher

```javascript
// middleware.js — control which paths trigger middleware
export const config = {
  matcher: [
    // Match all paths except static files
    '/((?!_next/static|_next/image|favicon.ico|public).*)',
    // Or be more specific
    '/dashboard/:path*',
    '/api/:path*',
  ],
};
```

### Debug Middleware Errors

```javascript
import { NextResponse } from 'next/server';

export function middleware(request) {
  console.log('Middleware triggered:', request.nextUrl.pathname);

  try {
    // Your middleware logic
    const response = NextResponse.next();

    // Add debug headers
    response.headers.set('x-middleware-timestamp', Date.now().toString());

    return response;
  } catch (err) {
    console.error('Middleware error:', err.message, err.stack);

    // Return a graceful fallback instead of crashing
    return NextResponse.next();
  }
}
```

## Common Scenarios

- **Auth middleware imports jsonwebtoken:** A developer imports the `jsonwebtoken` Node.js library in middleware, which uses `crypto` module operations unavailable in Edge Runtime.
- **Middleware too large:** A complex middleware with many route-specific checks exceeds the 50 KB size limit, causing the build to fail.
- **Missing config export:** No `export const config` is defined, so middleware runs on every request including static assets, causing performance issues.

## Prevent It

1. Only import Web-standard APIs and Next.js built-ins in middleware — test with `next dev --turbo` to catch Node.js usage early
2. Keep middleware under 50 KB by extracting complex logic to API routes or server components
3. Always export a `config` matcher to limit which paths trigger middleware execution

## Related Pages

- [Vercel Edge Function Error]({{< relref "/tools/vercel/vercel-edge-function-error" >}}) — Edge function error
- [Vercel Serverless Timeout]({{< relref "/tools/vercel/vercel-serverless-timeout" >}}) — Function timeout
