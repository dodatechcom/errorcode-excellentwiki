---
title: "[Solution] TypeError Invalid First Argument — Type Checking Fix"
description: "Fix TypeError when passing wrong type to a function that performs type checking."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Invalid First Argument Type

```javascript
// Promise.all expects iterable
Promise.all(42);        // TypeError
Promise.all(null);      // TypeError

// Fix
Promise.all([]);        // correct
Promise.all([p1, p2]);  // correct
```
