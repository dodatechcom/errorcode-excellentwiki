---
title: "[Solution] React CSR vs SSR Confusion"
description: "Mismatch between client and server rendering."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Mismatch between client and server rendering.

## Common Causes

Using browser APIs on server.

## How to Fix

Use typeof window checks.

## Example

```javascript
const isBrowser = typeof window !== 'undefined';
```
