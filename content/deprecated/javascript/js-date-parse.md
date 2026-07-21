---
title: "[Solution] Deprecated Function Migration: new Date(string) to Date.parse"
description: "Migrate from deprecated Date constructor with string to explicit parsing."
deprecated_function: "new Date(string)"
replacement_function: "Date.parse(string) or components"
languages: ["javascript"]
deprecated_since: "Best Practice"
---

# [Solution] Deprecated Function Migration: new Date(string) to Date.parse

The `new Date(string)` has been deprecated in favor of `Date.parse(string) or components`.

## Migration Guide

Date constructor string parsing is inconsistent

Date constructor with string is inconsistent across browsers.

## Before (Deprecated)

```javascript
const date = new Date("2024-01-15");
```

## After (Modern)

```javascript
const timestamp = Date.parse("2024-01-15");
const date = new Date(timestamp);

// Better: use components
const d = new Date(2024, 0, 15);
```

## Key Differences

- Date.parse returns timestamp
- new Date(year, month, day) is explicit
- ISO 8601 format is safest
