---
title: "[Solution] React Data Cache Error"
description: "Data not caching."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Data not caching.

## Common Causes

No-store used.

## How to Fix

Use cache option.

## Example

```javascript
const d = await fetch('...', { cache: 'force-cache' });
```
