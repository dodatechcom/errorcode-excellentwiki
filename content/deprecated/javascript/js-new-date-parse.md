---
title: "[Solution] Deprecated Function Migration: new Date to Date.UTC"
description: "Migrate from deprecated Date constructor to Date.UTC."
deprecated_function: "new Date(2024, 0, 15)"
replacement_function: "new Date(Date.UTC(2024, 0, 15))"
languages: ["javascript"]
deprecated_since: "Best Practice"
---

# [Solution] Deprecated Function Migration: new Date to Date.UTC

The `new Date(2024, 0, 15)` has been deprecated in favor of `new Date(Date.UTC(2024, 0, 15))`.

## Migration Guide

Date.UTC avoids timezone issues.

## Before (Deprecated)

```javascript
const date = new Date(2024, 0, 15);
```

## After (Modern)

```javascript
const date = new Date(Date.UTC(2024, 0, 15));
```

## Key Differences

- Date.UTC avoids timezone issues
