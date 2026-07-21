---
title: "[Solution] React Router Push Error"
description: "router.push not working."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

router.push not working.

## Common Causes

Wrong usage.

## How to Fix

Use router.push.

## Example

```javascript
import { useRouter } from 'next/router';
const r = useRouter();
r.push('/dashboard');
```
