---
title: "[Solution] Node.js ERR_HTTP_INVALID_CHUNK — Invalid HTTP Chunk Fix"
description: "Fix Node.js ERR_HTTP_INVALID_CHUNK when sending malformed chunked transfer encoding. Ensure chunks are Buffers or strings and proper chunk encoding."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["err-http-invalid-chunk", "http", "chunked", "transfer-encoding", "streaming", "nodejs"]
weight: 5
---

# Node.js ERR_HTTP_INVALID_CHUNK — Invalid HTTP Chunk Fix

The `ERR_HTTP_INVALID_CHUNK` error occurs when Node.js encounters an invalid chunk in the HTTP chunked transfer encoding. This happens when a chunk sent via `res.write()` is not a valid type (must be a `Buffer` or `string`), or when chunked encoding is corrupted during transmission.

## Description

Common ERR_HTTP_INVALID_CHUNK messages include:

- `Error [ERR_HTTP_INVALID_CHUNK]: Invalid HTTP chunk` — chunk data is not a Buffer or string.
- `ERR_HTTP_INVALID_CHUNK: must be Buffer or string` — wrong type passed to `res.write()`.

## Common Causes

```javascript
const http = require("http");

// Cause 1: Passing a non-Buffer, non-string to res.write()
const server = http.createServer((req, res) => {
  res.write(123);           // ERR_HTTP_INVALID_CHUNK — number
  res.write(null);          // ERR_HTTP_INVALID_CHUNK — null
  res.write(undefined);     // ERR_HTTP_INVALID_CHUNK — undefined
  res.write({ key: "val" }); // ERR_HTTP_INVALID_CHUNK — object
});

// Cause 2: Encoding mismatch — passing a string with a buffer encoding
const server2 = http.createServer((req, res) => {
  res.write(Buffer.from("data"), "hex");  // may corrupt the data
});

// Cause 3: Corrupted data during streaming
// Transform stream returns wrong type

// Cause 4: Passing a typed array instead of Buffer
const server3 = http.createServer((req, res) => {
  res.write(new Uint8Array([1, 2, 3]));  // ERR_HTTP_INVALID_CHUNK
});
```

## Solutions

### Fix 1: Ensure chunks are Buffer or string

```javascript
const http = require("http");

function safeWrite(res, chunk, encoding) {
  if (chunk === null || chunk === undefined) {
    console.warn("Cannot write null/undefined chunk");
    return false;
  }

  // Convert to Buffer or string
  let data;
  if (Buffer.isBuffer(chunk)) {
    data = chunk;
  } else if (typeof chunk === "string") {
    data = chunk;
  } else if (chunk instanceof ArrayBuffer) {
    data = Buffer.from(chunk);
  } else if (ArrayBuffer.isView(chunk)) {
    data = Buffer.from(chunk.buffer, chunk.byteOffset, chunk.byteLength);
  } else if (typeof chunk === "object") {
    data = JSON.stringify(chunk);
  } else {
    data = String(chunk);
  }

  return res.write(data, encoding);
}
```

### Fix 2: Validate data before streaming

```javascript
const http = require("http");

const server = http.createServer((req, res) => {
  res.writeHead(200, {
    "Content-Type": "application/json",
    "Transfer-Encoding": "chunked",
  });

  const data = [1, 2, 3];

  for (const item of data) {
    // Convert each item to a valid chunk
    const chunk = Buffer.from(JSON.stringify(item) + "\n");
    if (!res.write(chunk)) {
      // Backpressure — wait for drain
      res.once("drain", () => res.write(chunk));
    }
  }

  res.end();
});
```

### Fix 3: Use Transform streams correctly

```javascript
const { Transform } = require("stream");
const http = require("http");

const jsonTransform = new Transform({
  objectMode: true,
  transform(chunk, encoding, callback) {
    // Must return a string or Buffer, not an object
    try {
      const json = JSON.stringify(chunk) + "\n";
      callback(null, json);
    } catch (err) {
      callback(err);
    }
  },
});

const server = http.createServer((req, res) => {
  res.writeHead(200, { "Content-Type": "application/json" });

  const source = new (require("stream").Readable)({
    read() {
      this.push({ id: 1, name: "Alice" });
      this.push({ id: 2, name: "Bob" });
      this.push(null);
    },
  });

  source.pipe(jsonTransform).pipe(res);
});
```

### Fix 4: Handle backpressure in streaming responses

```javascript
const http = require("http");

const server = http.createServer(async (req, res) => {
  res.writeHead(200, {
    "Content-Type": "text/plain",
    "Transfer-Encoding": "chunked",
  });

  const chunks = ["Hello", " ", "World"];

  for (const chunk of chunks) {
    const ok = res.write(chunk);
    if (!ok) {
      // Wait for drain before continuing
      await new Promise((resolve) => res.once("drain", resolve));
    }
  }

  res.end();
});
```

## Examples

```javascript
// ERR_HTTP_INVALID_CHUNK when forwarding streams
const http = require("http");

const server = http.createServer(async (req, res) => {
  try {
    const upstream = await fetch("https://api.example.com/stream");

    // Wrong — upstream.body is a ReadableStream, not a Node.js stream
    // res.write(upstream.body);  // ERR_HTTP_INVALID_CHUNK

    // Correct — convert Web ReadableStream to Node.js stream
    const { Readable } = require("stream");
    const nodeStream = Readable.fromWeb(upstream.body);
    nodeStream.pipe(res);
  } catch (err) {
    res.statusCode = 502;
    res.end("Bad Gateway");
  }
});
```

## Related Errors

- [ERR_HTTP_HEADERS_SENT]({{< relref "/languages/javascript/err_http_headers_sent" >}}) — headers already sent.
- [ERR_HTTP_PARSER_COMPLETE]({{< relref "/languages/javascript/err_http_parser_complete" >}}) — HTTP parser finished prematurely.
- [ERR_HTTP_INVALID_STATUS_CODE]({{< relref "/languages/javascript/err_http_invalid_status_code" >}}) — invalid status code.
- [ERR_STREAM_DESTROYED]({{< relref "/languages/javascript/err_stream_destroyed" >}}) — stream already destroyed.
