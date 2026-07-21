---
title: "[Solution] React startTransition Error"
description: "Error with startTransition."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Error with startTransition.

## Common Causes

Deferred state update.

## How to Fix

Use for non-urgent updates.

## Example

```javascript
startTransition(() => { setDeferred(v); });
```
