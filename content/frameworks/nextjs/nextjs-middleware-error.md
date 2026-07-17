---
title: "Next.js Middleware Error"
description: "Next.js middleware errors occur when request modification, authentication, or routing logic fails"
frameworks: ["nextjs"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Next.js middleware errors occur when the middleware function encounters exceptions during request processing. Middleware runs before a request is completed and can modify the response, redirect, or rewrite URLs.

## Common Causes

- Middleware function throws an unhandled exception
- Missing `NextResponse` or `NextRequest` import
- Incorrect URL rewriting or redirecting logic
- Middleware not exported as default function
- Using incompatible APIs in middleware

## How to Fix

Set up middleware correctly:

```ts
// middleware.ts (root level)
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  const token = request.cookies.get('token');

  if (!token && request.nextUrl.pathname.startsWith('/dashboard')) {
    return NextResponse.redirect(new URL('/login', request.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: ['/dashboard/:path*', '/api/:path*'],
};
```

Handle authentication in middleware:

```ts
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';
import { verifyToken } from './lib/auth';

export async function middleware(request: NextRequest) {
  const token = request.cookies.get('token')?.value;

  if (request.nextUrl.pathname.startsWith('/protected')) {
    if (!token) {
      return NextResponse.redirect(new URL('/login', request.url));
    }

    try {
      await verifyToken(token);
      return NextResponse.next();
    } catch {
      return NextResponse.redirect(new URL('/login', request.url));
    }
  }

  return NextResponse.next();
}
```

Use middleware for headers:

```ts
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  const response = NextResponse.next();
  response.headers.set('x-custom-header', 'my-value');
  return response;
}
```

## Examples

```ts
// middleware.ts
export function middleware(request: NextRequest) {
  return NextResponse.redirect(new URL('/login'));
  // Missing: check if user is already on /login (infinite redirect)
}
```

```text
Error: Middleware is not allowed to modify response headers after response is sent.
```

## Related Errors

- [App Router error]({{< relref "/frameworks/nextjs/nextjs-app-router-error" >}})
- [Route handler error]({{< relref "/frameworks/nextjs/nextjs-route-handler-error" >}})
