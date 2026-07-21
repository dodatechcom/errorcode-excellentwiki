---
title: "[Solution] React Server Action revalidate Error"
description: "revalidate in action not working."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

revalidate in action not working.

## Common Causes

Wrong usage.

## How to Fix

Import and call.

## Example

```javascript
'use server';
import { revalidatePath } from 'next/cache';
export async function a() { await db.update(...); revalidatePath('/p'); }
```
