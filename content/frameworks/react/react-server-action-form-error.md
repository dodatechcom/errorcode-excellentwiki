---
title: "[Solution] React Server Action Form Error"
description: "Server action form not submitting."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Server action form not submitting.

## Common Causes

Wrong action.

## How to Fix

Use action prop.

## Example

```jsx
<form action={serverAction}><button>Submit</button></form>
```
