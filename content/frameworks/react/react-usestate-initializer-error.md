---
title: "[Solution] React useState Initializer Error"
description: "Error when useState initializer function has issues."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Error when useState initializer function has issues.

## Common Causes

Using expensive computation in initializer.

## How to Fix

Use lazy initialization with a function.

## Example

```javascript
const [s, setS] = useState(() => expensiveComputation());
```
