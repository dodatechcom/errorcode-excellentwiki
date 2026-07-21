---
title: "[Solution] Vercel Edge Function Error"
description: "Fix Vercel Edge Function errors when Deno-based edge functions fail to execute."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vercel Edge Function Error

Vercel Edge Functions fail to execute or return errors.

```
EDGE_FUNCTION_INVOCATION_TIMEOUT
Edge Function has crashed
```

## Common Causes

- Edge function exceeds 30-second limit
- Using Node.js APIs not available in Deno
- Import path issues
- Missing environment variables in Edge runtime
- Memory limit exceeded

## How to Fix

### Configure Edge Function

```javascript
// edge-functions/hello.js
export const config = { runtime: 'edge' };

export default async function handler(request) {
  return new Response(JSON.stringify({ hello: 'world' }), {
    headers: { 'content-type': 'application/json' }
  });
}
```

### Use Edge Runtime in Next.js

```typescript
// app/api/edge/route.ts
export const runtime = 'edge';

export async function GET() {
  return Response.json({ runtime: 'edge' });
}
```

### Handle Environment Variables

```typescript
// Edge functions use process.env
export const runtime = 'edge';

export async function GET() {
  const apiKey = process.env.API_KEY;
  return Response.json({ apiKey: apiKey ? 'set' : 'not set' });
}
```

### Fix Import Issues

```javascript
// Use URL imports in Edge runtime
import { serve } from "https://deno.land/std@0.177.0/http/server.ts";

// Or use Vercel's @vercel/edge package
import { geolocation } from '@vercel/edge';
```

### Limit Function Duration

```json
// vercel.json
{
  "functions": {
    "edge-functions/**": {
      "maxDuration": 30
    }
  }
}
```

## Examples

```typescript
// Edge middleware with geolocation
import { NextResponse } from 'next/server';
import { geolocation } from '@vercel/edge';

export const config = { runtime: 'edge' };

export function middleware(request) {
  const geo = geolocation(request);
  return NextResponse.rewrite(`/location/${geo?.country}`);
}
```
