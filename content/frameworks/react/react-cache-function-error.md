---
title: "[Solution] React cache Function Error"
description: "cache() used wrong."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

cache() used wrong.

## Common Causes

Outside server components.

## How to Fix

For single-request memoization.

## Example

```javascript
import { cache } from 'react';
const gU = cache(async (id) => await db.find(id));
```
