---
title: "[Solution] Cannot Find Name Error — Undefined Identifier in JavaScript"
description: "Fix 'cannot find name' when using an undeclared variable in TypeScript or JavaScript."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Cannot Find Name — Undefined Identifier

This error occurs when a variable or function is referenced before being declared.

## Causes

- Typo in variable name
- Variable declared in a different scope
- Missing import

```javascript
// Typo
console.log(nme); // ReferenceError: nme is not defined

// Wrong scope
function foo() { let x = 1; }
console.log(x); // ReferenceError
```
