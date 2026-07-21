---
title: "[Solution] Vercel Request Body Error"
description: "Fix Vercel request body errors when parsing or reading request bodies fails."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vercel Request Body Error

Vercel fails to parse request bodies in API routes.

```
SyntaxError: Unexpected token in JSON at position 0
```

## Common Causes

- Body not parsed automatically
- Content-Type header missing
- Body exceeds size limit
- Request body already consumed
- Using wrong method to read body

## How to Fix

### Parse JSON Body

```javascript
// pages/api/body.js
export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const body = JSON.parse(req.body);
  res.status(200).json({ received: body });
}
```

### Use req.json() for App Router

```typescript
// app/api/route.ts
export async function POST(request: Request) {
  const body = await request.json();
  return Response.json({ received: body });
}
```

### Handle FormData

```javascript
// API route for file uploads
export const config = {
  api: { bodyParser: false }
};

export default async function handler(req, res) {
  const formData = await req.formData();
  const file = formData.get('file');
  // Process file
}
```

### Handle Large Bodies

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

### Read Raw Body

```javascript
export default async function handler(req, res) {
  const chunks = [];
  for await (const chunk of req) {
    chunks.push(chunk);
  }
  const rawBody = Buffer.concat(chunks).toString();
  res.status(200).json({ raw: rawBody });
}
```

## Examples

```javascript
// Complete body parsing example
export default async function handler(req, res) {
  try {
    const { name, email, message } = JSON.parse(req.body);
    
    if (!email) {
      return res.status(400).json({ error: 'Email required' });
    }
    
    res.status(200).json({ name, email, message });
  } catch (error) {
    res.status(400).json({ error: 'Invalid JSON body' });
  }
}
```
