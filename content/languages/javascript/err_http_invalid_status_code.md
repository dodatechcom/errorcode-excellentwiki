---
title: "[Solution] Node.js ERR_HTTP_INVALID_STATUS_CODE — Invalid Status Code Fix"
description: "Fix Node.js ERR_HTTP_INVALID_STATUS_CODE when setting an invalid HTTP status code. Ensure status codes are integers between 100 and 599."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["err-http-invalid-status-code", "http", "status-code", "response", "express", "nodejs"]
weight: 5
---

# Node.js ERR_HTTP_INVALID_STATUS_CODE — Invalid Status Code Fix

The `ERR_HTTP_INVALID_STATUS_CODE` error occurs when setting an HTTP response status code to an invalid value. Status codes must be integers between 100 and 599. Non-integer values, negative numbers, or values outside the valid range trigger this error.

## Description

Common ERR_HTTP_INVALID_STATUS_CODE messages include:

- `Error [ERR_HTTP_INVALID_STATUS_CODE]: Invalid status code: X` — status code outside 100-599.
- `RangeError: Invalid status code: 0` — zero is not a valid HTTP status code.
- `ERR_HTTP_INVALID_STATUS_CODE: 999` — status code above 599.

## Common Causes

```javascript
const http = require("http");

// Cause 1: Using a float instead of integer
const server = http.createServer((req, res) => {
  res.writeHead(200.5);  // ERR_HTTP_INVALID_STATUS_CODE
});

// Cause 2: Using a string instead of number
const server2 = http.createServer((req, res) => {
  res.statusCode = "200";  // may cause issues in some contexts
  res.end("ok");
});

// Cause 3: Status code outside valid range
res.writeHead(0);      // ERR_HTTP_INVALID_STATUS_CODE
res.writeHead(600);    // ERR_HTTP_INVALID_STATUS_CODE
res.writeHead(-1);     // ERR_HTTP_INVALID_STATUS_CODE

// Cause 4: Using undefined or null
res.statusCode = undefined;  // ERR_HTTP_INVALID_STATUS_CODE
```

## Solutions

### Fix 1: Validate status codes before setting them

```javascript
function validStatusCode(code) {
  return Number.isInteger(code) && code >= 100 && code <= 599;
}

function safeWriteHead(res, statusCode, headers) {
  if (!validStatusCode(statusCode)) {
    console.error("Invalid status code:", statusCode);
    res.writeHead(500);
    res.end("Internal Server Error");
    return false;
  }
  res.writeHead(statusCode, headers);
  return true;
}
```

### Fix 2: Use a status code mapping

```javascript
const STATUS_CODES = {
  OK: 200,
  CREATED: 201,
  NO_CONTENT: 204,
  BAD_REQUEST: 400,
  UNAUTHORIZED: 401,
  FORBIDDEN: 403,
  NOT_FOUND: 404,
  INTERNAL_ERROR: 500,
  SERVICE_UNAVAILABLE: 503,
};

function setStatusCode(res, code) {
  const statusCode = typeof code === "string" ? STATUS_CODES[code] : code;

  if (!Number.isInteger(statusCode) || statusCode < 100 || statusCode > 599) {
    console.error("Invalid status code:", code);
    res.statusCode = 500;
    return false;
  }

  res.statusCode = statusCode;
  return true;
}

// Usage
const express = require("express");
const app = express();

app.get("/api", (req, res) => {
  setStatusCode(res, "NOT_FOUND");
  res.end("Not Found");
});
```

### Fix 3: Handle undefined response codes from upstream

```javascript
const http = require("http");

function fetchWithStatusCheck(url) {
  return new Promise((resolve, reject) => {
    http.get(url, (res) => {
      const status = parseInt(res.statusCode, 10);

      if (!Number.isInteger(status) || status < 100 || status > 599) {
        console.warn("Unexpected status code from upstream:", res.statusCode);
        resolve({ status: 502, data: null });
        return;
      }

      let data = "";
      res.on("data", (chunk) => (data += chunk));
      res.on("end", () => resolve({ status, data }));
    }).on("error", reject);
  });
}
```

### Fix 4: Use res.sendStatus() in Express for validation

```javascript
const express = require("express");
const app = express();

// Express sendStatus validates the code
app.get("/api", (req, res) => {
  res.sendStatus(200);
});

// Custom middleware to validate status codes
app.use((req, res, next) => {
  const originalWriteHead = res.writeHead.bind(res);

  res.writeHead = (statusCode, ...args) => {
    if (!Number.isInteger(statusCode) || statusCode < 100 || statusCode > 599) {
      console.error("Invalid status code intercepted:", statusCode);
      return originalWriteHead(500, ...args);
    }
    return originalWriteHead(statusCode, ...args);
  };

  next();
});
```

## Examples

```javascript
// ERR_HTTP_INVALID_STATUS_CODE in API gateway
const http = require("http");

function createGateway(routes) {
  return http.createServer(async (req, res) => {
    const handler = routes[req.url];

    if (!handler) {
      res.writeHead(404);
      res.end("Not Found");
      return;
    }

    try {
      const result = await handler(req, res);
      const statusCode = result.statusCode || 200;

      if (!Number.isInteger(statusCode) || statusCode < 100 || statusCode > 599) {
        console.error("Handler returned invalid status:", statusCode);
        res.writeHead(500);
        res.end("Internal Server Error");
        return;
      }

      res.writeHead(statusCode);
      res.end(JSON.stringify(result.body));
    } catch (err) {
      console.error("Gateway error:", err);
      res.writeHead(500);
      res.end("Internal Server Error");
    }
  });
}
```

## Related Errors

- [ERR_HTTP_HEADERS_SENT]({{< relref "/languages/javascript/err_http_headers_sent" >}}) — headers already sent.
- [ERR_HTTP_INVALID_CHUNK]({{< relref "/languages/javascript/err_http_invalid_chunk" >}}) — invalid chunked encoding.
- [ERR_HTTP_PARSER_COMPLETE]({{< relref "/languages/javascript/err_http_parser_complete" >}}) — HTTP parser finished prematurely.
- [SyntaxError]({{< relref "/languages/javascript/syntaxerror" >}}) — code has invalid syntax.
