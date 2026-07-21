---
title: "[Solution] Vercel HTTP Status Code Error"
description: "Fix Vercel HTTP status code errors when returning incorrect status codes from functions."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["warning"]
---

# Vercel HTTP Status Code Error

Vercel returns incorrect HTTP status codes from serverless functions or pages.

```
Error: Expected status 200, got 500
```

## Common Causes

- Missing status code in response
- Error handler returning wrong status
- Redirect loop producing 302 chain
- Cache headers causing stale responses
- Function crashing without error handling

## How to Fix

### Set Correct Status Code

```javascript
// pages/api/status.js
export default function handler(req, res) {
  res.status(200).json({ status: 'ok' });
}
```

### Handle Error Responses

```javascript
export default function handler(req, res) {
  try {
    // Success
    res.status(200).json({ data: result });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
}
```

### Return 404 for Missing Resources

```javascript
export default function handler(req, res) {
  const item = findItem(req.query.id);
  if (!item) {
    return res.status(404).json({ error: 'Not found' });
  }
  res.status(200).json(item);
}
```

### Use Next.js Response Helpers

```typescript
// app/api/route.ts
import { NextResponse } from 'next/server';

export async function GET() {
  return NextResponse.json({ ok: true }, { status: 200 });
}
```

### Check Redirect Status

```json
// vercel.json
{
  "redirects": [
    { "from": "/old", "to": "/new", "statusCode": 301 }
  ]
}
```

## Examples

```javascript
// Proper status code handling
export default function handler(req, res) {
  switch (req.method) {
    case 'GET':
      return res.status(200).json({ data: 'ok' });
    case 'POST':
      return res.status(201).json({ created: true });
    case 'DELETE':
      return res.status(204).end();
    default:
      return res.status(405).json({ error: 'Method not allowed' });
  }
}
```
