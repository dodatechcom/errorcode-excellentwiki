---
title: "[Solution] Node.js ERR_HTTP1_INSUFFICIENT — HTTP/1.1 Insufficient Data Fix"
description: "Fix Node.js ERR_HTTP1_INSUFFICIENT when there is insufficient data to parse an HTTP/1.1 message. Handle incomplete HTTP messages gracefully."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["err-http1-insufficient", "http", "parser", "data", "nodejs"]
weight: 5
---

# Node.js ERR_HTTP1_INSUFFICIENT — HTTP/1.1 Insufficient Data Fix

The `ERR_HTTP1_INSUFFICIENT` error occurs when there is not enough data to parse a complete HTTP/1.1 message. This typically happens when a connection is closed before the full request or response is received.

## Description

Common ERR_HTTP1_INSUFFICIENT messages include:

- `ERR_HTTP1_INSUFFICIENT: Insufficient data` — not enough data to parse HTTP message.
- `Incomplete HTTP message` — message body is shorter than Content-Length.
- `Unexpected end of data` — stream ended before message completion.

## Common Causes

```javascript
const http = require("node:http");

// Cause 1: Content-Length mismatch
const server = http.createServer((req, res) => {
  res.writeHead(200, {
    "Content-Length": "100", // claims 100 bytes
    "Content-Type": "text/plain",
  });
  res.end("Hello"); // only sends 5 bytes — ERR_HTTP1_INSUFFICIENT
});

// Cause 2: Premature connection close during POST
const server2 = http.createServer((req, res) => {
  let body = "";
  req.on("data", (chunk) => (body += chunk));
  req.on("end", () => {
    // Client disconnected before all data was received
    res.end("OK");
  });
});

// Cause 3: Chunked encoding terminated early
// Transfer-Encoding: chunked but final chunk not sent

// Cause 4: Connection timeout during large uploads
```

## Solutions

### Fix 1: Match Content-Length exactly

```javascript
const http = require("node:http");
const fs = require("node:fs");

const server = http.createServer((req, res) => {
  const filePath = "/path/to/file.txt";
  const stat = fs.statSync(filePath);

  res.writeHead(200, {
    "Content-Type": "text/plain",
    "Content-Length": stat.size, // exact size
  });

  fs.createReadStream(filePath).pipe(res);
});
```

### Fix 2: Use chunked transfer encoding

```javascript
const http = require("node:http");

const server = http.createServer((req, res) => {
  // Don't set Content-Length — use chunked encoding automatically
  res.writeHead(200, { "Content-Type": "text/plain" });

  // Send data in chunks without worrying about exact size
  res.write("Hello, ");
  res.write("World!");
  res.end();
});
```

### Fix 3: Validate Content-Length against body

```javascript
const http = require("node:http");

function safeEnd(res, data) {
  const body = typeof data === "string" ? Buffer.from(data) : data;
  res.writeHead(200, {
    "Content-Type": "text/plain",
    "Content-Length": body.length, // exact match
  });
  res.end(body);
}

const server = http.createServer((req, res) => {
  safeEnd(res, "Hello, World!");
});
```

### Fix 4: Handle incomplete requests on server

```javascript
const http = require("node:http");

const server = http.createServer((req, res) => {
  const contentLength = parseInt(req.headers["content-length"], 10);
  let received = 0;
  const chunks = [];

  req.on("data", (chunk) => {
    received += chunk.length;
    chunks.push(chunk);

    if (contentLength && received > contentLength) {
      req.destroy();
      res.writeHead(413);
      res.end("Request too large");
    }
  });

  req.on("end", () => {
    if (contentLength && received < contentLength) {
      res.writeHead(400);
      res.end("Incomplete request body");
      return;
    }
    const body = Buffer.concat(chunks).toString();
    res.writeHead(200, { "Content-Type": "text/plain" });
    res.end("Received " + received + " bytes");
  });

  req.on("error", (err) => {
    if (err.code === "ERR_HTTP1_INSUFFICIENT") {
      console.error("Incomplete HTTP message");
    }
    res.writeHead(500);
    res.end("Internal error");
  });
});
```

## Examples

```javascript
const http = require("node:http");

// ERR_HTTP1_INSUFFICIENT with Content-Length mismatch
const server = http.createServer((req, res) => {
  res.writeHead(200, {
    "Content-Length": 1000, // wrong: claims 1000 bytes
    "Content-Type": "text/plain",
  });
  res.end("Short response"); // actual: 15 bytes
});

const client = http.get("http://localhost:3000", (res) => {
  let data = "";
  res.on("data", (chunk) => (data += chunk));
  res.on("end", () => {
    console.log("Received:", data.length, "bytes");
  });
});

client.on("error", (err) => {
  if (err.code === "ERR_HTTP1_INSUFFICIENT") {
    console.error("Server sent fewer bytes than Content-Length");
  }
});
```

## Related Errors

- [ERR_HTTP1_CONNECTION_CLOSED]({{< relref "/languages/javascript/err-http1-connection-closed" >}}) — connection closed early.
- [ERR_HTTP1_HEADER_PARSING]({{< relref "/languages/javascript/err-http1-header-parsing" >}}) — header parsing failed.
- [ERR_HTTP1_STATUS_CODE]({{< relref "/languages/javascript/err-http1-status-code" >}}) — invalid status code.
- [ERR_HTTP_INVALID_CHUNK]({{< relref "/languages/javascript/err_http_invalid_chunk" >}}) — invalid chunked encoding.
