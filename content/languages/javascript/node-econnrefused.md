---
title: "Node.js Error: connect ECONNREFUSED"
description: "Error: connect ECONNREFUSED — Fix Node.js TCP connection refused errors when the target server is not listening."
languages: ["javascript"]
error-types: ["network-error"]
severities: ["error"]
tags: ["nodejs", "econnrefused", "tcp", "connection", "network", "net"]
weight: 5
---

The `ECONNREFUSED` error occurs when Node.js attempts to establish a TCP connection to a remote host, but the target machine actively refuses the connection. This typically means no service is listening on the specified port.

## Description

Common ECONNREFUSED messages include:

- `Error: connect ECONNREFUSED 127.0.0.1:5432` — nothing listening on port 5432
- `Error: connect ECONNREFUSED ::1:6379` — nothing listening on port 6379 on IPv6
- `connect ECONNREFUSED 10.0.0.5:3306` — remote host refused the connection

## Common Causes

```javascript
// Cause 1: Target service is not running
const net = require("node:net");
const client = net.createConnection({ host: "127.0.0.1", port: 5432 }, () => {
  console.log("Connected");
});
client.on("error", (err) => {
  // Error: connect ECONNREFUSED 127.0.0.1:5432
});

// Cause 2: Wrong host or port
const redis = require("redis");
redis.createClient({ host: "127.0.0.1", port: 6380 }); // wrong port

// Cause 3: Firewall blocking the connection
// The OS firewall or security group drops the SYN packet

// Cause 4: Service binding to localhost instead of 0.0.0.0
// Service on remote machine only listens on 127.0.0.1
```

## Solutions

### Fix 1: Verify the service is running

```bash
# Check if the service is listening on the expected port
ss -tlnp | grep 5432

# Check if the process is running
systemctl status postgresql

# Start the service if it is stopped
sudo systemctl start postgresql
```

### Fix 2: Verify host and port configuration

```javascript
const net = require("node:net");

function checkPort(host, port, timeout = 2000) {
  return new Promise((resolve) => {
    const socket = new net.Socket();
    socket.setTimeout(timeout);
    socket.on("connect", () => {
      socket.destroy();
      resolve(true);
    });
    socket.on("timeout", () => {
      socket.destroy();
      resolve(false);
    });
    socket.on("error", () => {
      resolve(false);
    });
    socket.connect(port, host);
  });
}

// Usage
const reachable = await checkPort("127.0.0.1", 5432);
if (!reachable) {
  console.error("PostgreSQL is not running on port 5432");
}
```

### Fix 3: Implement connection retry logic

```javascript
const net = require("node:net");

function connectWithRetry(host, port, retries = 5, delay = 2000) {
  return new Promise((resolve, reject) => {
    const attempt = (remaining) => {
      const client = net.createConnection({ host, port });
      client.on("connect", () => {
        client.end();
        resolve();
      });
      client.on("error", (err) => {
        client.destroy();
        if (remaining <= 0) return reject(err);
        console.log(`Retrying in ${delay}ms... (${remaining} left)`);
        setTimeout(() => attempt(remaining - 1), delay);
      });
    };
    attempt(retries);
  });
}
```

## Examples

```javascript
// ECONNREFUSED when PostgreSQL is not running locally
const { Client } = require("pg");
const client = new Client({
  host: "localhost",
  port: 5432,
  database: "myapp",
});
client.connect().catch((err) => {
  console.error("Cannot connect to PostgreSQL:", err.message);
});
// Error: connect ECONNREFUSED 127.0.0.1:5432
// Fix: sudo systemctl start postgresql
```

## Related Errors

- [ERR_CONNECTION_REFUSED]({{< relref "/languages/javascript/err-connection-refused" >}}) — older Node.js connection error.
- [ERR_CONNECTION_RESET]({{< relref "/languages/javascript/err-connection-reset" >}}) — connection reset by peer.
- [ERR_SOCKET_TIMEOUT]({{< relref "/languages/javascript/ERR_SOCKET_TIMEOUT" >}}) — socket operation timed out.
