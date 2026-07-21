---
title: "[Solution] Deprecated Function Migration: default parameter pattern to ES6 defaults"
description: "Migrate from deprecated default parameter pattern to ES6 default parameter values in JavaScript."
deprecated_function: "x = x || default"
replacement_function: "function(x = default)"
languages: ["javascript"]
deprecated_since: "ES6/2015"
---

# [Solution] Deprecated Function Migration: default parameter pattern to ES6 defaults

The `x = x || default` has been deprecated in favor of `function(x = default)`.

## Migration Guide

ES6 default parameters only apply when the argument is undefined, not for all falsy values like x || default.

## Before (Deprecated)

```javascript
function greet(name, greeting) {
    name = name || "World";
    greeting = greeting || "Hello";
    return greeting + ", " + name + "!";
}
```

## After (Modern)

```javascript
function greet(name = "World", greeting = "Hello") {
    return `${greeting}, ${name}!`;
}

function divide(a, b = 1) {
    return a / b;
}

// Destructuring with defaults
function createUser({ name = "Anonymous", age = 0 } = {}) {
    return { name, age };
}
```

## Key Differences

- Default params only trigger on undefined
- x || default treats 0, '', false as missing
- Defaults work with destructuring
