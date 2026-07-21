---
title: "[Solution] Next.js redirect Function Error"
description: "redirect() not working."
frameworks: ["nextjs"]
error-types: ["framework-error"]
severities: ["error"]
---

redirect() not working.

## Common Causes

Wrong usage.

## How to Fix

Import correctly.

## Example

```javascript
import { redirect } from 'next/navigation';
if (!auth) redirect('/login');
```
