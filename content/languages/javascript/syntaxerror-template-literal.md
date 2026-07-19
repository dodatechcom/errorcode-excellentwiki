---
title: "[Solution] SyntaxError — Template Literal Syntax Error Fix"
description: "Fix SyntaxError with template literals: missing backticks, unclosed expressions, and nested template issues."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Template Literal Syntax Error

```javascript
// Missing closing backtick
const msg = `Hello ${name};

// Unclosed expression
const msg2 = `Hello ${getName();

// Wrong nesting
const msg3 = `Outer \`inner\``;
```

## Fix

```javascript
const msg = `Hello ${name}`;
const msg2 = `Result: ${getName()}`;
```
