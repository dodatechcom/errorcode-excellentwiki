---
title: "[Solution] ReferenceError Cannot Access Before Initialization — Temporal Dead Zone"
description: "Fix ReferenceError: Cannot access 'x' before initialization caused by the Temporal Dead Zone with let/const."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Cannot Access Before Initialization (TDZ)

```javascript
// Temporal Dead Zone
console.log(x); // ReferenceError
let x = 1;

// Function hoisting works
console.log(fn()); // works
function fn() { return 1; }
```

## Fix

Declare variables before use. Don't rely on hoisting with `let`/`const`.
