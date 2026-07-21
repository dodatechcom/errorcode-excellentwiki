---
title: "[Solution] Express Response Time Error"
description: "Fix Express response time errors when the X-Response-Time header is missing or reports incorrect values."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

A response time error in Express occurs when the application fails to track or report how long requests take to process, making it difficult to identify slow endpoints and performance bottlenecks.

## Common Causes

- No response time tracking middleware configured
- `X-Response-Time` header set after `res.send()` already sent
- Timer started too early or too late in the middleware chain
- Response time calculated incorrectly across async boundaries
- Performance monitoring tool not receiving timing data

## How to Fix

1. Use the `response-time` middleware:

```javascript
const responseTime = require('response-time');

app.use(responseTime({ digits: 3, header: 'X-Response-Time' }));
```

2. Create a custom timing middleware:

```javascript
app.use((req, res, next) => {
  const start = process.hrtime.bigint();

  res.on('finish', () => {
    const end = process.hrtime.bigint();
    const durationMs = Number(end - start) / 1e6;
    res.set('X-Response-Time', `${durationMs.toFixed(2)}ms`);
    console.log(`${req.method} ${req.url} ${res.statusCode} ${durationMs.toFixed(2)}ms`);
  });

  next();
});
```

3. Log slow requests with a threshold:

```javascript
app.use((req, res, next) => {
  const start = Date.now();
  res.on('finish', () => {
    const duration = Date.now() - start;
    if (duration > 1000) {
      console.warn(`SLOW: ${req.method} ${req.url} took ${duration}ms`);
    }
  });
  next();
});
```

## Examples

```javascript
// Bug: timing set after response sent
app.get('/api/data', async (req, res) => {
  const data = await fetchData();
  res.json(data);
  res.set('X-Response-Time', '0ms'); // Too late -- header already sent
});

// Fixed: middleware runs before response
app.use((req, res, next) => {
  const start = Date.now();
  res.on('finish', () => {
    res.set('X-Response-Time', `${Date.now() - start}ms`);
  });
  next();
});

app.get('/api/data', async (req, res) => {
  const data = await fetchData();
  res.json(data); // X-Response-Time header included
});
```

```text
X-Response-Time header missing from response
```
