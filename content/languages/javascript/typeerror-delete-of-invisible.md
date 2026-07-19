---
title: "[Solution] TypeError Cannot Delete Property — delete Operator Fix"
description: "Fix TypeError when using delete on non-configurable or non-deletable properties."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# TypeError: Cannot Delete Property

```javascript
// Built-in properties are non-configurable
delete Object.prototype; // TypeError

// Variables declared with var/let/const
const x = 1;
delete x; // TypeError (in strict mode)

// Fix — use object properties for deletable values
const config = { x: 1 };
delete config.x; // works
```
