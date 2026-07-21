---
title: "[Solution] React React.memo Comparison Error"
description: "Issues with React.memo custom comparison functions."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Issues with React.memo custom comparison functions.

## Common Causes

Custom areEqual function has incorrect logic.

## How to Fix

Ensure comparison returns correct boolean.

## Example

```javascript
const C = React.memo(C, (p, n) => p.name === n.name);
```
