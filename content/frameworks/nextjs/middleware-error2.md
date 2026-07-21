---
title: "Middleware error"
description: "Next.js middleware throws an unhandled exception or modifies the response incorrectly"
frameworks: ["nextjs"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when Next.js middleware (defined in `middleware.ts` at the project root) throws an exception, uses Node.js-only APIs not available in the Edge Runtime, or modifies the response in an invalid way.

## Common Causes

- Using Node.js modules (`fs`, `path`, `crypto`) in middleware (Edge Runtime only)
- Middleware does not return a `NextResponse`
- Importing a module that uses Node.js APIs in the middleware file
- Middleware running on an incompatible runtime configuration

## How to Fix

1. Only return `NextResponse` from middleware:

```typescript
// middleware.ts
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  const token = request.cookies.get('token');

  if (!token && request.nextUrl.pathname.startsWith('/dashboard')) {
    return NextResponse.redirect(new URL('/login', request.url));
  }

  return NextResponse.next();
}
```

2. Use Edge-compatible imports:

```typescript
// CORRECT -- uses Web API
export function middleware(request: NextRequest) {
  const ip = request.ip || request.headers.get('x-forwarded-for');
  return NextResponse.next();
}

// WRONG -- Node.js module
import fs from 'fs'; // Not available in Edge Runtime
```

3. Configure matcher to limit middleware scope:

```typescript
export const config = {
  matcher: ['/dashboard/:path*', '/api/:path*']
};
```

## Examples

```typescript
// middleware.ts
import { NextResponse } from 'next/server';

export function middleware(request) {
  // Forgot to return a response
  if (request.nextUrl.pathname === '/admin') {
    // No return statement -- error
  }
}
```

```text
Error: Middleware must return a NextResponse or a Response object
```

## Related Errors

- [Routing error]({{< relref "/frameworks/nextjs/routing-error" >}})
