---
title: "[Solution] React API Route Error"
description: "API route not responding."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

API route not responding.

## Common Causes

Wrong export.

## How to Fix

Export handler.

## Example

```javascript
// pages/api/hello.js
export default function handler(req, res) { res.status(200).json({ d: 'ok' }); }
```
