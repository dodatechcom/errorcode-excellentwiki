---
title: "[Solution] JavaScript SyntaxError: Unexpected token in JSON Fix"
description: "Fix JavaScript SyntaxError: Unexpected token in JSON at position 0. Parse JSON safely, validate input, and handle malformed data with try/catch."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# SyntaxError: Unexpected token in JSON

A `SyntaxError: Unexpected token in JSON at position N` is thrown when `JSON.parse()` receives a string that is not valid JSON. The error points to the exact character position where parsing failed. This is one of the most common JavaScript errors when handling API responses.

## Description

JSON has strict syntax rules enforced by `JSON.parse()`. Unlike JavaScript object literals, JSON requires double quotes for strings and keys, does not allow trailing commas, and has no comments.

Common variants:

- `SyntaxError: Unexpected token < in JSON at position 0` — HTML instead of JSON
- `SyntaxError: Unexpected token } in JSON at position N` — trailing comma or missing comma
- `SyntaxError: Unexpected token u in JSON at position N` — `undefined` value
- `SyntaxError: Unexpected token N in JSON at position N` — `NaN` or `Infinity`

## Common Causes

```javascript
// Cause 1: HTML response instead of JSON
const data = await fetch("/api/data").then(r => r.json());
// If server returns HTML: SyntaxError: Unexpected token < in JSON at position 0

// Cause 2: Trailing comma
JSON.parse('{"key": "value",}');  // SyntaxError

// Cause 3: Single quotes (JS object syntax, not JSON)
JSON.parse("{'key': 'value'}");  // SyntaxError

// Cause 4: undefined or NaN values
JSON.parse('{"value": undefined}');  // SyntaxError
JSON.parse('{"value": NaN}');  // SyntaxError

// Cause 5: Comments in JSON
JSON.parse('{"key": "value" // comment}');  // SyntaxError
```

## How to Fix

### Fix 1: Check response content type before parsing

```javascript
// Wrong
const data = await fetch("/api/data").then(r => r.json());

// Correct
const response = await fetch("/api/data");
const contentType = response.headers.get("content-type");

if (contentType && contentType.includes("application/json")) {
    const data = await response.json();
} else {
    const text = await response.text();
    console.error("Expected JSON, got:", contentType, text.substring(0, 200));
}
```

### Fix 2: Wrap JSON.parse in try/catch

```javascript
// Wrong
const data = JSON.parse(rawString);

// Correct
let data;
try {
    data = JSON.parse(rawString);
} catch (err) {
    console.error("Invalid JSON at position", err.message);
    data = null;
}
```

### Fix 3: Use a safe JSON parsing helper

```javascript
function safeParseJSON(text, fallback = null) {
    if (typeof text !== "string" || !text.trim()) {
        return fallback;
    }
    try {
        return JSON.parse(text);
    } catch {
        return fallback;
    }
}

// Usage
const data = safeParseJSON(rawString, {});
const list = safeParseJSON(rawString, []);
```

### Fix 4: Handle fetch responses safely

```javascript
async function safeFetch(url) {
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }
        const text = await response.text();
        try {
            return JSON.parse(text);
        } catch {
            throw new Error(`Invalid JSON: ${text.substring(0, 100)}`);
        }
    } catch (err) {
        console.error(`Fetch failed for ${url}:`, err.message);
        return null;
    }
}
```

### Fix 5: Remove BOM and whitespace before parsing

```javascript
// BOM (Byte Order Mark) at start of string
const data = JSON.parse(text.replace(/^\uFEFF/, "").trim());
```

## Examples

This error commonly occurs when:

- API returns an HTML error page (403, 502, etc.) instead of JSON
- Proxy server injects HTML headers or content
- JSON string was built with template literals containing `undefined`
- A CDN returns a cached HTML error page

## Related Errors

- [TypeError: Failed to fetch](fetch-network-error) — network failure before JSON parsing
- [SyntaxError](syntaxerror) — JavaScript syntax errors (not JSON)
- [ReferenceError](referenceerror-settimeout) — variable not defined
