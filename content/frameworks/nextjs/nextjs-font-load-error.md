---
title: "[Solution] Next.js Font Load Error"
description: "Font not loading."
frameworks: ["nextjs"]
error-types: ["framework-error"]
severities: ["error"]
---

Font not loading.

## Common Causes

Wrong config.

## How to Fix

Use next/font.

## Example

```javascript
import { Inter } from 'next/font/google';
const i = Inter({ subsets: ['latin'] });
```
