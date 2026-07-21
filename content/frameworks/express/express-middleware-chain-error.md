---
title: "[Solution] Express Middleware Chain Error"
description: "Middleware not chaining."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Middleware not chaining.

## Common Causes

Not calling next.

## How to Fix

Call next().

## Example

```javascript
app.use((req, res, next) => { /* do work */ next(); });
```
