---
title: "[Solution] Deprecated Function Migration: window.name for data to sessionStorage"
description: "Migrate from deprecated window.name for data passing to sessionStorage."
deprecated_function: "window.name = data"
replacement_function: "sessionStorage.setItem('key', data)"
languages: ["javascript"]
deprecated_since: "Best Practice"
---

# [Solution] Deprecated Function Migration: window.name for data to sessionStorage

The `window.name = data` has been deprecated in favor of `sessionStorage.setItem('key', data)`.

## Migration Guide

window.name is a string and persists across navigation.

## Before (Deprecated)

```javascript
window.name = JSON.stringify(data);
```

## After (Modern)

```javascript
sessionStorage.setItem('myData', JSON.stringify(data));
```

## Key Differences

- sessionStorage is more appropriate
