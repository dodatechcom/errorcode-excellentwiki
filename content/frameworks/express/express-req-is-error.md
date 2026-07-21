---
title: "[Solution] Express req.is Error"
description: "req.is not checking correctly."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

req.is not checking correctly.

## Common Causes

Wrong mime type.

## How to Fix

Use correct type.

## Example

```javascript
if (req.is('json')) { /* handle JSON */ }
```
