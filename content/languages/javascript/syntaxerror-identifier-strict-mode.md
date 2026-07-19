---
title: "[Solution] SyntaxError — Strict Mode Reserved Word Identifier Fix"
description: "Fix SyntaxError in strict mode when using reserved words as identifiers or variable names."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Strict Mode Reserved Word Error

```javascript
'use strict';

// These are errors in strict mode
let let = 1;       // SyntaxError
const class = {};  // SyntaxError
var yield = 10;    // SyntaxError

function foo(let) {} // SyntaxError
```

## Fix

Rename the variable:

```javascript
let letValue = 1;
const classDef = {};
```
