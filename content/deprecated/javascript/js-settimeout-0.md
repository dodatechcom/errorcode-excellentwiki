---
title: "[Solution] Deprecated Function Migration: setTimeout(fn, 0) to queueMicrotask"
description: "Migrate from deprecated setTimeout(fn, 0) to queueMicrotask."
deprecated_function: "setTimeout(fn, 0)"
replacement_function: "queueMicrotask(fn)"
languages: ["javascript"]
deprecated_since: "ES2020"
---

# [Solution] Deprecated Function Migration: setTimeout(fn, 0) to queueMicrotask

The `setTimeout(fn, 0)` has been deprecated in favor of `queueMicrotask(fn)`.

## Migration Guide

queueMicrotask runs before next render.

## Before (Deprecated)

```javascript
setTimeout(() => {
    updateDOM();
}, 0);
```

## After (Modern)

```javascript
queueMicrotask(() => {
    updateDOM();
});
```

## Key Differences

- queueMicrotask runs before rendering
