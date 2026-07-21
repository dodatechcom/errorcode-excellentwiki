---
title: "[Solution] React Ref Callback Error"
description: "Error when ref callback throws."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Error when ref callback throws.

## Common Causes

Not returning cleanup.

## How to Fix

Receive element on mount, null on unmount.

## Example

```javascript
const cb = (n) => { if (n) n.focus(); };
```
