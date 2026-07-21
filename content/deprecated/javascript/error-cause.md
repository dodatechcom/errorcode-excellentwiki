---
title: "[Solution] Deprecated Function Migration: manual error chaining to Error cause"
description: "Migrate from deprecated error swallowing to Error cause property for error chaining in JavaScript."
deprecated_function: "new Error(msg)"
replacement_function: "new Error(msg, { cause })"
languages: ["javascript"]
deprecated_since: "ES2022"
---

# [Solution] Deprecated Function Migration: manual error chaining to Error cause

The `new Error(msg)` has been deprecated in favor of `new Error(msg, { cause })`.

## Migration Guide

The cause property preserves the original error when wrapping exceptions.

## Before (Deprecated)

```javascript
try {
    fetchData();
} catch (err) {
    throw new Error("Failed to fetch: " + err.message);
}
```

## After (Modern)

```javascript
try {
    fetchData();
} catch (err) {
    throw new Error("Failed to fetch", { cause: err });
}

// Accessing the cause
try {
    fetchData();
} catch (err) {
    console.log(err.message);  // "Failed to fetch"
    console.log(err.cause);    // original error object
}
```

## Key Differences

- cause property preserves original error
- err.cause accesses the wrapped error
- Stack traces include the full chain
