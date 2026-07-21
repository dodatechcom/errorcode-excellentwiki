---
title: "[Solution] Deprecated Function Migration: string concatenation to template literals"
description: "Migrate from deprecated string concatenation to template literals in JavaScript for readable strings."
deprecated_function: "string + concatenation"
replacement_function: "template literals"
languages: ["javascript"]
deprecated_since: "ES6/2015"
---

# [Solution] Deprecated Function Migration: string concatenation to template literals

The `string + concatenation` has been deprecated in favor of `template literals`.

## Migration Guide

Template literals use backticks and ${} for embedding expressions, making strings more readable.

## Before (Deprecated)

```javascript
var name = "Alice";
var greeting = "Hello, " + name + "! You have " + count + " messages.";
var html = "<div class=\"card\"><h1>" + title + "</h1></div>";
```

## After (Modern)

```javascript
const name = "Alice";
const greeting = `Hello, ${name}! You have ${count} messages.`;
const html = `<div class="card"><h1>${title}</h1></div>`;

// Multi-line
const multi = `Line 1
Line 2
Line 3`;
```

## Key Differences

- Use backticks for template literals
- Embed expressions with ${}
- Multi-line strings without \n
