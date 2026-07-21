---
title: "[Solution] React useRef Not Mutable Error"
description: "Error when trying to use useRef incorrectly."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Error when trying to use useRef incorrectly.

## Common Causes

Misunderstanding useRef returns {current}.

## How to Fix

Access and modify the .current property.

## Example

```javascript
const ref = useRef(null);
ref.current = 'new value';
```
