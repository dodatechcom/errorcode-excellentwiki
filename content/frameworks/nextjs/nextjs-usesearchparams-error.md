---
title: "[Solution] Next.js useSearchParams Error"
description: "useSearchParams not working."
frameworks: ["nextjs"]
error-types: ["framework-error"]
severities: ["error"]
---

useSearchParams not working.

## Common Causes

Wrong import.

## How to Fix

Import correctly.

## Example

```javascript
import { useSearchParams } from 'next/navigation';
const [sp] = useSearchParams();
const q = sp.get('q');
```
