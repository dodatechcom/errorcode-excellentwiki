---
title: "[Solution] Deprecated Function Migration: JSON.parse to safe parsing with validation"
description: "Migrate from deprecated JSON.parse without validation to safe parsing."
deprecated_function: "JSON.parse(data)"
replacement_function: "JSON.parse with try/catch and validation"
languages: ["javascript"]
deprecated_since: "Best Practice"
---

# [Solution] Deprecated Function Migration: JSON.parse to safe parsing with validation

The `JSON.parse(data)` has been deprecated in favor of `JSON.parse with try/catch and validation`.

## Migration Guide

JSON.parse can throw on invalid input.

## Before (Deprecated)

```javascript
const obj = JSON.parse(data);
```

## After (Modern)

```javascript
try {
    const obj = JSON.parse(data);
    // validate
} catch (e) {
    console.error('Invalid JSON');
}
```

## Key Differences

- Always validate JSON input
