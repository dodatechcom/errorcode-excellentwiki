---
title: "[Solution] Deprecated Function Migration: manual property extraction to destructuring"
description: "Migrate from deprecated manual property extraction to destructuring assignment in JavaScript."
deprecated_function: "var x = obj.x; var y = obj.y;"
replacement_function: "const { x, y } = obj;"
languages: ["javascript"]
deprecated_since: "ES6/2015"
---

# [Solution] Deprecated Function Migration: manual property extraction to destructuring

The `var x = obj.x; var y = obj.y;` has been deprecated in favor of `const { x, y } = obj;`.

## Migration Guide

Destructuring assignment allows extracting multiple properties in a single statement.

## Before (Deprecated)

```javascript
var response = getData();
var name = response.name;
var email = response.email;
var first = arr[0];
var second = arr[1];
```

## After (Modern)

```javascript
const { name, email, age } = getData();
const [first, second, third] = arr;

// Renaming
const { name: userName, email: userEmail } = getData();

// Default values
const { name, role = "user" } = getData();
```

## Key Differences

- Extract object properties by key name
- Extract array elements by position
- Support renaming and defaults
