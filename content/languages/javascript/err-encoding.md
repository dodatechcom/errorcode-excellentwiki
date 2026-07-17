---
title: "[Solution] Node.js ERR_ENCODING — Invalid Encoding Fix"
description: "Fix Node.js ERR_ENCODING when an invalid or unsupported encoding is specified for string or buffer operations. Use valid encoding types."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Node.js ERR_ENCODING — Invalid Encoding Fix

The `ERR_ENCODING` error occurs when an invalid or unsupported encoding name is passed to a Buffer or string operation. Node.js supports a specific set of encodings, and using an unrecognized one triggers this error.

## Description

Common ERR_ENCODING messages include:

- `ERR_ENCODING: "foo" encoding is invalid` — unknown encoding name.
- `Unknown encoding: xyz` — unsupported encoding string.
- `Invalid encoding in Buffer` — invalid encoding for buffer conversion.

## Common Causes

```javascript
const Buffer = require("node:buffer").Buffer;

// Cause 1: Typo in encoding name
Buffer.from("hello", "utf-8x"); // ERR_ENCODING

// Cause 2: Unsupported encoding
Buffer.from("hello", "latin9"); // ERR_ENCODING

// Cause 3: Case sensitivity issue
Buffer.from("hello", "UTF8"); // ERR_ENCODING

// Cause 4: Passing null encoding
"hello".encode(null); // ERR_ENCODING
```

## Solutions

### Fix 1: Use supported encoding names

```javascript
const Buffer = require("node:buffer").Buffer;

// Supported encodings in Node.js:
const buf1 = Buffer.from("hello", "utf8");
const buf2 = Buffer.from("hello", "ascii");
const buf3 = Buffer.from("hello", "latin1");
const buf4 = Buffer.from("68656c6c6f", "hex");
const buf5 = Buffer.from("aGVsbG8=", "base64");
const buf6 = Buffer.from("hello", "utf16le");

// Use Buffer.encodingExists() to check
const { encodingExists } = require("node:buffer");
if (encodingExists("utf8")) {
  console.log("utf8 is supported");
}
```

### Fix 2: Normalize encoding names

```javascript
function normalizeEncoding(encoding) {
  const map = {
    "utf-8": "utf8",
    "utf8": "utf8",
    "utf-16le": "utf16le",
    "utf16le": "utf16le",
    "latin1": "latin1",
    "binary": "latin1",
    "base64": "base64",
    "hex": "hex",
    "ascii": "ascii",
  };
  return map[encoding?.toLowerCase()] || encoding;
}

const buf = Buffer.from("hello", normalizeEncoding("UTF-8"));
```

### Fix 3: Validate encoding before use

```javascript
const { encodingExists } = require("node:buffer");

function safeBufferFrom(data, encoding = "utf8") {
  if (!encodingExists(encoding)) {
    throw new Error(
      `Invalid encoding: "${encoding}". Supported: utf8, ascii, latin1, hex, base64`
    );
  }
  return Buffer.from(data, encoding);
}
```

### Fix 4: Handle encoding in streams

```javascript
const { Transform } = require("node:stream");

const transform = new Transform({
  encoding: "utf8", // valid encoding
  transform(chunk, encoding, callback) {
    callback(null, chunk.toString("utf8"));
  },
});

transform.on("error", (err) => {
  if (err.code === "ERR_ENCODING") {
    console.error("Invalid encoding specified for stream");
  }
});
```

## Examples

```javascript
const Buffer = require("node:buffer").Buffer;

// ERR_ENCODING with invalid encoding
try {
  const buf = Buffer.from("hello", "invalid-encoding");
} catch (err) {
  console.error(err.code); // ERR_ENCODING
  console.error(err.message); // "invalid-encoding" encoding is invalid
}
```

## Related Errors

- [ERR_BUFFER_NOT_INITIALIZED]({{< relref "/languages/javascript/err-buffer-not-initialized" >}}) — buffer not initialized.
- [EncodingError]({{< relref "/languages/javascript/encodingerr" >}}) — encoding conversion failed.
- [ERR_INVALID_URI]({{< relref "/languages/javascript/err_invalid_uri" >}}) — invalid URI for conversion.
- [ERR_FILE_TOO_LARGE]({{< relref "/languages/javascript/err_file_too_large" >}}) — file exceeds size limits.
