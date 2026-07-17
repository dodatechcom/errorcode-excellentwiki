---
title: "[Solution] Netlify Lambda Function Timeout Error — Fix Function Duration"
description: "Fix Netlify Lambda function timeout errors. Resolve function execution limits, cold start delays, and duration issues."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
weight: 9
---

A Netlify Lambda function timeout error occurs when a serverless function exceeds its maximum execution time. Netlify Functions on the free tier have a 10-second limit, extended to 26 seconds on Pro plans.

## What This Error Means

When a function runs longer than allowed, Netlify terminates it and returns a timeout error:

```
Function timed out
Runtime.ExitError
```

The function was invoked but did not complete its execution within the duration limit.

## Why It Happens

- The function performs slow database queries
- External API calls are unresponsive or slow
- The function processes large datasets synchronously
- Cold start initialization takes too long
- The function has a deadlock or infinite loop
- Network latency to external services is high

## How to Fix It

### Reduce Function Execution Time

```javascript
// netlify/functions/fast-query.js
exports.handler = async (event) => {
  // Use indexed queries
  const result = await db.query(
    'SELECT id, name FROM users WHERE active = $1 LIMIT 100',
    [true]
  );

  return {
    statusCode: 200,
    body: JSON.stringify(result.rows),
  };
};
```

### Move Heavy Work to Background

```javascript
// netlify/functions/process-order.js
exports.handler = async (event) => {
  const { orderId } = JSON.parse(event.body);

  // Queue for background processing
  await queue.publish('order-processing', { orderId });

  return {
    statusCode: 202,
    body: JSON.stringify({
      message: 'Order queued for processing',
      orderId,
    }),
  };
};
```

### Use Connection Pooling

```javascript
// Keep database connection outside handler
const { Pool } = require('pg');

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  max: 5,
});

exports.handler = async (event) => {
  const client = await pool.connect();
  try {
    const result = await client.query('SELECT * FROM users');
    return { statusCode: 200, body: JSON.stringify(result.rows) };
  } finally {
    client.release();
  }
};
```

### Cache Repeated Results

```javascript
// netlify/functions/cached-data.js
const cache = new Map();

exports.handler = async (event) => {
  const cacheKey = 'expensive-data';

  if (cache.has(cacheKey)) {
    const { data, timestamp } = cache.get(cacheKey);
    if (Date.now() - timestamp < 60000) {
      return { statusCode: 200, body: JSON.stringify(data) };
    }
  }

  const data = await fetchExpensiveData();
  cache.set(cacheKey, { data, timestamp: Date.now() });

  return { statusCode: 200, body: JSON.stringify(data) };
};
```

### Optimize Dependencies

```bash
# Check function size
ls -la netlify/functions/*.js

# Use tree-shaking to reduce bundle size
# Remove unused imports
# Use dynamic imports for heavy libraries
```

```javascript
// Use dynamic imports for heavy modules
exports.handler = async (event) => {
  const { default: heavyLib } = await import('heavy-library');
  const result = heavyLib.process(event.body);
  return { statusCode: 200, body: JSON.stringify(result) };
};
```

### Split Large Functions

```javascript
// Instead of one large function, split by concern
// netlify/functions/get-users.js
// netlify/functions/create-user.js
// netlify/functions/delete-user.js
```

## Common Mistakes

- Not testing function execution time locally
- Using synchronous HTTP calls instead of parallel
- Not managing database connections properly
- Including heavy dependencies that slow cold starts
- Not monitoring function duration in production

## Related Pages

- [Netlify Functions Error]({{< relref "/tools/netlify/netlify-functions-error" >}}) — Serverless function error
- [Netlify Build Error]({{< relref "/tools/netlify/netlify-build-error" >}}) — Build failed
