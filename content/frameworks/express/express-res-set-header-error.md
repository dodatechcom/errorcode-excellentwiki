---
title: "[Solution] Express res.set Header Error"
description: "Headers not set."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Headers not set.

## Common Causes

Wrong usage.

## How to Fix

Use res.set.

## Example

```javascript
res.set('X-Custom', 'value');
```
