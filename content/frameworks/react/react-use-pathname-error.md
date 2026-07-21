---
title: "[Solution] React use Pathname Error"
description: "usePathname not working."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

usePathname not working.

## Common Causes

Wrong import.

## How to Fix

Import from next/navigation.

## Example

```javascript
import { usePathname } from 'next/navigation';
const p = usePathname();
```
