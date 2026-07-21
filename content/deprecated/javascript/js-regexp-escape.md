---
title: "[Solution] Deprecated Function Migration: manual regex escaping to RegExp.escape proposal"
description: "Migrate from deprecated manual regex escaping to RegExp.escape."
deprecated_function: 'str.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")'
replacement_function: "RegExp.escape(str)"
languages: ["javascript"]
deprecated_since: "Stage 3 Proposal"
---

# [Solution] Deprecated Function Migration: manual regex escaping to RegExp.escape proposal

The `str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')` has been deprecated in favor of `RegExp.escape(str)`.

## Migration Guide

RegExp.escape is cleaner.

## Before (Deprecated)

```javascript
function escapeRegex(str) {
    return str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}
```

## After (Modern)

```javascript
// When available
const pattern = new RegExp(RegExp.escape(str), 'g');
```

## Key Differences

- RegExp.escape is cleaner
