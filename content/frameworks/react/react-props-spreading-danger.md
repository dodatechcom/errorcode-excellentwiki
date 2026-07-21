---
title: "[Solution] React Props Spreading Danger"
description: "Warning about spreading unknown props on DOM elements."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Warning about spreading unknown props on DOM elements.

## Common Causes

Spreading all props on HTML.

## How to Fix

Pass only needed props.

## Example

```jsx
<div className={p.className} onClick={p.onClick} />
```
