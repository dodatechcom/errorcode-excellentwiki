---
title: "[Solution] React Cannot Read State or Props of Null"
description: "Error when a component tries to read state or props that are null."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Error when a component tries to read state or props that are null.

## Common Causes

Component receives null props or accesses state before initialization.

## How to Fix

Add default props and null checks.

## Example

```jsx
function UserProfile({ user }) {
  if (!user) return null;
  return <div>{user.name}</div>;
}
```
