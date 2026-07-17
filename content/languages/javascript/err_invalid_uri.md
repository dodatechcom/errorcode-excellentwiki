---
title: "[Solution] Node.js ERR_INVALID_URI — Malformed URI Fix"
description: "Fix Node.js ERR_INVALID_URI when parsing or creating URIs with invalid characters. Validate URIs, encode special characters, and use the URL constructor."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Node.js ERR_INVALID_URI — Malformed URI Fix

The `ERR_INVALID_URI` error occurs when a URI (Uniform Resource Identifier) contains invalid characters or is otherwise malformed. This appears in Node.js when parsing URLs, constructing URIs, or passing malformed URI strings to APIs that expect well-formed input.

## Description

Common ERR_INVALID_URI messages include:

- `Error [ERR_INVALID_URI]: URI must be a string` — non-string passed to URI parser.
- `Error [ERR_INVALID_URI]: Malformed URI` — invalid characters or structure.
- `URIError: URI malformed` — `decodeURIComponent` received invalid percent-encoding.

## Common Causes

```javascript
// Cause 1: Unencoded characters in URL path
const url = new URL("https://example.com/path with spaces");
// May cause issues in some contexts

// Cause 2: Invalid percent-encoding
decodeURIComponent("%E0%A4%A");  // URIError: URI malformed

// Cause 3: Non-string URI passed to URL constructor
new URL(123);  // TypeError, but similar errors occur with URI operations

// Cause 4: Null bytes or control characters in URI
const badUri = "https://example.com/path\x00with\x00nulls";
```

## Solutions

### Fix 1: Use the URL constructor for validation

```javascript
function safeParseUrl(uri) {
  try {
    return new URL(uri);
  } catch (err) {
    console.error("Invalid URI:", uri, err.message);
    return null;
  }
}

const url = safeParseUrl("https://example.com/path?q=1");
if (url) {
  console.log(url.hostname, url.pathname);
}
```

### Fix 2: Encode URI components properly

```javascript
// Wrong — spaces and special characters cause issues
const baseUrl = "https://api.example.com";
const path = "/search?q=hello world&type=full";
fetch(baseUrl + path);  // may fail

// Correct — encode the path and query
const url = new URL("/search", baseUrl);
url.searchParams.set("q", "hello world");
url.searchParams.set("type", "full");
fetch(url.toString());  // https://api.example.com/search?q=hello+world&type=full
```

### Fix 3: Handle malformed percent-encoding

```javascript
function safeDecodeUriComponent(str) {
  try {
    return decodeURIComponent(str);
  } catch (err) {
    if (err instanceof URIError) {
      // Fix common issues: stray % characters
      const fixed = str.replace(/%(?![0-9A-Fa-f]{2})/g, "%25");
      try {
        return decodeURIComponent(fixed);
      } catch {
        console.error("Cannot decode URI component:", str);
        return str;  // return original as fallback
      }
    }
    throw err;
  }
}

const decoded = safeDecodeUriComponent("hello%20world%ZZ");
```

### Fix 4: Build URIs using URL and URLSearchParams

```javascript
// Wrong — manual string concatenation
const uri = `https://api.example.com/users/${name}?filter=${filter}`;

// Correct — use URL and URLSearchParams
const url = new URL("https://api.example.com/users");
url.pathname += `/${encodeURIComponent(name)}`;
url.searchParams.set("filter", filter);
const uri = url.toString();
```

### Fix 5: Validate URIs before network operations

```javascript
async function safeFetch(uri) {
  // Validate URI format
  let url;
  try {
    url = new URL(uri);
  } catch {
    throw new Error(`Invalid URI: ${uri}`);
  }

  // Validate scheme
  if (!["http:", "https:", "file:"].includes(url.protocol)) {
    throw new Error(`Unsupported URI scheme: ${url.protocol}`);
  }

  return fetch(url.toString());
}
```

## Examples

```javascript
// ERR_INVALID_URI with file paths used as URIs
const filePath = "/home/user/my file (2).txt";

// Wrong — file path as URI string
const badUri = `file://${filePath}`;
// May contain unencoded parentheses and spaces

// Correct — properly encode the file path
const { pathToFileURL } = require("url");
const fileUri = pathToFileURL(filePath).href;
// file:///home/user/my%20file%20(2).txt

console.log(fileUri);
```

## Related Errors

- [DataError]({{< relref "/languages/javascript/enodata" >}}) — data is invalid or malformed.
- [EncodingError]({{< relref "/languages/javascript/encodingerr" >}}) — encoding or decoding operation failed.
- [URIError]({{< relref "/languages/javascript/urierror" >}}) — malformed URI string in browser context.
- [SyntaxError]({{< relref "/languages/javascript/syntaxerror" >}}) — code has invalid syntax.
