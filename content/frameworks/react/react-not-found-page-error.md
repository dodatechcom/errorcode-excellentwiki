---
title: "[Solution] React Not Found Page Error"
description: "Custom 404 not configured."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Custom 404 not configured.

## Common Causes

Missing not-found.js.

## How to Fix

Create app/not-found.js.

## Example

```jsx
export default function NF() { return <h1>404</h1>; }
```
