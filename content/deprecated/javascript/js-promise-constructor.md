---
title: "[Solution] Deprecated Function Migration: new Promise(callback) to async/await"
description: "Migrate from verbose Promise constructor to async/await for simpler async code."
deprecated_function: "new Promise((resolve, reject) => { ... })"
replacement_function: "async function"
languages: ["javascript"]
deprecated_since: "ES2017"
---

# [Solution] Deprecated Function Migration: new Promise(callback) to async/await

The `new Promise((resolve, reject) => { ... })` has been deprecated in favor of `async function`.

## Migration Guide

async/await is more readable than Promise constructor

Promise constructor with callbacks can be verbose. async/await simplifies the pattern.

## Before (Deprecated)

```javascript
const fetchData = () => {
    return new Promise((resolve, reject) => {
        fetch('/api')
            .then(res => res.json())
            .then(data => resolve(data))
            .catch(err => reject(err));
    });
};
```

## After (Modern)

```javascript
const fetchData = async () => {
    const res = await fetch('/api');
    const data = await res.json();
    return data;
};
```

## Key Differences

- async functions return Promises
- await pauses until Promise resolves
- try/catch for error handling
- More readable than .then chains
