---
title: "[Solution] Deprecated Function Migration: .then().then() to async/await"
description: "Migrate from deprecated promise chains to async/await."
deprecated_function: ".then().then().then()"
replacement_function: "async/await"
languages: ["javascript"]
deprecated_since: "ES2017"
---

# [Solution] Deprecated Function Migration: .then().then() to async/await

The `.then().then().then()` has been deprecated in favor of `async/await`.

## Migration Guide

async/await is more readable.

## Before (Deprecated)

```javascript
fetchData()
    .then(data => process(data))
    .then(result => save(result))
    .then(() => done());
```

## After (Modern)

```javascript
const data = await fetchData();
const result = await process(data);
await save(result);
done();
```

## Key Differences

- async/await is more readable
