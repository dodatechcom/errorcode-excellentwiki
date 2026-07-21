---
title: "[Solution] React Key Prop Missing in List"
description: "Warning when rendering lists without keys."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Warning when rendering lists without keys.

## Common Causes

Using map without key.

## How to Fix

Always add unique key prop.

## Example

```jsx
items.map(i => <div key={i.id}>{i.name}</div>)
```
