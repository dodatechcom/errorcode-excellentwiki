---
title: "[Solution] Node.js ECONNREFUSED: connection refused Error Fix"
description: "Fix Node.js ECONNREFUSED: connection refused error. Handle network connections, verify server availability, and configure retries."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Node.js ECONNREFUSED — connection refused

This error occurs when a Node.js application attempts to connect to a remote server that is not accepting connections on the specified port.

## What This Error Means

Common error messages:

- `Error: connect ECONNREFUSED 127.0.0.1:5432`
- `Error: connect ECONNREFUSED ::1:3000`
- `ECONNREFUSED - Connection refused by server`

The `ECONNREFUSED` code means the target machine actively refused the connection — the port is either not open or no service is listening.

## Common Causes

```javascript
// Cause 1: Target server not running
const net = require('net');
const client = net.createConnection({ port: 5432, host: 'localhost' });
// ECONNREFUSED if PostgreSQL not started

// Cause 2: Wrong host or port
fetch('http://localhost:3001/api') // server on 3000, not 3001

// Cause 3: Firewall blocking connection
// iptables or security group blocking the port

// Cause 4: Service binding to different interface
// Server binds to 127.0.0.1, client connects to 0.0.0.0
```

## How to Fix

### Fix 1: Verify server is running

```bash
# Check if port is listening
lsof -i :5432
netstat -tlnp | grep 5432

# Start the service
sudo systemctl start postgresql
```

### Fix 2: Add retry logic with backoff

```javascript
const net = require('net');

function connectWithRetry(host, port, retries = 5, delay = 1000) {
  return new Promise((resolve, reject) => {
    const attempt = (remaining) => {
      const socket = net.createConnection({ port, host });
      socket.on('connect', () => {
        socket.destroy();
        resolve();
      });
      socket.on('error', (err) => {
        if (remaining <= 0) {
          reject(err);
          return;
        }
        setTimeout(() => attempt(remaining - 1), delay);
      });
    };
    attempt(retries);
  });
}
```

### Fix 3: Health check before connecting

```javascript
async function waitForService(url, maxRetries = 30, interval = 1000) {
  for (let i = 0; i < maxRetries; i++) {
    try {
      const res = await fetch(url);
      if (res.ok) return true;
    } catch {
      // not ready yet
    }
    await new Promise((r) => setTimeout(r, interval));
  }
  throw new Error('Service not available');
}
```

### Fix 4: Check firewall and security groups

```bash
# Check iptables
sudo iptables -L -n | grep 5432

# Check if service binds to correct interface
ss -tlnp | grep 5432
# Should show 0.0.0.0:5432, not 127.0.0.1:5432
```

## Examples

```javascript
const http = require('http');

// This triggers ECONNREFUSED
http.get('http://localhost:9999/api', (res) => {
  console.log('Status:', res.statusCode);
}).on('error', (err) => {
  console.error(err.code); // "ECONNREFUSED"
  console.error(err.message); // "connect ECONNREFUSED 127.0.0.1:9999"
});
```

## Related Errors

- [ETIMEDOUT]({{< relref "/languages/javascript/etimedout" >}}) — connection timed out
- [EADDRINUSE]({{< relref "/languages/javascript/eaddrinuse" >}}) — port in use
- [Axios Error]({{< relref "/languages/javascript/axios-error" >}}) — HTTP request failed
