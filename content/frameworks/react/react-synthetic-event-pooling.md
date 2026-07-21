---
title: "[Solution] React Synthetic Event Pooling"
description: "Warning about accessing event after async."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Warning about accessing event after async.

## Common Causes

Events nullified after callback.

## How to Fix

Save values before async.

## Example

```javascript
function h(e) { const v = e.target.value; setTimeout(() => console.log(v), 100); }
```
