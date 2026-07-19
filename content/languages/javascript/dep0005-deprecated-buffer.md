---
title: "[Solution] DEP0005 — Deprecation Warning: Buffer() Constructor"
description: "Fix DEP0005 deprecation warning for Buffer() constructor. Use Buffer.alloc(), Buffer.from(), or Buffer.allocUnsafe()."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# DEP0005 — Buffer() is Deprecated

The `Buffer()` and `new Buffer()` constructors are deprecated due to security concerns.

## Fix

```javascript
// Deprecated
const buf = Buffer(16);
const buf2 = new Buffer('hello');

// Safe alternatives
const buf3 = Buffer.alloc(16);          // zero-filled
const buf4 = Buffer.allocUnsafe(16);    // uninitialized (faster)
const buf5 = Buffer.from('hello');       // from string
const buf6 = Buffer.from([1, 2, 3]);    // from array
```
