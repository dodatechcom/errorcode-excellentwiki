---
title: "Next.js middleware errors"
description: "Next.js middleware errors that occur when middleware is misconfigured, has incorrect response handling, or doesn't properly handle edge cases. Middleware runs on the Edge Runtime and has specific limitations."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "nextjs"
tags: ["error", "middleware", "edge", "routing"]
severity: "error"
solution: "Ensure middleware.ts is in the project root. Handle all response cases including redirects. Use NextResponse correctly. Be aware of Edge Runtime limitations. Test middleware with different URL patterns."
---

Next.js middleware errors that occur when middleware is misconfigured, has incorrect response handling, or doesn't properly handle edge cases. Middleware runs on the Edge Runtime and has specific limitations.

## Solution

Ensure middleware.ts is in the project root. Handle all response cases including redirects. Use NextResponse correctly. Be aware of Edge Runtime limitations. Test middleware with different URL patterns.

## Code Example

```javascript
  "" // middleware.ts
  import { NextResponse } from 'next/server';
  import type { NextRequest } from 'next/server';
  
  // BAD: Not returning a response
  export function middleware(request: NextRequest) {
    const token = request.cookies.get('token');
    
    if (!token) {
      // Forgot to return response!
      NextResponse.redirect(new URL('/login', request.url));
    }
    // No else clause - continues without response
  }
  
  // GOOD: Proper middleware
  export function middleware(request: NextRequest) {
    const token = request.cookies.get('token');
    
    if (!token && request.nextUrl.pathname.startsWith('/dashboard')) {
      return NextResponse.redirect(new URL('/login', request.url));
    }
    
    return NextResponse.next();
  }
  
  export const config = {
    matcher: ['/dashboard/:path*', '/api/:path*']
  };
  
  // GOOD: Middleware with headers
  export function middleware(request: NextRequest) {
    const response = NextResponse.next();
    
    response.headers.set('x-custom-header', 'value');
    
    return response;
  }
  
  // GOOD: Middleware with rewrite
  export function middleware(request: NextRequest) {
    if (request.nextUrl.pathname.startsWith('/old-blog')) {
      return NextResponse.rewrite(
        new URL('/blog' + request.nextUrl.pathname.slice(10), request.url)
      );
    }
    
    return NextResponse.next();
  }
  
  // GOOD: Handle CORS in middleware
  export function middleware(request: NextRequest) {
    if (request.method === 'OPTIONS') {
      return new Response(null, {
        status: 200,
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        }
      });
    }
    
    const response = NextResponse.next();
    response.headers.set('Access-Control-Allow-Origin', '*');
    return response;
  }
```
