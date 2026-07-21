---
title: "[Solution] React Lazy Import Failed"
description: "Error when React.lazy fails to load."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Error when React.lazy fails to load.

## Common Causes

Import path is wrong.

## How to Fix

Verify the import path.

## Example

```javascript
const C = React.lazy(() => import('./C'));
```
