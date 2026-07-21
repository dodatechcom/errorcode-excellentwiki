---
title: "[Solution] React Edge API Route Error"
description: "Edge API route failing."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Edge API route failing.

## Common Causes

Not compatible.

## How to Fix

Use Edge runtime.

## Example

```javascript
export const runtime = 'edge';
export async function GET(req) { return Response.json({ d: 'ok' }); }
```
