---
title: "[Solution] Express next() Not Called Error"
description: "Request hanging."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Request hanging.

## Common Causes

Forgetting next().

## How to Fix

Always call next().

## Example

```javascript
app.use((req, res, next) => { next(); });
```
