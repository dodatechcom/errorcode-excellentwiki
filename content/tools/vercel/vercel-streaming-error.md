---
title: "[Solution] Vercel Streaming Response Error"
description: "Fix Vercel streaming response errors when server-sent events or streaming fails."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vercel Streaming Response Error

Vercel streaming responses fail or return incomplete data.

```
Error: Response body is not a ReadableStream
```

## Common Causes

- Response not properly encoded as stream
- Edge runtime required but not specified
- Timeout before stream completes
- Missing Content-Type header
- Function crashing mid-stream

## How to Fix

### Use Streaming in Edge Runtime

```typescript
// app/api/stream/route.ts
export const runtime = 'edge';

export async function GET() {
  const encoder = new TextEncoder();
  const stream = new ReadableStream({
    start(controller) {
      controller.enqueue(encoder.encode('data: hello\n\n'));
      controller.close();
    }
  });

  return new Response(stream, {
    headers: {
      'Content-Type': 'text/event-stream',
      'Cache-Control': 'no-cache',
      'Connection': 'keep-alive'
    }
  });
}
```

### Use Next.js Streaming

```typescript
// app/page.tsx
export const runtime = 'edge';

export default async function Page() {
  return (
    <div>
      <h1>Streaming Page</h1>
      <Suspense fallback={<Loading />}>
        <SlowComponent />
      </Suspense>
    </div>
  );
}
```

### Server-Sent Events

```javascript
// pages/api/events.js
export default function handler(req, res) {
  res.setHeader('Content-Type', 'text/event-stream');
  res.setHeader('Cache-Control', 'no-cache');
  res.setHeader('Connection', 'keep-alive');

  const interval = setInterval(() => {
    res.write(`data: ${JSON.stringify({ time: Date.now() })}\n\n`);
  }, 1000);

  req.on('close', () => clearInterval(interval));
}
```

### Handle Stream Errors

```typescript
export async function GET() {
  const stream = new ReadableStream({
    start(controller) {
      try {
        controller.enqueue(new TextEncoder().encode('data'));
        controller.close();
      } catch (error) {
        controller.error(error);
      }
    }
  });

  return new Response(stream);
}
```

## Examples

```typescript
// AI streaming response
export const runtime = 'edge';

export async function POST(request: Request) {
  const { prompt } = await request.json();
  
  const response = await fetch('https://api.openai.com/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${process.env.OPENAI_KEY}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ model: 'gpt-3.5-turbo', messages: [{ role: 'user', content: prompt }] })
  });

  return new Response(response.body, {
    headers: { 'Content-Type': 'text/event-stream' }
  });
}
```
