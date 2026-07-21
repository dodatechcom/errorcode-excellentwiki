---
title: "[Solution] Express Body Limit Error"
description: "Entity too large."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Entity too large.

## Common Causes

Limit exceeded.

## How to Fix

Increase limit.

## Example

```javascript
app.use(express.json({ limit: '50mb' }));
```
