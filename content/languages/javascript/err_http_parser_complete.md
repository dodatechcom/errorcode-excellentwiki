---
title: "[Solution] Node.js ERR_HTTP_PARSER_COMPLETE — HTTP Parser Error Fix"
description: "Fix Node.js ERR_HTTP_PARSER_COMPLETE when the HTTP parser finishes unexpectedly. Handle incomplete responses, connection resets, and malformed HTTP data."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Node.js ERR_HTTP_PARSER_COMPLETE — HTTP Parser Error Fix

The `ERR_HTTP_PARSER_COMPLETE` error occurs when the HTTP parser completes before the full response or request has been received. This typically happens when the remote server closes the connection prematurely, sends malformed HTTP headers, or the connection is reset mid-transfer.

## Description

Common ERR_HTTP_PARSER_COMPLETE messages include:

- `Error [ERR_HTTP_PARSER_COMPLETE]: HTTP parser was not completed` — parser finished before full message.
- `Error: aborted` — connection was aborted during HTTP parsing.
- `Error: socket hang up` — remote end closed connection unexpectedly.

## Common Causes

```javascript
const http = require("http");

// Cause 1: Server closes connection before sending complete response
http.get("http://example.com", (res) => {
  // If server sends headers then closes, parser fails mid-read
}).on("error", (err) => {
  // ERR_HTTP_PARSER_COMPLETE or ECONNRESET
});

// Cause 2: Malformed HTTP response from server
// Server sends: "HTTP/1.1 200 OK\r\nContent-Length: 100\r\n"
// But closes before sending body

// Cause 3: Proxy or load balancer interrupting the connection
// Upstream proxy times out while Node.js is still reading

// Cause 4: Client disconnects before server finishes sending
// AbortController aborts the request mid-response
```

## Solutions

### Fix 1: Add error handling to HTTP requests

```javascript
const http = require("http");

function makeRequest(url) {
  return new Promise((resolve, reject) => {
    const req = http.get(url, (res) => {
      let data = "";

      res.on("data", (chunk) => {
        data += chunk;
      });

      res.on("end", () => {
        resolve({ status: res.statusCode, data });
      });
    });

    req.on("error", (err) => {
      if (err.code === "ERR_HTTP_PARSER_COMPLETE" || err.code === "ECONNRESET") {
        console.error("HTTP parser error — server may have closed connection");
        reject(err);
      } else {
        reject(err);
      }
    });

    req.setTimeout(10000, () => {
      req.destroy(new Error("Request timeout"));
    });
  });
}
```

### Fix 2: Implement retry logic for transient parser errors

```javascript
const http = require("http");

async function fetchWithRetry(url, maxRetries = 3) {
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      return await makeRequest(url);
    } catch (err) {
      const isRetryable =
        err.code === "ERR_HTTP_PARSER_COMPLETE" ||
        err.code === "ECONNRESET" ||
        err.code === "EPIPE";

      if (isRetryable && attempt < maxRetries) {
        console.log(`Attempt ${attempt} failed, retrying...`);
        await new Promise((r) => setTimeout(r, 1000 * attempt));
        continue;
      }
      throw err;
    }
  }
}
```

### Fix 3: Validate response headers before processing body

```javascript
const http = require("http");

function safeRequest(url) {
  return new Promise((resolve, reject) => {
    const req = http.get(url, (res) => {
      // Validate we got a proper response
      if (!res.headers["content-length"] && !res.headers["transfer-encoding"]) {
        console.warn("No content-length or transfer-encoding header");
      }

      const chunks = [];
      res.on("data", (chunk) => chunks.push(chunk));
      res.on("end", () => {
        resolve(Buffer.concat(chunks));
      });
    });

    req.on("error", reject);
  });
}
```

### Fix 4: Handle keep-alive connection reuse

```javascript
const http = require("http");

// Reuse connections to reduce parser errors
const agent = new http.Agent({
  keepAlive: true,
  maxSockets: 5,
  maxFreeSockets: 2,
  timeout: 60000,
});

http.get("http://example.com/api", { agent }, (res) => {
  // Connection is kept alive for reuse
  // Parser errors are less likely with persistent connections
}).on("error", (err) => {
  console.error("Request failed:", err.message);
});
```

## Examples

```javascript
// ERR_HTTP_PARSER_COMPLETE when proxying requests
const http = require("http");

const proxy = http.createServer((req, res) => {
  const proxyReq = http.request(
    {
      hostname: "backend",
      port: 3000,
      path: req.url,
      method: req.method,
      headers: req.headers,
    },
    (proxyRes) => {
      res.writeHead(proxyRes.statusCode, proxyRes.headers);
      proxyRes.pipe(res);
    }
  );

  proxyReq.on("error", (err) => {
    if (err.code === "ERR_HTTP_PARSER_COMPLETE") {
      console.error("Backend closed connection prematurely");
      res.statusCode = 502;
      res.end("Bad Gateway");
    } else {
      throw err;
    }
  });

  req.pipe(proxyReq);
});

proxy.listen(8080);
```

## Related Errors

- [ERR_HTTP_HEADERS_SENT]({{< relref "/languages/javascript/err_http_headers_sent" >}}) — headers already sent.
- [ERR_HTTP_INVALID_CHUNK]({{< relref "/languages/javascript/err_http_invalid_chunk" >}}) — invalid chunked encoding.
- [ERR_HTTP_INVALID_STATUS_CODE]({{< relref "/languages/javascript/err_http_invalid_status_code" >}}) — invalid status code.
- [ERR_SOCKET_DESTROYED]({{< relref "/languages/javascript/err_socket_destroyed" >}}) — socket already destroyed.
