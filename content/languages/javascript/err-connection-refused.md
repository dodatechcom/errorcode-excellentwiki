---
title: "[Solution] Node.js ERR_CONNECTION_REFUSED — Connection Refused Fix"
description: "Fix Node.js ERR_CONNECTION_REFUSED when a TCP connection to a server is rejected. Ensure the target server is running and accepting connections."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Node.js ERR_CONNECTION_REFUSED — Connection Refused Fix

The `ERR_CONNECTION_REFUSED` error occurs when a TCP connection attempt to a remote server is actively rejected. This typically means the target server is not running, not listening on the specified port, or a firewall is blocking the connection.

## Description

Common ERR_CONNECTION_REFUSED messages include:

- `connect ECONNREFUSED 127.0.0.1:3000` — server not listening on localhost:3000.
- `connect ECONNREFUSED ::1:8080` — server not listening on IPv6 port 8080.
- `Connection refused` — generic refusal from the target host.

## Common Causes

```javascript
const net = require("node:net");

// Cause 1: Server is not running
const client = net.createConnection({ port: 3000, host: "localhost" });
// ERR_CONNECTION_REFUSED if no server on port 3000

// Cause 2: Wrong port number
const client2 = net.createConnection({ port: 9999 });
// ERR_CONNECTION_REFUSED if server is on port 3000

// Cause 3: Wrong host address
const client3 = net.createConnection({ host: "192.168.1.999", port: 3000 });

// Cause 4: Firewall blocking the connection
// Connection blocked by OS firewall rules
```

## Solutions

### Fix 1: Verify the target server is running

```bash
# Check if the server is listening on the port
netstat -tlnp | grep 3000
# or
ss -tlnp | grep 3000

# Check if the process is running
ps aux | grep node
```

### Fix 2: Add retry logic for transient failures

```javascript
const net = require("node:net");

function connectWithRetry(port, host, retries = 5, delay = 1000) {
  return new Promise((resolve, reject) => {
    const attempt = (remaining) => {
      const client = net.createConnection({ port, host });

      client.on("connect", () => {
        client.destroy();
        resolve();
      });

      client.on("error", (err) => {
        client.destroy();
        if (remaining <= 0) {
          reject(err);
          return;
        }
        console.log(`Connection failed, retrying in ${delay}ms...`);
        setTimeout(() => attempt(remaining - 1), delay);
      });
    };

    attempt(retries);
  });
}

connectWithRetry(3000, "localhost")
  .then(() => console.log("Connected!"))
  .catch((err) => console.error("Failed to connect:", err.message));
```

### Fix 3: Validate host and port before connecting

```javascript
const net = require("node:net");

function validateConnection(host, port) {
  return new Promise((resolve) => {
    const socket = new net.Socket();
    const timer = setTimeout(() => {
      socket.destroy();
      resolve(false);
    }, 3000);

    socket.connect(port, host, () => {
      clearTimeout(timer);
      socket.destroy();
      resolve(true);
    });

    socket.on("error", () => {
      clearTimeout(timer);
      socket.destroy();
      resolve(false);
    });
  });
}

// Check before making the real connection
const isAvailable = await validateConnection("localhost", 3000);
if (!isAvailable) {
  console.error("Server is not available on port 3000");
}
```

### Fix 4: Handle connection errors gracefully

```javascript
const http = require("node:http");

function makeRequest(url) {
  return new Promise((resolve, reject) => {
    const req = http.get(url, (res) => {
      let data = "";
      res.on("data", (chunk) => (data += chunk));
      res.on("end", () => resolve(data));
    });

    req.on("error", (err) => {
      if (err.code === "ECONNREFUSED") {
        reject(new Error(`Server refused connection: ${err.message}`));
      } else {
        reject(err);
      }
    });

    req.end();
  });
}
```

## Examples

```javascript
const http = require("node:http");

// ERR_CONNECTION_REFUSED when server is not running
const req = http.get("http://localhost:3000/api", (res) => {
  console.log("Status:", res.statusCode);
});

req.on("error", (err) => {
  if (err.code === "ECONNREFUSED") {
    console.error("Server is not running on port 3000");
    console.error("Start the server with: node server.js");
  }
});

req.end();
```

## Related Errors

- [ERR_CONNECTION_RESET]({{< relref "/languages/javascript/err-connection-reset" >}}) — connection was reset by peer.
- [ERR_SOCKET_TIMEOUT]({{< relref "/languages/javascript/ERR_SOCKET_TIMEOUT" >}}) — socket timed out.
- [ERR_DNS_RESOLUTION_FAILED]({{< relref "/languages/javascript/err-dns-resolution-failed" >}}) — DNS lookup failed.
- [ERR_HTTP1_CONNECTION_CLOSED]({{< relref "/languages/javascript/err-http1-connection-closed" >}}) — HTTP/1.1 connection closed.
