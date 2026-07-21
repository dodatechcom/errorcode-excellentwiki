---
title: "[Solution] Next.js Middleware Rewrite Error"
description: "Middleware rewrite not working."
frameworks: ["nextjs"]
error-types: ["framework-error"]
severities: ["error"]
---

Middleware rewrite not working.

## Common Causes

Wrong usage.

## How to Fix

Use NextResponse.rewrite.

## Example

```javascript
import { NextResponse } from 'next/server';
export function middleware(req) {
  return NextResponse.rewrite(new URL('/new', req.url));
}
```
