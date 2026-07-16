---
title: "[Solution] Node.js ERR_HTTP_HEADERS_SENT — Headers Already Sent Fix"
description: "Fix Node.js ERR_HTTP_HEADERS_SENT when attempting to set HTTP headers after they have already been sent. Send all headers before writing the response body."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["err-http-headers-sent", "http", "headers", "response", "express", "nodejs"]
weight: 5
---

# Node.js ERR_HTTP_HEADERS_SENT — Headers Already Sent Fix

The `ERR_HTTP_HEADERS_SENT` error occurs when attempting to set or modify HTTP response headers after they have already been sent to the client. Once `res.writeHead()` or the first `res.write()`/`res.end()` call is made, headers are locked and cannot be changed.

## Description

Common ERR_HTTP_HEADERS_SENT messages include:

- `Error [ERR_HTTP_HEADERS_SENT]: Headers have already been sent` — setting headers after first write.
- `Cannot set headers after they are sent to the client` — Express.js version of the error.
- `ERR_HTTP_HEADERS_SENT: 200` — headers sent with a 200, attempting to change status.

## Common Causes

```javascript
const http = require("http");

// Cause 1: Calling res.writeHead() after res.write()
const server = http.createServer((req, res) => {
  res.write("partial data");  // headers sent here
  res.writeHead(200, { "Content-Type": "text/plain" });  // ERR_HTTP_HEADERS_SENT
  res.end("complete");
});

// Cause 2: Calling res.setHeader() after write
res.write("data");
res.setHeader("X-Custom", "value");  // ERR_HTTP_HEADERS_SENT

// Cause 3: Sending response twice
const server2 = http.createServer((req, res) => {
  res.end("first response");
  res.end("second response");  // ERR_HTTP_HEADERS_SENT
});

// Cause 4: Next() called after sending response in Express
app.get("/api", (req, res) => {
  res.send("done");
  next();  // may trigger ERR_HTTP_HEADERS_SENT downstream
});
```

## Solutions

### Fix 1: Set all headers before writing the body

```javascript
const http = require("http");

const server = http.createServer((req, res) => {
  // Set all headers FIRST
  res.writeHead(200, {
    "Content-Type": "application/json",
    "X-Request-Id": "abc123",
    "Cache-Control": "no-cache",
  });

  // Then write the body
  res.end(JSON.stringify({ status: "ok" }));
});
```

### Fix 2: Check if headers have been sent before modifications

```javascript
function safeSetHeader(res, name, value) {
  if (res.headersSent) {
    console.warn(`Cannot set header '${name}' — headers already sent`);
    return false;
  }
  res.setHeader(name, value);
  return true;
}

function safeRedirect(res, url, statusCode = 302) {
  if (res.headersSent) {
    console.warn("Cannot redirect — headers already sent");
    return false;
  }
  res.writeHead(statusCode, { Location: url });
  res.end();
  return true;
}
```

### Fix 3: Prevent double response in Express.js

```javascript
const express = require("express");
const app = express();

// Wrong — can send response twice
app.get("/api", (req, res) => {
  if (req.query.error) {
    return res.status(500).json({ error: "failed" });
  }
  res.json({ data: "success" });  // runs even after the error response
});

// Correct — use return to prevent fallthrough
app.get("/api", (req, res) => {
  if (req.query.error) {
    return res.status(500).json({ error: "failed" });
  }
  return res.json({ data: "success" });
});
```

### Fix 4: Handle async errors without sending headers twice

```javascript
const express = require("express");
const app = express();

// Wrong — async error may trigger double response
app.get("/api", async (req, res) => {
  const data = await fetchData();
  res.json(data);
  // If an error is thrown, Express sends 500
  // but headers may already be partially sent
});

// Correct — use async error handler
function asyncHandler(fn) {
  return (req, res, next) => {
    Promise.resolve(fn(req, res, next)).catch(next);
  };
}

app.get("/api", asyncHandler(async (req, res) => {
  const data = await fetchData();
  return res.json(data);
}));

// Global error handler — check headersSent
app.use((err, req, res, next) => {
  console.error(err);
  if (res.headersSent) {
    return next(err);  // delegate to default Express error handler
  }
  res.status(500).json({ error: "Internal server error" });
});
```

### Fix 5: Use res.flushHeaders() for streaming responses

```javascript
const http = require("http");

const server = http.createServer((req, res) => {
  // Flush headers immediately for streaming
  res.writeHead(200, {
    "Content-Type": "text/event-stream",
    "Cache-Control": "no-cache",
    Connection: "keep-alive",
  });
  res.flushHeaders();

  // Now send data events
  const interval = setInterval(() => {
    res.write(`data: ${JSON.stringify({ time: Date.now() })}\n\n`);
  }, 1000);

  req.on("close", () => clearInterval(interval));
});
```

## Examples

```javascript
// ERR_HTTP_HEADERS_SENT in middleware chain
const http = require("http");
const express = require("express");
const app = express();

// Middleware that sends early response
app.use((req, res, next) => {
  if (req.headers.authorization === "invalid") {
    return res.status(401).json({ error: "Unauthorized" });
  }
  next();
});

// Route handler — headers already sent if auth failed
app.get("/api", (req, res) => {
  res.json({ data: "success" });  // this runs regardless
});

app.listen(3000);
```

## Related Errors

- [ERR_HTTP_PARSER_COMPLETE]({{< relref "/languages/javascript/err_http_parser_complete" >}}) — HTTP parser finished prematurely.
- [ERR_HTTP_INVALID_CHUNK]({{< relref "/languages/javascript/err_http_invalid_chunk" >}}) — invalid chunked encoding.
- [ERR_HTTP_INVALID_STATUS_CODE]({{< relref "/languages/javascript/err_http_invalid_status_code" >}}) — invalid status code.
- [ERR_STREAM_DESTROYED]({{< relref "/languages/javascript/err_stream_destroyed" >}}) — stream already destroyed.
