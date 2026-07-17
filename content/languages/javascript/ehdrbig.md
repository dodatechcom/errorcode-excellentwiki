---
title: "[Solution] ERR_HTTP_HEADERS_SENT: headers already sent Error Fix"
description: "Fix ERR_HTTP_HEADERS_SENT: Cannot set headers after they are sent to the client. Handle HTTP response headers properly in Node.js."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ERR_HTTP_HEADERS_SENT — headers already sent

This error occurs when you try to set HTTP response headers after they have already been sent to the client. Once headers are sent, they cannot be modified.

## What This Error Means

Common error messages:

- `Error [ERR_HTTP_HEADERS_SENT]: Cannot set headers after they are sent to the client`
- `HTTPError: Headers have already been sent`
- `Error: Can't set headers after they are sent to the client`

HTTP headers must be set before calling `res.end()` or `res.write()`. After the first write, headers are flushed to the client.

## Common Causes

```javascript
// Cause 1: Multiple res.send() calls
app.get('/api', (req, res) => {
  res.send('first');
  res.send('second'); // ERR_HTTP_HEADERS_SENT
});

// Cause 2: Sending response in async callback after response already sent
app.get('/api', async (req, res) => {
  res.json({ status: 'ok' });
  const data = await fetchExternalApi();
  res.json(data); // already sent
});

// Cause 3: Error handler calling res.send after response
app.use((err, req, res, next) => {
  res.status(500).send('error');
  next(err); // might trigger another response
});

// Cause 4: Redirect after sending
res.send('hello');
res.redirect('/other'); // ERR_HTTP_HEADERS_SENT
```

## How to Fix

### Fix 1: Use return after res.send/json

```javascript
app.get('/api', (req, res) => {
  if (!req.user) {
    return res.status(401).json({ error: 'unauthorized' });
  }
  res.json({ data: 'secret' });
});
```

### Fix 2: Use a flag to prevent double response

```javascript
app.get('/api', async (req, res) => {
  let responded = false;

  try {
    const data = await fetchData();
    if (!responded) {
      responded = true;
      res.json(data);
    }
  } catch (err) {
    if (!responded) {
      responded = true;
      res.status(500).json({ error: err.message });
    }
  }
});
```

### Fix 3: Use next() to chain middleware safely

```javascript
app.get('/api', (req, res, next) => {
  if (!req.authenticated) {
    return res.status(401).json({ error: 'unauthorized' });
  }
  next();
});

app.get('/api', (req, res) => {
  res.json({ data: 'success' });
});
```

### Fix 4: Check res.headersSent before writing

```javascript
app.use((err, req, res, next) => {
  if (res.headersSent) {
    return next(err);
  }
  res.status(500).json({ error: 'Internal server error' });
});
```

## Examples

```javascript
const http = require('http');

// This triggers ERR_HTTP_HEADERS_SENT
const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Hello');
  res.writeHead(404); // Error: Can't set headers after they are sent
});
```

## Related Errors

- [ECONNREFUSED]({{< relref "/languages/javascript/econnrefused-node" >}}) — connection refused
- [Express Route 404]({{< relref "/languages/javascript/express-route" >}}) — route not found
- [Express Middleware]({{< relref "/languages/javascript/express-middleware" >}}) — middleware error
