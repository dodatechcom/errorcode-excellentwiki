---
title: "[Solution] Reflect.apply TypeError — Invalid Arguments Fix"
description: "Fix TypeError when using Reflect.apply with wrong argument types. Validate function and arguments list."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Reflect.apply Error

```javascript
// Reflect.apply(target, thisArgument, argumentsList)
Reflect.apply('not a function', null, []); // TypeError
Reflect.apply(console.log, null, 'not array'); // TypeError

// Fix
Reflect.apply(console.log, console, ['hello']); // works
```
