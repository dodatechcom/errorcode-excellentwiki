---
title: "[Solution] React Server Reference Error"
description: "Server actions not defined."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Server actions not defined.

## Common Causes

Missing 'use server'.

## How to Fix

Add 'use server' directive.

## Example

```javascript
'use server';
export async function create(d) { await db.create(d); }
```
