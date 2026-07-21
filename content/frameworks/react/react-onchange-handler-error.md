---
title: "[Solution] React onChange Handler Error"
description: "onChange not connected to state."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

onChange not connected to state.

## Common Causes

Not updating state.

## How to Fix

Use event to update.

## Example

```jsx
<input onChange={e => setName(e.target.value)} value={name} />
```
