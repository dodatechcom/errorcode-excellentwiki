---
title: "[Solution] Express app.all Route Error"
description: "app.all not handling."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

app.all not handling.

## Common Causes

Wrong method.

## How to Fix

Use app.all.

## Example

```javascript
app.all('/api/*', (req, res, next) => { next(); });
```
