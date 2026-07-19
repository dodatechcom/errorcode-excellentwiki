---
title: "[Solution] TypeError Cannot Convert to Symbol / Primitive Fix"
description: "Fix TypeError when objects cannot be implicitly converted to primitives in JavaScript."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Cannot Convert to Primitive

```javascript
const obj = {};
const result = obj + 1; // [object Object]1 (not an error)

// But this errors:
const sym = Symbol('test');
sym + 1; // TypeError: Cannot convert a Symbol value to a number
```

## Fix

Implement `Symbol.toPrimitive` or `toString()`:

```javascript
const obj = {
  [Symbol.toPrimitive](hint) {
    if (hint === 'number') return 42;
    return 'default';
  }
};
```
