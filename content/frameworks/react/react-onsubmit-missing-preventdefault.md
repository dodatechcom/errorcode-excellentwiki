---
title: "[Solution] React onSubmit Missing preventDefault"
description: "Form refreshing on submit."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Form refreshing on submit.

## Common Causes

Not calling preventDefault.

## How to Fix

Always call preventDefault.

## Example

```jsx
<form onSubmit={e => { e.preventDefault(); submit(); }}>
```
