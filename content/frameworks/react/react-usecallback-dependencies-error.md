---
title: "[Solution] React useCallback Dependencies Error"
description: "Warning when useCallback has incorrect dependencies."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Warning when useCallback has incorrect dependencies.

## Common Causes

Dependencies not matching callback body.

## How to Fix

Ensure all referenced values are in deps.

## Example

```javascript
const h = useCallback(() => { onClick(id); }, [onClick, id]);
```
