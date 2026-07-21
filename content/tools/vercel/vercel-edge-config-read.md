---
title: "[Solution] Vercel Edge Config Read Error"
description: "Fix Vercel Edge Config read errors. Resolve reading items from Edge Config."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["error"]
---

Vercel Edge Config Read Error can prevent your application from working correctly.

## Common Causes

- Key does not exist
- Connection timeout
- Token invalid
- Edge Config deleted

## How to Fix

### Read

```javascript
import { get, getAll } from '@vercel/edge-config';
const value = await get('my-key');
const all = await getAll();
```

