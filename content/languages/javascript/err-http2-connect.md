---
title: "[Solution] Node.js ERR_HTTP2_CONNECT — HTTP/2 Connect Error Fix"
description: "Fix Node.js ERR_HTTP2_CONNECT when an HTTP/2 CONNECT request fails. Handle CONNECT method errors and tunnel establishment issues."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Node.js ERR_HTTP2_CONNECT — HTTP/2 Connect Error Fix

The `ERR_HTTP2_CONNECT` error occurs when an HTTP/2 CONNECT request fails. The CONNECT method is used to establish a tunnel through a proxy, and errors can occur when the tunnel setup fails or the server rejects the CONNECT request.

## Description

Common ERR_HTTP2_CONNECT messages include:

- `ERR_HTTP2_CONNECT: CONNECT error` — CONNECT request failed.
- `CONNECT request rejected` — server rejected the tunnel.
- `CONNECT tunnel failed` — tunnel establishment failed.

## Common Causes

```javascript
const http2 = require("node:http2");

// Cause 1: Server doesn't support CONNECT
const client = http2.connect("https://proxy.example.com");
const req = client.request({
  ":method": "CONNECT",
  ":authority": "target.example.com:443",
});
// Server may reject with 403 or 501

// Cause 2: Invalid CONNECT authority
const req2 = client.request({
  ":method": "CONNECT",
  ":authority": "", // empty authority
});

// Cause 3: CONNECT on non-proxy server
// Regular servers don't accept CONNECT requests

// Cause 4: Tunnel timeout
// CONNECT request times out waiting for response
```

## Solutions

### Fix 1: Validate CONNECT target

```javascript
const http2 = require("node:http2");

function isValidConnectTarget(authority) {
  if (!authority || typeof authority !== "string") return false;
  const [host, port] = authority.split(":");
  if (!host) return false;
  if (port && (isNaN(port) || port < 1 || port > 65535)) return false;
  return true;
}

const client = http2.connect("https://proxy.example.com");

const target = "target.example.com:443";
if (!isValidConnectTarget(target)) {
  throw new Error("Invalid CONNECT target");
}

const req = client.request({
  ":method": "CONNECT",
  ":authority": target,
});
```

### Fix 2: Handle CONNECT errors gracefully

```javascript
const http2 = require("node:http2");

const client = http2.connect("https://proxy.example.com");

const req = client.request({
  ":method": "CONNECT",
  ":authority": "target.example.com:443",
});

req.on("response", (headers) => {
  const status = parseInt(headers[":status"], 10);
  if (status !== 200) {
    console.error("CONNECT rejected with status:", status);
    return;
  }
  console.log("Tunnel established");
});

req.on("error", (err) => {
  if (err.code === "ERR_HTTP2_CONNECT") {
    console.error("CONNECT failed:", err.message);
  }
});

req.end();
```

### Fix 3: Set timeout for CONNECT

```javascript
const http2 = require("node:http2");

const client = http2.connect("https://proxy.example.com");

const req = client.request({
  ":method": "CONNECT",
  ":authority": "target.example.com:443",
});

const timeout = setTimeout(() => {
  req.close(0x8); // CANCEL
  console.error("CONNECT timed out");
}, 10000);

req.on("response", (headers) => {
  clearTimeout(timeout);
  if (headers[":status"] === "200") {
    console.log("Tunnel established");
  }
});

req.on("error", (err) => {
  clearTimeout(timeout);
  console.error("CONNECT error:", err.message);
});

req.end();
```

### Fix 4: Use proper proxy configuration

```javascript
const http2 = require("node:http2");
const url = require("node:url");

function connectThroughProxy(proxyUrl, targetHost, targetPort) {
  const proxy = url.parse(proxyUrl);
  const client = http2.connect(proxy.href);

  const req = client.request({
    ":method": "CONNECT",
    ":authority": `${targetHost}:${targetPort}`,
  });

  return new Promise((resolve, reject) => {
    const timeout = setTimeout(() => {
      reject(new Error("CONNECT timeout"));
    }, 10000);

    req.on("response", (headers) => {
      clearTimeout(timeout);
      if (headers[":status"] === "200") {
        resolve(client);
      } else {
        reject(new Error(`CONNECT rejected: ${headers[":status"]}`));
      }
    });

    req.on("error", (err) => {
      clearTimeout(timeout);
      reject(err);
    });

    req.end();
  });
}
```

## Examples

```javascript
const http2 = require("node:http2");

// ERR_HTTP2_CONNECT when proxy rejects request
const client = http2.connect("https://proxy.example.com");

const req = client.request({
  ":method": "CONNECT",
  ":authority": "blocked.example.com:443",
});

req.on("response", (headers) => {
  console.log("Status:", headers[":status"]); // 403
});

req.on("error", (err) => {
  if (err.code === "ERR_HTTP2_CONNECT") {
    console.error("CONNECT request failed");
  }
});

req.end();
```

## Related Errors

- [ERR_HTTP2_SESSION]({{< relref "/languages/javascript/err-http2-session" >}}) — HTTP/2 session error.
- [ERR_CONNECTION_REFUSED]({{< relref "/languages/javascript/err-connection-refused" >}}) — server refused connection.
- [ERR_CONNECTION_RESET]({{< relref "/languages/javascript/err-connection-reset" >}}) — connection was reset.
- [ERR_HTTP2_STREAM_ERROR]({{< relref "/languages/javascript/err-http2-stream-error" >}}) — HTTP/2 stream error.
