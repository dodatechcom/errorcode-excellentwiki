---
title: "[Solution] SyntaxError Missing Initializer in Destructuring"
description: "Fix SyntaxError: Missing initializer in destructuring declaration when using incomplete destructuring syntax."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Missing Initializer in Destructuring

```javascript
// Wrong — missing default or value
const { a, b } = ;  // SyntaxError

// Wrong — missing comma
const { a b } = obj;  // SyntaxError

// Correct
const { a, b } = obj;
const { a, b = 10 } = obj;
```
