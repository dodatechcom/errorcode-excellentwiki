---
title: "[Solution] Express Cache Control Error"
description: "Fix Express cache control errors when responses are cached incorrectly or cache headers are missing."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

A cache control error in Express occurs when the `Cache-Control` header is not set correctly, causing browsers or CDNs to cache responses that should not be cached, or failing to cache static assets.

## Common Causes

- No `Cache-Control` headers set on API responses
- Static assets served without long cache durations
- Sensitive data cached by intermediate proxies
- `no-store` and `no-cache` used incorrectly
- CDN ignores cache headers due to missing `s-maxage`

## How to Fix

1. Set cache headers for different content types:

```javascript
// API responses -- no cache
app.use('/api', (req, res, next) => {
  res.set('Cache-Control', 'no-store, no-cache, must-revalidate, proxy-revalidate');
  res.set('Pragma', 'no-cache');
  res.set('Expires', '0');
  next();
});

// Static assets -- long cache with versioned filenames
app.use('/static', express.static('public', {
  maxAge: '1y',
  immutable: true
}));
```

2. Use the `nocache` middleware for API routes:

```javascript
const nocache = require('nocache');
app.use('/api', nocache());
```

3. Implement ETag-based caching for dynamic content:

```javascript
app.get('/api/data', (req, res) => {
  const data = generateData();
  const etag = calculateHash(data);

  if (req.headers['if-none-match'] === etag) {
    return res.status(304).end();
  }

  res.set('ETag', etag);
  res.set('Cache-Control', 'private, max-age=0, must-revalidate');
  res.json(data);
});
```

## Examples

```javascript
// Bug: API responses cached by browser
app.get('/api/user/profile', (req, res) => {
  res.json(getUserProfile(req.user.id));
  // Browser caches this -- next request returns stale data
});

// Fixed
app.get('/api/user/profile', (req, res) => {
  res.set('Cache-Control', 'private, no-cache');
  res.json(getUserProfile(req.user.id));
});
```

```text
Cache-Control headers missing or misconfigured
```
