---
title: "[Solution] React Custom Document Error"
description: "_document.js not rendering."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

_document.js not rendering.

## Common Causes

Wrong structure.

## How to Fix

Define correctly.

## Example

```javascript
// pages/_document.js
import { Html, Head, Main, NextScript } from 'next/document';
export default function Document() {
  return <Html><Head /><body><Main /><NextScript /></body></Html>;
}
```
