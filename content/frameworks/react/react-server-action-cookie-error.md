---
title: "[Solution] React Server Action Cookie Error"
description: "Setting cookie in action."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Setting cookie in action.

## Common Causes

Wrong usage.

## How to Fix

Use cookies().

## Example

```javascript
'use server';
import { cookies } from 'next/headers';
cookies().set('name', 'value');
```
