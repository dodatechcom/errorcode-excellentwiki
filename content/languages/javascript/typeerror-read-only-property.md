---
title: "[Solution] TypeError Cannot Assign to Read Only Property Fix"
description: "Fix TypeError: Cannot assign to read only property when modifying frozen or sealed objects."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Cannot Assign to Read Only Property

```javascript
const obj = Object.freeze({ x: 1 });
obj.x = 2; // TypeError (silently fails in sloppy mode)

// Fix — use Object.assign for new object
const newObj = Object.assign({}, obj, { x: 2 });

// Or spread
const newObj2 = { ...obj, x: 2 };
```
