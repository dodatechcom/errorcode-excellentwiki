---
title: "[Solution] React Middleware Cookie Error"
description: "Middleware cookie access failing."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Middleware cookie access failing.

## Common Causes

Wrong usage.

## How to Fix

Use cookies().

## Example

```javascript
import { cookies } from 'next/headers';
const c = cookies();
```
