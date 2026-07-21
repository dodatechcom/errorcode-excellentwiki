---
title: "[Solution] React Font CSS Error"
description: "Font CSS not loading."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Font CSS not loading.

## Common Causes

Wrong import.

## How to Fix

Use next/font.

## Example

```javascript
import { Roboto } from 'next/font/google';
const roboto = Roboto({ subsets: ['latin'], weight: ['400', '700'] });
```
