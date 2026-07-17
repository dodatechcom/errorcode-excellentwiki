---
title: "[Solution] JavaScript EncodingError — Encoding/Decoding Error Fix"
description: "Fix JavaScript EncodingError when encoding or decoding text. Handle malformed sequences, invalid byte inputs, and unsupported encodings."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# EncodingError — Encoding/Decoding Error Fix

An `EncodingError` is thrown when a text encoding or decoding operation encounters invalid data. This commonly occurs with `TextDecoder` when the input contains byte sequences that are not valid for the specified encoding, or with URL encoding functions when given malformed input.

## Description

Common EncodingError messages include:

- `EncodingError: The encoded data was not valid` — `TextDecoder` received invalid byte sequences.
- `URIError: URI malformed` — `decodeURI` or `decodeURIComponent` received invalid percent-encoded input.
- `EncodingError: The source string is not properly encoded` — invalid input to `btoa` or URL encoding.

## Common Causes

```javascript
// Cause 1: Invalid UTF-8 byte sequence
const invalidBytes = new Uint8Array([0xE0, 0xA4, 0xFF]); // invalid UTF-8
const decoder = new TextDecoder("utf-8", { fatal: true });
decoder.decode(invalidBytes);  // EncodingError

// Cause 2: Malformed URI percent-encoding
decodeURIComponent("%E0%A4%A");  // URIError: URI malformed

// Cause 3: Mismatched encoding between writer and reader
const encoder = new TextEncoder();           // always UTF-8
const latin1Decoder = new TextDecoder("iso-8859-1");
const data = encoder.encode("café");
latin1Decoder.decode(data);  // may produce unexpected results or errors

// Cause 4: Base64 with non-ASCII characters
btoa("café");  // EncodingError in strict environments
```

## Solutions

### Fix 1: Handle fatal decoding errors gracefully

```javascript
function safeDecode(buffer, encoding = "utf-8") {
  // Use fatal: true to throw on invalid sequences
  const decoder = new TextDecoder(encoding, { fatal: true });
  try {
    return decoder.decode(buffer);
  } catch (err) {
    if (err.name === "TypeError") {
      console.error(`Invalid ${encoding} data, falling back to replacement`);
      // Fall back to non-fatal mode (replaces invalid with U+FFFD)
      const fallbackDecoder = new TextDecoder(encoding, { fatal: false });
      return fallbackDecoder.decode(buffer);
    }
    throw err;
  }
}
```

### Fix 2: Validate and sanitize percent-encoded URIs

```javascript
function safeDecodeUriComponent(str) {
  try {
    return decodeURIComponent(str);
  } catch (err) {
    if (err instanceof URIError) {
      console.error("Malformed URI component:", str);
      // Attempt to fix common issues
      const fixed = str
        .replace(/%(?![0-9A-Fa-f]{2})/g, "%25"); // encode stray %
      return decodeURIComponent(fixed);
    }
    throw err;
  }
}

// Usage
const decoded = safeDecodeUriComponent("hello%20world%ZZ");
```

### Fix 3: Use compatible encodings for cross-system data

```javascript
// When data comes from a system using Latin-1 (ISO-8859-1)
const latin1Bytes = new Uint8Array([0x63, 0x61, 0x66, 0xE9]); // "café"
const latin1Decoder = new TextDecoder("iso-8859-1");
const text = latin1Decoder.decode(latin1Bytes);  // "café"

// When encoding for transmission
const encoder = new TextEncoder();  // UTF-8
const utf8Bytes = encoder.encode(text);
```

### Fix 4: Handle Base64 encoding of non-ASCII strings

```javascript
function encodeBase64Unicode(str) {
  // Properly encode Unicode strings to Base64
  return btoa(
    encodeURIComponent(str).replace(/%([0-9A-F]{2})/g, (_, p1) =>
      String.fromCharCode(parseInt(p1, 16))
    )
  );
}

function decodeBase64Unicode(base64) {
  return decodeURIComponent(
    Array.from(atob(base64), (c) =>
      "%" + ("00" + c.charCodeAt(0).toString(16)).slice(-2)
    ).join("")
  );
}

// Usage
const encoded = encodeBase64Unicode("café");
const decoded = decodeBase64Unicode(encoded);  // "café"
```

## Examples

```javascript
// EncodingError when decoding corrupted network data
const response = await fetch("/api/data");
const buffer = await response.arrayBuffer();

const decoder = new TextDecoder("utf-8", { fatal: true });
try {
  const text = decoder.decode(buffer);
  console.log(text);
} catch (err) {
  console.error("Server returned corrupted data:", err.message);
}
```

## Related Errors

- [DataError]({{< relref "/languages/javascript/enodata" >}}) — data is invalid or malformed.
- [ERR_INVALID_URI]({{< relref "/languages/javascript/err_invalid_uri" >}}) — URI is malformed.
- [URIError]({{< relref "/languages/javascript/urierror" >}}) — malformed URI string.
- [SyntaxError]({{< relref "/languages/javascript/syntaxerror" >}}) — code has invalid syntax.
