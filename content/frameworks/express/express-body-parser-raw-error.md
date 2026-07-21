---
title: "[Solution] Express Body Parser Raw Error"
description: "Raw body not accessible."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Raw body not accessible.

## Common Causes

Wrong type.

## How to Fix

Use express.raw().

## Example

```javascript
app.use(express.raw({ type: 'application/octet-stream' }));
```
