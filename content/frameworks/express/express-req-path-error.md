---
title: "[Solution] Express req.path Error"
description: "req.path wrong."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

req.path wrong.

## Common Causes

Includes base URL.

## How to Fix

Use req.path not req.url.

## Example

```javascript
const p = req.path;
```
