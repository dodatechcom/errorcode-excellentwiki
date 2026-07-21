---
title: "[Solution] Express ENOENT Static File Error"
description: "Static file not found."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Static file not found.

## Common Causes

Wrong path.

## How to Fix

Ensure file exists.

## Example

```javascript
app.use(express.static('public'));
```
