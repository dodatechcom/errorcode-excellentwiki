---
title: "[Solution] ReferenceError Invalid Left-Hand Side in Assignment Fix"
description: "Fix ReferenceError: Invalid left-hand side in assignment when the assignment target is not assignable."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Invalid Left-Hand Side in Assignment

```javascript
// Can't assign to result of function call
getInt() = 5;  // ReferenceError

// Can't assign to non-assignable
true = false;   // ReferenceError

// Fix — assign to variable
let value = 5;
value = getInt();
```
