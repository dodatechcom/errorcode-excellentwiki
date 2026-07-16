---
title: "[Solution] JavaScript escape()/unescape() Deprecated — Use encodeURI()"
description: "Replace deprecated escape() and unescape() with encodeURI(), encodeURIComponent() and their decoding counterparts."
deprecated_function: "escape/unescape"
replacement_function: "encodeURI/decodeURI"
languages: ["javascript"]
deprecated_since: "ES3"
removed_in: "ES2018"
error_message: "escape is deprecated"
tags: ["escape", "unescape", "encode", "uri"]
weight: 90
---

# [Solution] JavaScript escape()/unescape() Deprecated — Use encodeURI()

The `escape()` and `unescape()` functions were deprecated in the ECMAScript 3 specification (1999) and removed in ES2018. They encode non-ASCII characters using a non-standard `%uXXXX` format that is not part of the URI specification. The correct replacements are `encodeURI()`/`decodeURI()` for full URIs and `encodeURIComponent()`/`decodeURIComponent()` for URI components.

## What You'll See

In modern JavaScript environments, using `escape()` or `unescape()` triggers a deprecation warning:

```
escape is deprecated
```

In strict mode or newer engines, you may see:

```
ReferenceError: escape is not defined
```

## Why Deprecated

`escape()` and `unescape()` were removed because:

- **Non-standard encoding**: They used `%uXXXX` notation for Unicode characters, which is not part of the URI specification (RFC 3986).
- **Security issues**: The `%u` encoding could bypass security checks that expected standard percent-encoding.
- **Inconsistency**: They encoded spaces as `%20` but did not encode `+`, `/`, `?`, `:`, `@`, and other URI-reserved characters that need encoding in certain contexts.
- **Standardized replacements**: `encodeURI()` and `encodeURIComponent()` follow the URI specification exactly.

## Old Code (Deprecated)

```javascript
// Encoding a string
var name = "John Doe";
var encoded = escape(name);
console.log(encoded); // "John%20Doe"

// Encoding with special characters
var text = "Hello, World! café";
console.log(escape(text)); // "Hello%2C%20World%21%20caf%E9"

// Decoding
var decoded = unescape("Hello%2C%20World%21");
console.log(decoded); // "Hello, World!"

// Encoding for a URL parameter
var search = "hello world & foo=bar";
var param = "q=" + escape(search);
// This produces a non-standard encoded string
```

## New Code (Replacement)

```javascript
// encodeURI() — for encoding a complete URI
// Does NOT encode: ; , / ? : @ & = + $ - _ . ! ~ * ' ( )
var uri = "https://example.com/path with spaces";
console.log(encodeURI(uri));
// "https://example.com/path%20with%20spaces"

// encodeURIComponent() — for encoding a URI component (part of a URL)
// Encodes almost everything except: - _ . ! ~ * ' ( )
var search = "hello world & foo=bar";
var param = "q=" + encodeURIComponent(search);
console.log(param);
// "q=hello%20world%20%26%20foo%3Dbar"

// Encoding with non-ASCII characters
var text = "Hello, World! café";
console.log(encodeURI(text));
// "Hello,%20World!%20caf%C3%A9"

console.log(encodeURIComponent(text));
// "Hello%2C%20World!%20caf%C3%A9"

// Decoding
console.log(decodeURIComponent("Hello%2C%20World!"));
// "Hello, World!"

console.log(decodeURI("https://example.com/path%20with%20spaces"));
// "https://example.com/path with spaces"

// Practical example: building a URL with query parameters
function buildUrl(base, params) {
  var query = Object.keys(params)
    .map(function(key) {
      return encodeURIComponent(key) + "=" + encodeURIComponent(params[key]);
    })
    .join("&");
  return base + "?" + query;
}

var url = buildUrl("https://api.example.com/search", {
  q: "hello & goodbye",
  page: "1"
});
// "https://api.example.com/search?q=hello%20%26%20goodbye&page=1"
```

## encodeURI vs encodeURIComponent

Choose the right function based on what you are encoding:

| Function | Use Case | Encodes Spaces | Encodes `/` | Encodes `?` `&` `=` |
|---|---|---|---|---|
| `encodeURI()` | Full URL | `%20` | No | No |
| `encodeURIComponent()` | URL parameter value | `%20` | `%2F` | `%3F` `%26` `%3D` |

Example:

```javascript
var url = "https://example.com/path?q=hello world";

// WRONG — encodeURI does not encode query string characters
var broken = "https://example.com" + encodeURI("/path?q=hello world");
// "https://example.com/path?q=hello%20world" — looks correct but...

// CORRECT — use encodeURIComponent for query values
var correct = "https://example.com/path?q=" + encodeURIComponent("hello world");
// "https://example.com/path?q=hello%20world"
```

## Migration Steps

1. **Find all escape() and unescape() calls**:

```bash
grep -rn "\bescape\s*(" --include="*.js" /path/to/project/
grep -rn "\bunescape\s*(" --include="*.js" /path/to/project/
```

2. **Determine the context.** If you are encoding a full URL, use `encodeURI()`. If you are encoding a value that will be placed inside a URL (like a query parameter), use `encodeURIComponent()`.

3. **Replace `escape()` with the appropriate function**. Watch for the `%u` encoding format — if your code checks for `%u` patterns, those need to be updated to standard `%XX` or `%uXXXX` handling with `String.fromCharCode()`.

4. **Replace `unescape()` with `decodeURI()` or `decodeURIComponent()`** using the same context-based decision.

5. **Test encoding behavior** with non-ASCII characters, spaces, and URI-reserved characters (`&`, `=`, `+`, `/`, `?`).

6. **Search for related deprecated patterns** like `substr()`:

```bash
grep -rn "\.substr\s*(" --include="*.js" /path/to/project/
```
