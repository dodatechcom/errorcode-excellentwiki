---
title: "[Solution] React setState Called in Render"
description: "Warning when setState is called directly inside a render function."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Warning when setState is called directly inside a render function.

## Common Causes

Calling setState without useEffect.

## How to Fix

Use useEffect for side effects.

## Example

```javascript
useEffect(() => { setProcessed(transform(data)); }, [data]);
```
