---
title: "[Solution] Express Middleware Not Invoked"
description: "Middleware not executing."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Middleware not executing.

## Common Causes

Wrong registration.

## How to Fix

Register before routes.

## Example

```javascript
app.use((req, res, next) => { next(); });
```
