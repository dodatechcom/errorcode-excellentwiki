---
title: "[Solution] Deprecated Function Migration: replace with string to replaceAll"
description: "Migrate from deprecated replace (only first match) to replaceAll."
deprecated_function: "str.replace('old', 'new')"
replacement_function: "str.replaceAll('old', 'new')"
languages: ["javascript"]
deprecated_since: "ES2021"
---

# [Solution] Deprecated Function Migration: replace with string to replaceAll

The `str.replace('old', 'new')` has been deprecated in favor of `str.replaceAll('old', 'new')`.

## Migration Guide

replaceAll replaces all occurrences.

## Before (Deprecated)

```javascript
const result = str.replace('old', 'new');
```

## After (Modern)

```javascript
const result = str.replaceAll('old', 'new');
```

## Key Differences

- replaceAll replaces all occurrences
