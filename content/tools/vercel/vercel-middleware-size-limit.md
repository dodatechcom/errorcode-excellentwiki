---
title: "[Solution] Vercel Middleware Size Limit"
description: "Fix Vercel middleware size limit errors when the middleware bundle exceeds the maximum size."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Vercel deployment fails because the middleware file exceeds the 200 KB size limit for Edge Functions.

## Common Causes

- Large imports included in middleware
- Bundling unnecessary dependencies
- Middleware handles too many concerns
- Third-party SDKs imported in middleware
- Node.js-only modules used in Edge runtime

## How to Fix

- Move heavy logic to Serverless Functions called from middleware
- Use dynamic imports to reduce bundle size
- Remove unused imports and dependencies
- Keep middleware focused on edge-compatible tasks

## Examples

```typescript
// middleware.ts - keep it lean
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  if (request.nextUrl.pathname === '/api/heavy') {
    return NextResponse.rewrite(new URL('/api/handler', request.url));
  }
  return NextResponse.next();
}

export const config = {
  matcher: ['/((?!api|_next/static|_next/image|favicon.ico).*)'],
};
```
