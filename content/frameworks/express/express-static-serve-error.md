---
title: "[Solution] Express Static Serve Error"
description: "express.static not serving."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

express.static not serving.

## Common Causes

Wrong directory.

## How to Fix

Verify directory.

## Example

```javascript
app.use(express.static(path.join(__dirname, 'public')));
```
