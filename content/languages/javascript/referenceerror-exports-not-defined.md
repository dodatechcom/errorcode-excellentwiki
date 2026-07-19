---
title: "[Solution] ReferenceError exports is not defined — CommonJS in Browser Fix"
description: "Fix ReferenceError: exports is not defined when using CommonJS syntax in browser or ESM context."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# ReferenceError: exports is not defined

```javascript
// This errors in ESM context
exports.myFunc = myFunc;

// Fix — use ES module syntax
export function myFunc() { ... }

// Or use module.exports in CommonJS
module.exports = { myFunc };
```
