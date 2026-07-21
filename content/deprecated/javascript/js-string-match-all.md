---
title: "[Solution] Deprecated Function Migration: match with /g flag to matchAll"
description: "Migrate from deprecated match with global flag to matchAll."
deprecated_function: "str.match(/pattern/g)"
replacement_function: "str.matchAll(/pattern/g)"
languages: ["javascript"]
deprecated_since: "ES2020"
---

# [Solution] Deprecated Function Migration: match with /g flag to matchAll

The `str.match(/pattern/g)` has been deprecated in favor of `str.matchAll(/pattern/g)`.

## Migration Guide

matchAll returns iterator with capture groups.

## Before (Deprecated)

```javascript
const matches = str.match(/\\d+/g);
```

## After (Modern)

```javascript
const matches = str.matchAll(/(\\d+)(\\w+)/g);
for (const match of matches) {
    console.log(match[0], match[1], match[2]);
}
```

## Key Differences

- matchAll returns iterator
