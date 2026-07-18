---
title: "[Solution] Vercel Serverless Function Timeout Error — How to Fix"
description: "Fix Vercel serverless function timeouts. Resolve cold start delays, long-running requests, and execution duration limit issues."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["error"]
weight: 1
comments: true
---

A Vercel serverless function timeout occurs when a serverless function exceeds the maximum execution time allowed by your Vercel plan. The function is terminated and returns a timeout error to the client.

## What This Error Means

Vercel serverless functions have strict execution time limits: 10 seconds on Hobby, 60 seconds on Pro, and up to 900 seconds on Enterprise. When a function exceeds this limit, Vercel kills the process and returns a `FUNCTION_INVOCATION_TIMEOUT` error. The function's response is never sent to the client.

## Why It Happens

- Long-running database queries without proper indexing
- Slow external API calls blocking the function
- Heavy synchronous processing of large datasets
- Cold starts with large dependencies (bundled node_modules)
- Missing connection pooling causing repeated connection establishment
- File processing operations (image resize, PDF generation) taking too long
- Sequential API calls that could be parallelized
- The function is doing work that should be offloaded to a background job

## Common Error Messages

- `FUNCTION_INVOCATION_TIMEOUT` — Function exceeded execution time limit
- `FUNCTION_INVOCATION_BODY_TOO_LARGE` — Request body too large
- `FUNCTION_TIMEOUT` — Function did not complete in time
- `Your function's execution time exceeded the maximum` — Plan limit exceeded
- `FUNCTION_RESPONSE_TIMEOUT` — Function took too long to send response

## How to Fix It

### Increase Function Duration

```json
// vercel.json
{
  "functions": {
    "api/quick-endpoint.js": {
      "maxDuration": 10
    },
    "api/heavy-report.js": {
      "maxDuration": 60
    },
    "api/data-export.js": {
      "maxDuration": 300
    }
  }
}
```

### Optimize Database Queries

```javascript
// WRONG: N+1 query pattern
const users = await db.query('SELECT * FROM users');
for (const user of users) {
  user.posts = await db.query('SELECT * FROM posts WHERE user_id = ?', [user.id]);
}

// RIGHT: JOIN query
const usersWithPosts = await db.query(`
  SELECT u.*, p.title, p.body
  FROM users u
  LEFT JOIN posts p ON u.id = p.user_id
  WHERE u.id = ?
`, [userId]);

// RIGHT: Use connection pooling
import { Pool } from 'pg';

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  max: 5, // Keep connections alive across invocations
});

export default async function handler(req, res) {
  const client = await pool.connect();
  try {
    const result = await client.query('SELECT * FROM users');
    res.json(result.rows);
  } finally {
    client.release();
  }
}
```

### Use Edge Functions Instead

```javascript
// Edge functions run at the edge with lower latency and no cold starts
// File: api/fast-endpoint.js (in edge runtime)

export const config = {
  runtime: 'edge',
};

export default async function handler(request) {
  const url = new URL(request.url);
  const id = url.searchParams.get('id');

  // Edge functions are ideal for:
  // - Authentication checks
  // - Header manipulation
  // - A/B testing
  // - Geolocation-based routing
  const data = { id, timestamp: Date.now() };

  return new Response(JSON.stringify(data), {
    headers: { 'Content-Type': 'application/json' },
  });
}
```

### Implement Background Tasks

```javascript
// WRONG: Do everything in the function
export default async function handler(req, res) {
  const data = await fetchAllData();       // 5s
  const processed = await processData(data); // 10s
  await sendEmails(processed);              // 15s
  await updateDatabase(processed);          // 5s
  // Total: 35s — may timeout on Hobby plan
}

// RIGHT: Return quickly, process in background
export default async function handler(req, res) {
  // Start background processing
  const jobId = await createJob(req.body);

  // Return immediately with job ID
  res.json({
    status: 'processing',
    jobId,
    checkUrl: `/api/job-status/${jobId}`,
  });
}
```

### Cache Expensive Results

```javascript
import { kv } from '@vercel/kv';

export default async function handler(req, res) {
  const cacheKey = `report:${req.query.period}`;

  // Check cache first
  const cached = await kv.get(cacheKey);
  if (cached) {
    return res.json(cached);
  }

  // Generate report (expensive operation)
  const report = await generateReport(req.query.period);

  // Cache for 1 hour
  await kv.set(cacheKey, report, { ex: 3600 });

  res.json(report);
}
```

## Common Scenarios

- **Cold start + heavy import:** A function imports a large library at initialization, causing cold starts to exceed the timeout before any request processing begins.
- **Unindexed database query:** A function queries a table with millions of rows without an index, causing the query to scan the entire table.
- **Synchronous API chain:** A function calls three external APIs sequentially, each taking 15 seconds, totaling 45 seconds and exceeding the Hobby plan limit.

## Prevent It

1. Monitor function execution duration in Vercel Analytics and set up alerts for functions approaching 80% of the time limit
2. Use Edge Functions for lightweight tasks that do not need Node.js APIs
3. Implement connection pooling and caching to reduce the work done per invocation

## Related Pages

- [Vercel Build Timeout Error]({{< relref "/tools/vercel/vercel-build-timeout-error" >}}) — Build time exceeded
- [Vercel Edge Function Error]({{< relref "/tools/vercel/vercel-edge-function-error" >}}) — Edge function error
