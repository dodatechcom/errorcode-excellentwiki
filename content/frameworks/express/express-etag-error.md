---
title: "[Solution] Express ETag Error"
description: "Fix Express ETag errors when conditional requests fail or ETags are generated incorrectly for dynamic content."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

An ETag error in Express occurs when the `ETag` header is generated incorrectly or conflicts with response compression, causing 304 responses to be served when the content has actually changed, or preventing valid caching.

## Common Causes

- ETag generated before response body is compressed
- Weak ETags used for binary responses
- ETag conflicts with `Content-Encoding` header
- Stale ETag served after content update
- `etag` setting disabled but clients expect conditional responses

## How to Fix

1. Control ETag generation through Express settings:

```javascript
// Disable ETags globally
app.set('etag', false);

// Use weak ETags (default)
app.set('etag', 'weak');

// Use strong ETags
app.set('etag', 'strong');
```

2. Generate custom ETags for dynamic content:

```javascript
const crypto = require('crypto');

app.get('/api/data', (req, res) => {
  const data = fetchData();
  const body = JSON.stringify(data);
  const etag = `"${crypto.createHash('md5').update(body).digest('hex')}"`;

  if (req.headers['if-none-match'] === etag) {
    return res.status(304).end();
  }

  res.set('ETag', etag);
  res.set('Cache-Control', 'private, max-age=0');
  res.json(data);
});
```

3. Handle ETag mismatches after data updates:

```javascript
app.put('/api/data', async (req, res) => {
  await updateData(req.body);
  const data = await fetchData();
  const etag = generateETag(data);

  // Include new ETag in response so client cache is updated
  res.set('ETag', etag);
  res.json(data);
});
```

## Examples

```javascript
// Bug: compression changes body after ETag is set
app.use(compression());
app.get('/api/report', (req, res) => {
  const report = generateReport();
  const etag = `"${hash(report)}"`;
  res.set('ETag', etag);
  res.json(report); // Body may be compressed, ETag no longer matches
});

// Fix: generate ETag after compression
// Use a middleware that runs after compression
app.use(compression());
app.use((req, res, next) => {
  const originalSend = res.send;
  res.send = function(body) {
    const etag = `"${hash(body)}"`;
    if (req.headers['if-none-match'] === etag) {
      return res.status(304).end();
    }
    res.set('ETag', etag);
    return originalSend.call(this, body);
  };
  next();
});
```

```text
304 Not Modified served incorrectly when content changed
```
