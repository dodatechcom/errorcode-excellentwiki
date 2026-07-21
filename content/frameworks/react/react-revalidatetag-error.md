---
title: "[Solution] React revalidateTag Error"
description: "revalidateTag called wrong."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

revalidateTag called wrong.

## Common Causes

Outside server context.

## How to Fix

Only in server actions.

## Example

```javascript
'use server';
import { revalidateTag } from 'next/cache';
export async function u() { revalidateTag('posts'); }
```
