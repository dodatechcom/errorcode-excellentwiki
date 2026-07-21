---
title: "[Solution] Deprecated Function Migration: callbacks to Promises"
description: "Migrate from deprecated callback pattern to Promises in JavaScript for cleaner async code."
deprecated_function: "callbacks"
replacement_function: "Promises"
languages: ["javascript"]
deprecated_since: "ES6/2015"
---

# [Solution] Deprecated Function Migration: callbacks to Promises

The `callbacks` has been deprecated in favor of `Promises`.

## Migration Guide

The callback pattern leads to deeply nested code (callback hell). Promises provide a cleaner way to handle async operations with .then() chains and .catch() for errors.

## Before (Deprecated)

```javascript
getData(function(a) {
    getMoreData(a, function(b) {
        getEvenMoreData(b, function(c) {
            console.log(c);
        });
    });
});
```

## After (Modern)

```javascript
getData()
    .then(a => getMoreData(a))
    .then(b => getEvenMoreData(b))
    .then(c => console.log(c))
    .catch(err => console.error(err));
```

## Key Differences

- Promises flatten nested callbacks into linear chains
- .catch() handles errors at any point
- Promises are composable with Promise.all/race
