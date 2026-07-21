---
title: "[Solution] Express Request Aborted Error"
description: "Fix Express request aborted errors when clients disconnect before the server finishes processing."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

A request aborted error in Express occurs when the client disconnects before the server finishes sending a response. This causes write errors and unhandled exceptions in the request handler.

## Common Causes

- Client closes the browser tab while request is processing
- Network timeout before server responds
- Long-running database query exceeds client timeout
- Streaming response interrupted by client disconnect
- `req.on('abort')` handler missing

## How to Fix

1. Listen for the `close` event on the request:

```javascript
app.get('/api/slow', async (req, res) => {
  req.on('close', () => {
    console.log(`Request ${req.id} aborted by client`);
    // Abort any ongoing work
  });

  try {
    const data = await longRunningQuery();
    res.json(data);
  } catch (err) {
    if (err.code === 'ECONNRESET') return;
    next(err);
  }
});
```

2. Handle write errors gracefully:

```javascript
app.get('/api/stream', (req, res) => {
  const stream = getDataStream();

  stream.on('data', (chunk) => {
    const ok = res.write(chunk);
    if (!ok) {
      stream.pause();
      res.once('drain', () => stream.resume());
    }
  });

  stream.on('end', () => res.end());

  res.on('error', (err) => {
    if (err.code === 'ECONNRESET') {
      stream.destroy();
    }
  });
});
```

3. Use a timeout to detect stalled requests:

```javascript
app.get('/api/data', async (req, res) => {
  const timeout = setTimeout(() => {
    if (!res.headersSent) {
      res.status(504).json({ error: 'Gateway timeout' });
    }
  }, 30000);

  try {
    const data = await fetchData();
    clearTimeout(timeout);
    res.json(data);
  } catch (err) {
    clearTimeout(timeout);
    if (err.code === 'ECONNRESET') return;
    next(err);
  }
});
```

## Examples

```javascript
// Bug: writes to a closed connection
app.get('/api/export', async (req, res) => {
  const data = await generateReport();
  res.write(JSON.stringify(data)); // Error if client disconnected
  res.end();
});

// Fixed: check connection state
app.get('/api/export', async (req, res) => {
  const data = await generateReport();
  if (res.writableFinished || req.destroyed) return;
  res.json(data);
});
```

```text
Error [ERR_STREAM_WRITE_AFTER_END]: write after end
Error: aborted
```
