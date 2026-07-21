---
title: "[Solution] Vercel API Route Error"
description: "Fix Vercel API route errors when serverless API functions fail to respond correctly."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vercel API Route Error

Vercel API routes return errors or fail to respond as expected.

```
500: INTERNAL_SERVER_ERROR
FUNCTION_INVOCATION_TIMEOUT
```

## Common Causes

- API function exceeds execution timeout
- Missing export of default handler
- Request body too large
- Invalid JSON in response
- Missing environment variables

## How to Fix

### Check API Route Structure

```javascript
// pages/api/endpoint.js
export default function handler(req, res) {
  if (req.method !== 'GET') {
    return res.status(405).json({ error: 'Method not allowed' });
  }
  res.status(200).json({ data: 'success' });
}
```

### Handle Timeout

```javascript
// Increase function duration in vercel.json
{
  "functions": {
    "api/**/*.js": {
      "maxDuration": 30
    }
  }
}
```

### Handle Large Request Bodies

```javascript
// vercel.json
{
  "functions": {
    "api/upload.js": {
      "maxDuration": 60,
      "memory": 1024
    }
  }
}
```

### Fix Next.js App Router

```typescript
// app/api/route.ts
import { NextResponse } from 'next/server';

export async function GET() {
  return NextResponse.json({ data: 'hello' });
}

export async function POST(request: Request) {
  const body = await request.json();
  return NextResponse.json({ received: body });
}
```

### Check Environment Variables

```bash
# Verify variables are set
vercel env ls

# Add variable
vercel env add API_KEY production
```

## Examples

```javascript
// Complete API route with error handling
export default async function handler(req, res) {
  try {
    const { url } = req.query;
    const response = await fetch(url);
    const data = await response.json();
    res.status(200).json(data);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
}
```
