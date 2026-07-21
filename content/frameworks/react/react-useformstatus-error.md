---
title: "[Solution] React useFormStatus Error"
description: "Used outside form."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Used outside form.

## Common Causes

Not inside form.

## How to Fix

Must be inside form.

## Example

```jsx
function SB() {
  const { pending } = useFormStatus();
  return <button disabled={pending}>Submit</button>;
}
```
