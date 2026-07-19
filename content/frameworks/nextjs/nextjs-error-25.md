---
title: "Next.js middleware CORS errors"
description: "Next.js middleware errors related to Cross-Origin Resource Sharing (CORS). Common issues include missing CORS headers, incorrect header configuration, or preflight request handling failures."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "nextjs"
tags: ["error", "middleware", "cors", "headers"]
severity: "error"
solution: "Configure CORS headers in middleware for API routes. Handle OPTIONS preflight requests properly. Use environment variables for allowed origins. Test CORS configuration with different browsers."
---

Next.js middleware errors related to Cross-Origin Resource Sharing (CORS). Common issues include missing CORS headers, incorrect header configuration, or preflight request handling failures.

## Solution

Configure CORS headers in middleware for API routes. Handle OPTIONS preflight requests properly. Use environment variables for allowed origins. Test CORS configuration with different browsers.

## Code Example

```javascript
  // BAD: Missing CORS headers
  // middleware.ts
  import { NextResponse } from 'next/server';
  
  export function middleware(request) {
    return NextResponse.next(); // No CORS headers!
  }
  
  // GOOD: Proper CORS configuration
  import { NextResponse } from 'next/server';
  import type { NextRequest } from 'next/server';
  
  const ALLOWED_ORIGINS = [
    'https://example.com',
    'https://app.example.com',
  ];
  
  export function middleware(request: NextRequest) {
    const origin = request.headers.get('origin');
    const isAllowedOrigin = ALLOWED_ORIGINS.includes(origin || '');
    
    // Handle preflight
    if (request.method === 'OPTIONS') {
      return new Response(null, {
        status: 200,
        headers: {
          'Access-Control-Allow-Origin': isAllowedOrigin ? origin! : '',
          'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
          'Access-Control-Allow-Headers': 'Content-Type, Authorization',
          'Access-Control-Max-Age': '86400',
        },
      });
    }
    
    const response = NextResponse.next();
    
    if (isAllowedOrigin) {
      response.headers.set('Access-Control-Allow-Origin', origin!);
    }
    
    return response;
  }
  
  export const config = {
    matcher: '/api/:path*',
  };
```
