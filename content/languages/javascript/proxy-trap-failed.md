---
title: "[Solution] Proxy TypeError — Trap Returned Falsish for Property Fix"
description: "Fix TypeError when Proxy handler traps return incorrect values. Ensure traps return correct types."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Proxy Trap Error

```javascript
const handler = {
  get(target, prop) {
    // Must return correct type for certain operations
    if (prop === Symbol.toPrimitive) return undefined; // TypeError possible
    return target[prop];
  }
};

const proxy = new Proxy({}, handler);
```

## Common Mistake

```javascript
// getPrototypeOf trap must return object or null
const handler2 = {
  getPrototypeOf() {
    return 42; // TypeError: expected object or null
  }
};
```
