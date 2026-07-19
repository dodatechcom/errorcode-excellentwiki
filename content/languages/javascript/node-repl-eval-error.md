---
title: "[Solution] Node.js REPL Eval Error — Unexpected Token in Interactive Mode"
description: "Fix errors in Node.js REPL when eval fails on invalid input. Handle REPL context errors gracefully."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Node.js REPL Eval Error

The Node.js REPL catches eval errors and displays them.

## Common REPL Errors

```javascript
> { const x = 1 }  // SyntaxError — braces confused with block
> eval('{ const x = 1 }')  // works as expression

> function foo() {} // SyntaxError in REPL
// Use arrow functions or wrap in parens
> const foo = () => {}
```
