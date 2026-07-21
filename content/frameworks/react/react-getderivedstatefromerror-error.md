---
title: "[Solution] React getDerivedStateFromError Error"
description: "getDerivedStateFromError not returning state."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

getDerivedStateFromError not returning state.

## Common Causes

Not returning an object.

## How to Fix

Always return an object.

## Example

```javascript
static getDerivedStateFromError(e) { return { hasError: true }; }
```
