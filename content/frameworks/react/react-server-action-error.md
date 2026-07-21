---
title: "[Solution] React Server Action Error"
description: "Server action misconfigured."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Server action misconfigured.

## Common Causes

Missing 'use server'.

## How to Fix

Add directive.

## Example

```javascript
'use server';
export async function submit(d) { await db.create(d); }
```
