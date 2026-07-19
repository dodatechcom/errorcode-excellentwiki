---
title: "[Solution] TypeError Cannot Define Property on Non-Object Fix"
description: "Fix TypeError: Cannot define property when trying to define a property on a primitive value."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Cannot Define Property on Non-Object

```javascript
// Primitives can't have properties defined
Object.defineProperty('string', 'key', {});  // TypeError
Object.defineProperty(42, 'key', {});         // TypeError

// Fix — only define on objects
const obj = {};
Object.defineProperty(obj, 'key', { value: 1 });
```
