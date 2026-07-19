---
title: "[Solution] SyntaxError Unexpected End of Input — Missing Bracket Fix"
description: "Fix SyntaxError: Unexpected end of input caused by missing closing brackets, parentheses, or quotes."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# SyntaxError: Unexpected End of Input

The parser reached the end of the file before completing a syntax construct.

## Common Causes

```javascript
// Missing closing bracket
function foo() {
  console.log('hello');
// } is missing

// Missing closing quote
const str = 'hello;

// Missing closing parenthesis
if (true console.log('yes');
```

## Fix

Use a code formatter (Prettier) or linter (ESLint) to catch these automatically.
