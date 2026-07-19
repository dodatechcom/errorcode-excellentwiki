---
title: "[Solution] RangeError Invalid Array Length — Fix in JavaScript"
description: "Fix RangeError: Invalid array length when creating arrays with negative or too-large sizes."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Invalid Array Length

```javascript
// These all throw RangeError
new Array(-1);
new Array(2**53);
new Array(Number.MAX_SAFE_INTEGER + 1);

// Also when using push to exceed safe size
const arr = [];
arr.length = -5; // RangeError
```

## Fix

Validate array sizes before creation:

```javascript
function safeArray(size) {
  if (!Number.isInteger(size) || size < 0 || size > Number.MAX_SAFE_INTEGER) {
    throw new RangeError('Invalid array length');
  }
  return new Array(size);
}
```
