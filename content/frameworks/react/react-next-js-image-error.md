---
title: "[Solution] React Next.js Image Error"
description: "next/image blur not working."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

next/image blur not working.

## Common Causes

Wrong config.

## How to Fix

Set blurDataURL.

## Example

```javascript
<Image src="/img.png" placeholder="blur" blurDataURL="/blur.png" width={100} height={100} />
```
