---
title: "[Solution] Express Rate Limit Retry-After Error"
description: "Fix Express rate limit retry-after errors when clients do not receive or respect the Retry-After header."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

A rate limit retry-after error in Express occurs when the rate limiter sends a `Retry-After` header but the client does not implement proper backoff logic, causing repeated 429 responses.

## Common Causes

- Client does not read the `Retry-After` header from 429 responses
- No `Retry-After` header sent by the rate limiter
- Client retries immediately without waiting
- Multiple rate limiters conflict and produce different limits
- Rate limit keys do not identify clients correctly

## How to Fix

1. Configure the rate limiter to send Retry-After:

```javascript
const rateLimit = require('express-rate-limit');

const limiter = rateLimit({
  windowMs: 60 * 1000,
  max: 100,
  standardHeaders: true,
  legacyHeaders: false,
  message: { error: 'Too many requests' }
});

app.use(limiter);
```

2. Implement client-side retry with exponential backoff:

```javascript
async function fetchWithRetry(url, options, maxRetries = 3) {
  for (let i = 0; i < maxRetries; i++) {
    const response = await fetch(url, options);

    if (response.status === 429) {
      const retryAfter = response.headers.get('Retry-After') || Math.pow(2, i);
      await new Promise(resolve => setTimeout(resolve, retryAfter * 1000));
      continue;
    }

    return response;
  }
  throw new Error('Max retries exceeded');
}
```

3. Use different rate limits for different endpoints:

```javascript
const apiLimiter = rateLimit({ windowMs: 60000, max: 100 });
const authLimiter = rateLimit({ windowMs: 60000, max: 5 });

app.use('/api', apiLimiter);
app.use('/auth', authLimiter);
```

## Examples

```javascript
// Bug: custom handler does not set Retry-After
const limiter = rateLimit({
  windowMs: 60000,
  max: 10,
  handler: (req, res) => {
    res.status(429).json({ error: 'Slow down' }); // No Retry-After
  }
});

// Fixed: include Retry-After header
const limiter = rateLimit({
  windowMs: 60000,
  max: 10,
  handler: (req, res) => {
    const retryAfter = Math.ceil(60 - (Date.now() % 60000) / 1000);
    res.set('Retry-After', retryAfter.toString());
    res.status(429).json({ error: 'Slow down', retryAfter });
  }
});
```

```text
429 Too Many Requests
```
