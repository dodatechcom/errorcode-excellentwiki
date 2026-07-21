---
title: "[Solution] React Middleware Response Error"
description: "Middleware response wrong."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Middleware response wrong.

## Common Causes

Not returning Response.

## How to Fix

Return NextResponse.

## Example

```javascript
import { NextResponse } from 'next/server';
export function middleware(req) { return NextResponse.next(); }
```
