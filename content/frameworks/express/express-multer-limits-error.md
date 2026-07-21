---
title: "[Solution] Express Multer Limits Error"
description: "Upload exceeding limits."
frameworks: ["express"]
error-types: ["framework-error"]
severities: ["error"]
---

Upload exceeding limits.

## Common Causes

Limits too strict.

## How to Fix

Adjust limits.

## Example

```javascript
const u = multer({ limits: { fileSize: 5 * 1024 * 1024 } });
```
