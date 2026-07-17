---
title: "Node.js Error: connect ETIMEDOUT"
description: "Error: connect ETIMEDOUT — Fix Node.js connection timeout errors when the server does not respond."
languages: ["javascript"]
error-types: ["network-error"]
severities: ["error"]
weight: 5
---

The `ETIMEDOUT` error occurs when a TCP connection attempt takes too long to complete. Unlike ECONNREFUSED, the server never sends a response (the SYN packet goes unanswered), usually due to network issues or a non-routable host.

## Description

Common ETIMEDOUT messages include:

- `Error: connect ETIMEDOUT 104.21.32.15:443` — connection timed out to remote host
- `Error: connect ETIMEDOUT 192.168.1.100:8080` — no response from local network host
- `connect ETIMEDOUT 10.0.0.1:5432` — timeout connecting to database

## Common Causes

```javascript
// Cause 1: Target host is unreachable (firewall or wrong IP)
const net = require("node:net");
net.createConnection({ host: "192.168.1.100", port: 8080 });

// Cause 2: Network outage or DNS resolution to wrong IP
// DNS resolves to an IP that is not reachable from your network

// Cause 3: Default timeout too short for slow connections
fetch("https://slow-api.example.com/data"); // default timeout may be too low

// Cause 4: Server behind load balancer is not responding
// Load balancer forwards but backend server hangs
```

## Solutions

### Fix 1: Increase the socket timeout

```javascript
const net = require("node:net");

const client = net.createConnection({ host: "10.0.0.1", port: 5432 });
client.setTimeout(30000); // 30 seconds

client.on("timeout", () => {
  console.error("Connection timed out");
  client.destroy();
});

client.on("connect", () => {
  console.log("Connected successfully");
});
```

### Fix 2: Use AbortController for fetch timeouts

```javascript
async function fetchWithTimeout(url, timeoutMs = 10000) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), timeoutMs);

  try {
    const response = await fetch(url, { signal: controller.signal });
    return response;
  } catch (err) {
    if (err.name === "AbortError") {
      console.error(`Request to ${url} timed out after ${timeoutMs}ms`);
    }
    throw err;
  } finally {
    clearTimeout(timer);
  }
}
```

### Fix 3: Verify network connectivity

```bash
# Check if the host is reachable
ping -c 4 10.0.0.1

# Check if the port is open
nc -zv 10.0.0.1 5432

# Traceroute to find where packets are dropped
traceroute 10.0.0.1
```

### Fix 4: Configure DNS and retry

```javascript
const dns = require("node:dns");
const net = require("node:net");

function resolveAndConnect(hostname, port) {
  return new Promise((resolve, reject) => {
    dns.lookup(hostname, (err, address) => {
      if (err) return reject(err);
      console.log(`Resolved ${hostname} to ${address}`);
      const socket = net.createConnection({ host: address, port });
      socket.on("connect", () => resolve(socket));
      socket.on("error", reject);
    });
  });
}
```

## Examples

```javascript
// ETIMEDOUT when connecting to a remote database over VPN
const { Client } = require("pg");
const client = new Client({
  host: "10.0.0.50",
  port: 5432,
  connectionTimeoutMillis: 5000,
});
client.connect().catch((err) => {
  if (err.code === "ETIMEDOUT") {
    console.error("Database is unreachable — check VPN connection");
  }
});
```

## Related Errors

- [ECONNREFUSED]({{< relref "/languages/javascript/node-econnrefused" >}}) — connection actively refused.
- [ERR_SOCKET_TIMEOUT]({{< relref "/languages/javascript/ERR_SOCKET_TIMEOUT" >}}) — socket operation timed out.
- [ERR_CONNECTION_RESET]({{< relref "/languages/javascript/err-connection-reset" >}}) — connection reset by peer.
