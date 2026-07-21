---
title: "[Solution] React Cannot Read Property of Undefined"
description: "Runtime error when accessing a property on an undefined value."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Runtime error when accessing a property on an undefined value.

## Common Causes

Accessing properties before data is loaded or on null/undefined values.

## How to Fix

Use optional chaining or null checks.

## Example

```javascript
const name = user?.profile?.name ?? 'Unknown';
```
