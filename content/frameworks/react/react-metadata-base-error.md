---
title: "[Solution] React Metadata Base Error"
description: "Metadata base URL wrong."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Metadata base URL wrong.

## Common Causes

Not set.

## How to Fix

Set metadataBase.

## Example

```javascript
export const metadata = { metadataBase: new URL('https://example.com'), title: 'My Site' };
```
