---
title: "[Solution] TypeError x is not a function — Calling Non-Callable Fix"
description: "Fix TypeError: x is not a function when trying to call a non-function value. Check variable types and imports."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# TypeError: x is not a function

```javascript
// Variable is not a function
const obj = { method: () => 1 };
const notFunc = obj.method;
obj.method();  // works
notFunc();     // also works (same reference)

// But if reassigned
let fn = null;
fn(); // TypeError: fn is not a function
```

## Common Causes

- Named export vs default export mismatch
- Import returns an object, not a function
- Module reassignment
