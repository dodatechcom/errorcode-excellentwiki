---
title: "[Solution] Express Socket Hang Up Error"
description: "Fix Express socket hang up errors when the client disconnects before receiving the complete response."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

A socket hang up error in Express occurs when the client closes the TCP connection before the server finishes sending the response. This produces an `ECONNRESET` or `socket hang up` error in the server logs.

## Common Causes

- Client request timeout expires before server responds
- Reverse proxy closes connection before server finishes
- Server takes too long to start writing the response
- Large file download interrupted by client
- Keep-alive timeout on proxy is shorter than server processing time

## How to Fix

1. Send an early response acknowledgment for long operations:

```javascript
app.get('/api/report', async (req, res) => {
  res.setHeader('Content-Type', 'text/event-stream');
  res.flushHeaders();

  const steps = ['Querying database', 'Processing data', 'Generating report'];
  for (const step of steps) {
    res.write(`: ${step}\n\n`);
    await processStep(step);
  }

  const report = await generateReport();
  res.write(`data: ${JSON.stringify(report)}\n\n`);
  res.end();
});
```

2. Increase proxy keep-alive timeout:

```nginx
# nginx configuration
proxy_read_timeout 300s;
proxy_send_timeout 300s;
```

3. Handle ECONNRESET errors gracefully:

```javascript
app.get('/api/large', async (req, res, next) => {
  try {
    const data = await generateLargeDataset();
    res.json(data);
  } catch (err) {
    if (err.code === 'ECONNRESET' || err.message.includes('socket hang up')) {
      console.warn(`Client disconnected during request ${req.id}`);
      return;
    }
    next(err);
  }
});
```

## Examples

```javascript
// Bug: long computation with no response sent
app.get('/api/heavy', async (req, res) => {
  const result = await heavyComputation(); // 30 seconds
  res.json(result); // Client may have disconnected
});

// Fixed: stream progress
app.get('/api/heavy', async (req, res) => {
  res.setHeader('Content-Type', 'application/json');
  res.write('{"progress": 0');

  const result = await heavyComputation((pct) => {
    res.write(`,"progress": ${pct}`);
  });

  res.write(`,"data": ${JSON.stringify(result)}}`);
  res.end();
});
```

```text
Error: socket hang up
at TLSSocket.onSocketClose (net.js:426:22)
```
