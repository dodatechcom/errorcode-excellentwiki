---
title: "[Solution] React createRef vs useRef Confusion"
description: "createRef in function components re-creates each render."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

createRef in function components re-creates each render.

## Common Causes

createRef creates new ref.

## How to Fix

Use useRef in function components.

## Example

```javascript
const ref = useRef(null);
```
