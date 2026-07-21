---
title: "[Solution] React Custom App Error"
description: "_app.js not loading."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

_app.js not loading.

## Common Causes

Wrong file location.

## How to Fix

Create in pages/.

## Example

```javascript
// pages/_app.js
export default function App({ Component, pageProps }) {
  return <Component {...pageProps} />;
}
```
