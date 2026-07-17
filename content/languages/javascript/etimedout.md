---
title: "[Solution] Node.js ETIMEDOUT: connection timed out Error Fix"
description: "Fix Node.js ETIMEDOUT: connection timed out error. Handle network timeouts, configure request timeouts, and implement retry strategies."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["etimedout", "timeout", "connection", "network", "socket"]
weight: 5
---

# Node.js ETIMEDOUT — connection timed out

This error occurs when a TCP connection or HTTP request takes longer than the configured timeout to complete. The system gives up waiting for a response.

## What This Error Means

Common error messages:

- `Error: connect ETIMEDOUT 93.184.216.34:443`
- `Error: ETIMEDOUT: operation timed out`
- `FetchError: network timeout at http://example.com`

The `ETIMEDOUT` code means "Error TIME OUT" — the connection attempt or data transfer exceeded the allowed time.

## Common Causes

```javascript
// Cause 1: Server too slow to respond
fetch('http://slow-server.com/api') // no timeout set

// Cause 2: Network congestion or high latency
// Mobile networks, long-distance connections

// Cause 3: Server behind load balancer that's overloaded
// Requests queued and timing out

// Cause 4: DNS resolution taking too long
// DNS server unreachable or slow
```

## How to Fix

### Fix 1: Set timeouts on HTTP requests

```javascript
const http = require('http');
const https = require('https');

function fetchWithTimeout(url, options = {}) {
  const { timeout = 10000 } = options;
  const client = url.startsWith('https') ? https : http;

  return new Promise((resolve, reject) => {
    const req = client.get(url, { timeout }, (res) => {
      let data = '';
      res.on('data', (chunk) => (data += chunk));
      res.on('end', () => resolve({ status: res.statusCode, data }));
    });

    req.on('timeout', () => {
      req.destroy();
      reject(new Error(`Request timed out after ${timeout}ms`));
    });

    req.on('error', reject);
  });
}
```

### Fix 2: Configure timeouts in axios

```javascript
const axios = require('axios');

const client = axios.create({
  timeout: 15000, // 15 seconds
  connectTimeout: 5000, // connection timeout
});

client.get('/api/data')
  .then(res => console.log(res.data))
  .catch(err => {
    if (err.code === 'ECONNABORTED') {
      console.error('Request timed out');
    }
  });
```

### Fix 3: Use AbortController for fetch

```javascript
async function fetchWithTimeout(url, ms = 10000) {
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), ms);

  try {
    const res = await fetch(url, { signal: controller.signal });
    clearTimeout(timeoutId);
    return res;
  } catch (err) {
    clearTimeout(timeoutId);
    if (err.name === 'AbortError') {
      throw new Error(`Timeout: ${url} took more than ${ms}ms`);
    }
    throw err;
  }
}
```

### Fix 4: Implement exponential backoff retry

```javascript
async function fetchWithRetry(url, maxRetries = 3) {
  for (let i = 0; i < maxRetries; i++) {
    try {
      const res = await fetch(url);
      return res;
    } catch (err) {
      if (i === maxRetries - 1) throw err;
      const delay = Math.pow(2, i) * 1000;
      await new Promise(r => setTimeout(r, delay));
    }
  }
}
```

## Examples

```javascript
const net = require('net');

// This triggers ETIMEDOUT
const socket = net.createConnection({ port: 9999, host: '10.0.0.1' });
socket.setTimeout(3000);
socket.on('timeout', () => {
  console.error('Connection timed out');
  socket.destroy();
});
```

## Related Errors

- [ECONNREFUSED]({{< relref "/languages/javascript/econnrefused-node" >}}) — connection actively refused
- [AbortError]({{< relref "/languages/javascript/aborterror" >}}) — operation aborted
- [Axios Error]({{< relref "/languages/javascript/axios-error" >}}) — HTTP request failed
