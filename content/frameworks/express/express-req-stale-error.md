---
title: "[Solution] Express req.stale Error"
description: "req.stale not working."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

req.stale not working.

## Common Causes

Not checking cache.

## How to Fix

Use req.stale.

## Example

```javascript
if (req.stale) res.set('Cache-Control', 'no-cache');
```
