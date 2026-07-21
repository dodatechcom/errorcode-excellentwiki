---
title: "[Solution] Express Request Entity Too Large"
description: "Request too large."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Request too large.

## Common Causes

Body limit exceeded.

## How to Fix

Increase limit.

## Example

```javascript
app.use(express.json({ limit: '100mb' }));
```
