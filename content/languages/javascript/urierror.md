---
title: "[Solution] JavaScript URIError — Malformed URI Encoding Fix"
description: "Fix JavaScript URIError from decodeURI/decodeURIComponent on invalid input. Use correct encoding functions, handle unicode, and validate URIs."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
tags: ["urierror", "encodeuri", "decodeuri", "unicode", "encoding"]
weight: 78
---

# URIError — Malformed URI Encoding Fix

A `URIError` in JavaScript is thrown when a malformed URI is passed to `decodeURI()`, `decodeURIComponent()`, `encodeURI()`, or `encodeURIComponent()`. This typically happens when decoding a string that contains invalid percent-encoding sequences like `%ZZ` or a standalone `%` character.

## Common Causes

```javascript
// Cause 1: Decoding a string with invalid percent-encoding
decodeURIComponent("%ZZ");  // URIError: URI malformed
decodeURI("%zz");  // URIError: URI malformed

// Cause 2: Standalone percent sign
decodeURIComponent("%");  // URIError: URI malformed
decodeURIComponent("hello%world");  // URIError: URI malformed

// Cause 3: Incomplete percent-encoding
decodeURIComponent("%2");  // URIError: URI malformed
decodeURIComponent("test%2F%");  // URIError: URI malformed

// Cause 4: Double encoding issues
const doubleEncoded = encodeURIComponent("%20");  // "%2520"
decodeURIComponent(decodeURIComponent(doubleEncoded));  // URIError

// Cause 5: Encoding non-string values
encodeURI(12345);  // Works (auto-converted), but can cause issues
```

## Solutions

### Fix 1: Wrap decode calls in try-catch

```javascript
// Wrong — crashes on malformed input
function decodeUserInput(input) {
    return decodeURIComponent(input);
}
decodeUserInput("hello%");  // URIError

// Correct — handle the error gracefully
function decodeUserInput(input) {
    try {
        return decodeURIComponent(input);
    } catch (e) {
        if (e instanceof URIError) {
            console.warn("Malformed URI input, returning raw value");
            return input;
        }
        throw e;
    }
}
```

### Fix 2: Use encodeURI vs encodeURIComponent correctly

```javascript
// Wrong — using encodeURI for query parameters (does not encode & = ? etc.)
const search = "hello world & foo=bar";
const url = "https://api.example.com/search?q=" + encodeURI(search);
// Broken: the & in the search value splits the query string

// Correct — use encodeURIComponent for values
const url = "https://api.example.com/search?q=" + encodeURIComponent(search);
// "https://api.example.com/search?q=hello%20world%20%26%20foo%3Dbar"

// encodeURI is for full URIs where you want to preserve structure:
const base = encodeURI("https://example.com/path with spaces");
// "https://example.com/path%20with%20spaces"
```

### Fix 3: Pre-validate strings before decoding

```javascript
// Wrong — decoding raw user input
function processUrl(url) {
    return decodeURIComponent(url.split("?q=")[1]);
}

// Correct — validate the input is properly encoded first
function isValidPercentEncoded(str) {
    return /^%[0-9A-Fa-f]{2}|[^%]*$/.test(str);
}

function processUrl(url) {
    const queryValue = url.split("?q=")[1] ?? "";
    if (!isValidPercentEncoded(queryValue)) {
        throw new URIError(`Invalid percent-encoding in: ${queryValue}`);
    }
    return decodeURIComponent(queryValue);
}
```

### Fix 4: Handle unicode safely

```javascript
// Wrong — may produce invalid sequences
function decodeWithUnicode(input) {
    return decodeURIComponent(input);
}

// Correct — handle surrogate pairs and invalid UTF-8
function decodeWithUnicode(input) {
    try {
        // First pass: standard decoding
        const decoded = decodeURIComponent(input);
        // Second pass: verify the result is valid UTF-8
        const encoder = new TextEncoder();
        const bytes = encoder.encode(decoded);
        const decoder = new TextDecoder("utf-8", { fatal: true });
        return decoder.decode(bytes);
    } catch (e) {
        if (e instanceof URIError || e instanceof TypeError) {
            return input; // return raw input on failure
        }
        throw e;
    }
}
```

### Fix 5: Safe decode utility for untrusted input

```javascript
// Safe utility that never throws on untrusted input
function safeDecode(value, fallback = "") {
    if (typeof value !== "string") return fallback;
    try {
        return decodeURIComponent(value);
    } catch {
        try {
            return decodeURI(value);
        } catch {
            return fallback;
        }
    }
}

// Usage with user input from query string
const params = new URLSearchParams(window.location.search);
const searchTerm = safeDecode(params.get("q"), "default");
```

## encodeURI vs encodeURIComponent Quick Reference

| Function | Use Case | Encodes `/` | Encodes `?&=` |
|---|---|---|---|
| `encodeURI()` | Full URL | No | No |
| `encodeURIComponent()` | URL parameter values | Yes (`%2F`) | Yes (`%3F%26%3D`) |
| `decodeURI()` | Decode full URL | No | No |
| `decodeURIComponent()` | Decode parameter values | Yes | Yes |

## Prevention Tips

- Always wrap `decodeURI`/`decodeURIComponent` calls in try-catch for untrusted input.
- Use `encodeURIComponent()` for query parameter values, `encodeURI()` for full URLs.
- Prefer `new URL()` and `URLSearchParams` for URL construction — they handle encoding automatically.
- Never pass user-controlled strings to decoding functions without validation.

## Related Errors

- [RangeError](rangeerror) — value outside valid range.
- [SyntaxError](syntaxerror) — invalid code syntax during parsing.
- [ReferenceError](referenceerror) — variable not defined in scope.
