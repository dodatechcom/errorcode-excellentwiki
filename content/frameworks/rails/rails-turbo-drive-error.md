---
title: "[Solution] Rails Turbo Drive Error"
description: "Turbo Drive not working."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

Turbo Drive not working.

## Common Causes

Incompatible JS.

## How to Fix

Use turbo events.

## Example

```javascript
document.addEventListener('turbo:load', () => {});
```
