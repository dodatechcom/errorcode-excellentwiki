---
title: "[Solution] Vercel Serverless Function Timeout Error — Fix Function Limits"
description: "Fix Vercel serverless function timeouts. Resolve function execution limits, cold starts, and timeout configuration."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["error"]
weight: 3
---

A Vercel serverless function timeout occurs when a function exceeds the maximum execution time allowed by your plan. Vercel limits function duration to 10 seconds (Hobby), 60 seconds (Pro), or longer with Enterprise configuration.

## What This Error Means

When a serverless function runs too long, Vercel terminates it and returns a timeout error:

```
FUNCTION_INVOCATION_TIMEOUT
Function has timed out
```

The function was invoked but did not complete within the allowed duration.

## Why It Happens

- The function performs long-running database queries
- External API calls are slow or unresponsive
- The function processes large amounts of data synchronously
- Cold starts take too long due to heavy dependencies
- The function is performing tasks that should be async
- Network latency to external services is high

## How to Fix It

### Increase Function Timeout

```json
// vercel.json
{
  "functions": {
    "api/long-task.js": {
      "maxDuration": 30
    },
    "api/report.js": {
      "maxDuration": 60
    }
  }
}
```

### Optimize Database Queries

```javascript
// Slow query
const users = await db.query(
  'SELECT * FROM orders WHERE created_at > ?',
  [startDate]
);

// Optimized query with index
const users = await db.query(
  'SELECT id, name, total FROM orders WHERE created_at > ? LIMIT 100',
  [startDate]
);
```

### Use Streaming Responses

```javascript
// Stream large responses
export default async function handler(req, res) {
  const data = await fetchData();
  res.setHeader('Content-Type', 'application/json');
  res.setHeader('Transfer-Encoding', 'chunked');

  // Send data in chunks
  for (const chunk of data) {
    res.write(JSON.stringify(chunk));
  }
  res.end();
}
```

### Handle Cold Starts

```javascript
// Keep connections warm
import { withDB } from '@/lib/db';

// Initialize connection outside handler
const db = await withDB();

export default async function handler(req, res) {
  const result = await db.query('SELECT * FROM users');
  res.json(result);
}
```

### Move Heavy Tasks to Background

```javascript
// Instead of doing everything in the function
export default async function handler(req, res) {
  // Start background job
  const job = await triggerBackgroundJob(req.body);

  // Return immediately
  res.json({
    status: 'processing',
    jobId: job.id,
    checkUrl: `/api/job-status/${job.id}`
  });
}
```

### Use Vercel KV or Redis for Caching

```javascript
import { kv } from '@vercel/kv';

export default async function handler(req, res) {
  const cacheKey = `data:${req.query.id}`;

  // Check cache first
  const cached = await kv.get(cacheKey);
  if (cached) {
    return res.json(cached);
  }

  // Fetch from database
  const data = await fetchExpensiveData();

  // Cache for 5 minutes
  await kv.set(cacheKey, data, { ex: 300 });

  res.json(data);
}
```

## Common Mistakes

- Not monitoring function execution duration
- Making multiple sequential API calls instead of parallel
- Not using connection pooling for databases
- Storing large objects in the function instead of using KV
- Not setting up alerts for approaching timeout limits

## Related Pages

- [Vercel Deploy Error]({{< relref "/tools/vercel/vercel-deploy-error" >}}) — Deployment failed
- [Vercel Edge Function Error]({{< relref "/tools/vercel/vercel-edge-function-error" >}}) — Edge function error
