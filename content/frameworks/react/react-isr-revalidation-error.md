---
title: "[Solution] React ISR Revalidation Error"
description: "ISR not revalidating."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

ISR not revalidating.

## Common Causes

Wrong config.

## How to Fix

Set revalidate.

## Example

```javascript
export const revalidate = 3600;
```
