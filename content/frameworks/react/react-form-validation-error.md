---
title: "[Solution] React Form Validation Error"
description: "Client-side validation not working."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Client-side validation not working.

## Common Causes

Missing validation logic.

## How to Fix

Use controlled components.

## Example

```jsx
const [e, setE] = useState('');
const v = () => { if (!e.includes('@')) setE('Invalid'); };
```
