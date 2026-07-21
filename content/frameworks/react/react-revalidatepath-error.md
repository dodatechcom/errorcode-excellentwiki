---
title: "[Solution] React revalidatePath Error"
description: "revalidatePath called wrong."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

revalidatePath called wrong.

## Common Causes

Outside server actions.

## How to Fix

Only in server actions.

## Example

```javascript
'use server';
import { revalidatePath } from 'next/cache';
export async function u() { revalidatePath('/dash'); }
```
