---
title: "[Solution] React Route Handler Error"
description: "API route handler error."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

API route handler error.

## Common Causes

Incorrect exports.

## How to Fix

Export GET/POST functions.

## Example

```javascript
export async function GET(req) { return Response.json({ d: 'ok' }); }
```
