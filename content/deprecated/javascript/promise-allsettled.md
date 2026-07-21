---
title: "[Solution] Deprecated Function Migration: Promise.all to Promise.allSettled"
description: "Migrate from deprecated Promise.all error handling to Promise.allSettled for better error tolerance."
deprecated_function: "Promise.all"
replacement_function: "Promise.allSettled()"
languages: ["javascript"]
deprecated_since: "ES2020"
---

# [Solution] Deprecated Function Migration: Promise.all to Promise.allSettled

The `Promise.all` has been deprecated in favor of `Promise.allSettled()`.

## Migration Guide

Promise.allSettled waits for all promises and reports their status, making it better for batch operations.

## Before (Deprecated)

```javascript
const promises = [fetch(url1), fetch(url2), fetch(url3)];
try {
    const results = await Promise.all(promises);
} catch (err) {
    // One failed, others unknown
}
```

## After (Modern)

```javascript
const promises = [fetch(url1), fetch(url2), fetch(url3)];
const results = await Promise.allSettled(promises);

results.forEach((result, i) => {
    if (result.status === "fulfilled") {
        console.log(`Request ${i} succeeded:`, result.value);
    } else {
        console.log(`Request ${i} failed:`, result.reason);
    }
});
```

## Key Differences

- Promise.allSettled never rejects
- Each result has status: 'fulfilled' or 'rejected'
- Better for batch operations
