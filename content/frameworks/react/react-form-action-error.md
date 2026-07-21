---
title: "[Solution] React Form Action Error"
description: "Form action not connected."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Form action not connected.

## Common Causes

Not using action prop.

## How to Fix

Use action prop.

## Example

```jsx
<form action={createPost}><input name="title" /><button>Submit</button></form>
```
