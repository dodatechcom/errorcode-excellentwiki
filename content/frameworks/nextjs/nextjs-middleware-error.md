---
title: "[Solution] Next.js Middleware Execution Error — How to Fix"
description: "Fix Next.js middleware errors. Resolve middleware execution, edge runtime, and middleware configuration issues."
frameworks: ["nextjs"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

A Next.js middleware execution error occurs when the middleware file fails to run, throws an exception, or returns an invalid response. Middleware runs on the Edge runtime and has specific constraints.

## Why It Happens

Next.js middleware runs at the edge before a request is completed. Errors occur when middleware uses Node.js-only APIs (not available at the edge), when the middleware file is incorrectly named, when middleware returns an invalid response object, when middleware modifies headers improperly, or when the middleware file is too large.

## Common Error Messages

```
Error: Middleware is not allowed to use Node.js API "fs.readFile"
```

```
Error: The default export function must be a function
```

```
ReferenceError: Buffer is not defined
```

```
Error: Edge Runtime does not support dynamic imports
```

## How to Fix It

### 1. Create Middleware Correctly

Use the correct file name and export:

```typescript
// middleware.ts (must be in project root)
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
    // Access request properties
    const token = request.cookies.get('token')?.value;
    const pathname = request.nextUrl.pathname;

    // Protected routes
    if (pathname.startsWith('/dashboard') && !token) {
        return NextResponse.redirect(new URL('/login', request.url));
    }

    // Add custom headers
    const response = NextResponse.next();
    response.headers.set('x-custom-header', 'value');
    return response;
}

export const config = {
    matcher: [
        '/dashboard/:path*',
        '/api/:path*',
        '/admin/:path*',
    ],
};
```

### 2. Avoid Node.js APIs in Middleware

Use Edge-compatible alternatives:

```typescript
import { NextResponse } from 'next/server';

export function middleware(request: NextRequest) {
    // Wrong: Node.js API (not available at edge)
    // const fs = require('fs');
    // const crypto = require('crypto');

    // Correct: use Web API alternatives
    const encoder = new TextEncoder();
    const data = encoder.encode('hello');
    const hash = crypto.subtle.digest('SHA-256', data);

    // Use request.url, request.cookies, request.headers
    // (all available in Edge runtime)

    return NextResponse.next();
}
```

### 3. Handle Middleware Errors Gracefully

Catch errors to prevent complete failure:

```typescript
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
    try {
        const token = request.cookies.get('token')?.value;

        if (isProtectedRoute(request.nextUrl.pathname) && !token) {
            const loginUrl = new URL('/login', request.url);
            loginUrl.searchParams.set('from', request.nextUrl.pathname);
            return NextResponse.redirect(loginUrl);
        }

        return NextResponse.next();
    } catch (error) {
        // Log error (limited logging at edge)
        console.error('Middleware error:', error);
        return NextResponse.next();
    }
}

function isProtectedRoute(pathname: string): boolean {
    return pathname.startsWith('/dashboard') ||
           pathname.startsWith('/settings');
}
```

### 4. Use Middleware for Authentication

Implement JWT verification at the edge:

```typescript
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
    const token = request.cookies.get('session')?.value;

    if (!token && request.nextUrl.pathname.startsWith('/protected')) {
        return NextResponse.redirect(new URL('/login', request.url));
    }

    // Verify token expiry (basic check — use proper JWT library)
    if (token) {
        try {
            const payload = JSON.parse(atob(token.split('.')[1]));
            if (payload.exp * 1000 < Date.now()) {
                const response = NextResponse.redirect(new URL('/login', request.url));
                response.cookies.delete('session');
                return response;
            }
        } catch {
            const response = NextResponse.redirect(new URL('/login', request.url));
            response.cookies.delete('session');
            return response;
        }
    }

    return NextResponse.next();
}
```

## Common Scenarios

**Scenario 1: Middleware uses `require()` or `fs`.**
Edge runtime doesn't support Node.js modules. Use Web APIs like `fetch`, `crypto.subtle`, and `TextEncoder`.

**Scenario 2: Middleware slows down all routes.**
Use the `config.matcher` to limit middleware execution to specific paths.

**Scenario 3: Middleware redirects create loops.**
Ensure the redirect target is not also matched by the middleware matcher.

## Prevent It

1. **Keep middleware under 4KB** to avoid performance issues at the edge.

2. **Use `config.matcher`** to restrict middleware to only the routes that need it.

3. **Test middleware locally** with `next dev` before deploying to production.
