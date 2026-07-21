---
title: "[Solution] Express req.fresh Error"
description: "req.fresh not working."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

req.fresh not working.

## Common Causes

Not checking cache.

## How to Fix

Use req.fresh.

## Example

```javascript
if (req.fresh) return res.sendStatus(304);
```
