---
title: "[Solution] TypeError Assignment to Constant Variable Fix"
description: "Fix TypeError: Assignment to constant variable. Understand const behavior and use let when reassignment is needed."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# TypeError: Assignment to Constant Variable

```javascript
const PI = 3.14159;
PI = 3; // TypeError: Assignment to constant variable

// Fix — use let
let counter = 0;
counter++; // works
```

## Trap: Block Scoping

```javascript
const x = 1;
if (true) {
  const x = 2; // new binding, different x
  console.log(x); // 2
}
console.log(x); // 1
```
