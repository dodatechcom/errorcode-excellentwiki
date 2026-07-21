---
title: "[Solution] Next.js useRouter Error"
description: "useRouter not working."
frameworks: ["nextjs"]
error-types: ["framework-error"]
severities: ["error"]
---

useRouter not working.

## Common Causes

Wrong import.

## How to Fix

Import from next/navigation.

## Example

```javascript
import { useRouter } from 'next/navigation';
const r = useRouter();
r.push('/dashboard');
```
