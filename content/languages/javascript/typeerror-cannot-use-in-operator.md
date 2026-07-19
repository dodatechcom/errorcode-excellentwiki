---
title: "[Solution] TypeError Cannot Use 'in' Operator to Search for Property Fix"
description: "Fix TypeError: Cannot use 'in' operator to search for 'X' in Y when using 'in' on non-objects."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Cannot Use 'in' Operator

```javascript
// 'in' requires an object
'name' in 'string';  // TypeError
'name' in null;      // TypeError
'name' in undefined; // TypeError

// Fix — check type first
function hasProperty(obj, key) {
  return obj !== null && typeof obj === 'object' && key in obj;
}
```
