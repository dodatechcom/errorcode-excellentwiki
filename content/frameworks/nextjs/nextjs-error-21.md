---
title: "Next.js middleware rewrites and redirects errors"
description: "Next.js errors related to middleware rewrites and redirects. Common issues include infinite redirect loops, incorrect URL construction, or rewrite rules that don't match expected patterns."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "nextjs"
tags: ["error", "middleware", "rewrites", "redirects"]
severity: "error"
solution: "Test rewrites and redirects thoroughly. Avoid redirect loops by checking the target path. Use URL constructor for proper URL building. Implement proper middleware matching patterns."
---

Next.js errors related to middleware rewrites and redirects. Common issues include infinite redirect loops, incorrect URL construction, or rewrite rules that don't match expected patterns.

## Solution

Test rewrites and redirects thoroughly. Avoid redirect loops by checking the target path. Use URL constructor for proper URL building. Implement proper middleware matching patterns.

## Code Example

```javascript
  // BAD: Infinite redirect loop
  import { NextResponse } from 'next/server';
  
  export function middleware(request) {
    // Always redirects to /login, causing loop!
    return NextResponse.redirect(new URL('/login', request.url));
  }
  
  // GOOD: Conditional redirect with loop prevention
  import { NextResponse } from 'next/server';
  import type { NextRequest } from 'next/server';
  
  export function middleware(request: NextRequest) {
    const { pathname } = request.nextUrl;
    const token = request.cookies.get('token');
    
    // Don't redirect if already on login page
    if (pathname === '/login') {
      return NextResponse.next();
    }
    
    // Only redirect unprotected routes
    if (pathname.startsWith('/dashboard') && !token) {
      return NextResponse.redirect(new URL('/login', request.url));
    }
    
    return NextResponse.next();
  }
  
  // GOOD: Proper rewrite
  export function middleware(request: NextRequest) {
    const { pathname } = request.nextUrl;
    
    // Rewrite /blog/:slug to /posts/:slug
    if (pathname.startsWith('/blog/')) {
      const slug = pathname.slice(6); // Remove '/blog/'
      return NextResponse.rewrite(new URL(`/posts/${slug}`, request.url));
    }
    
    return NextResponse.next();
  }
  
  // GOOD: Rewrite with header
  export function middleware(request: NextRequest) {
    const response = NextResponse.next();
    
    if (request.nextUrl.pathname.startsWith('/api')) {
      response.headers.set('x-api-version', 'v1');
    }
    
    return response;
  }
  
  // GOOD: Redirect with query params
  export function middleware(request: NextRequest) {
    if (request.nextUrl.pathname === '/old-page') {
      const newUrl = new URL('/new-page', request.url);
      // Preserve query parameters
      newUrl.search = request.nextUrl.search;
      return NextResponse.redirect(newUrl);
    }
    
    return NextResponse.next();
  }
  
  export const config = {
    matcher: ['/old-page', '/blog/:path*']
  };
```
