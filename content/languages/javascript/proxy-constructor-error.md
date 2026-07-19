---
title: "[Solution] Proxy TypeError — Cannot Create Proxy of Non-Object Fix"
description: "Fix TypeError when trying to create a Proxy of a primitive value. Only objects and functions can be proxied."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Proxy Constructor Error

```javascript
// Only objects/functions can be proxied
new Proxy(42, {});    // TypeError
new Proxy('string', {}); // TypeError
new Proxy(null, {});     // TypeError

// Fix
const obj = { value: 42 };
const proxy = new Proxy(obj, {
  get(target, prop) {
    return target[prop];
  }
});
```
