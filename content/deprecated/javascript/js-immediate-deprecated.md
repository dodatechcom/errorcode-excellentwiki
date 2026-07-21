---
title: "[Solution] Deprecated Function Migration: setImmediate to requestAnimationFrame"
description: "Migrate from deprecated setImmediate to requestAnimationFrame."
deprecated_function: "setImmediate(fn)"
replacement_function: "requestAnimationFrame(fn)"
languages: ["javascript"]
deprecated_since: "Browser"
---

# [Solution] Deprecated Function Migration: setImmediate to requestAnimationFrame

The `setImmediate(fn)` has been deprecated in favor of `requestAnimationFrame(fn)`.

## Migration Guide

requestAnimationFrame is standard.

## Before (Deprecated)

```javascript
setImmediate(() => {
    updateUI();
});
```

## After (Modern)

```javascript
requestAnimationFrame(() => {
    updateUI();
});
```

## Key Differences

- requestAnimationFrame is standard
