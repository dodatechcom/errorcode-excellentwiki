---
title: "[Solution] Deprecated Function Migration: eval() to JSON.parse and safe alternatives"
description: "Migrate from deprecated eval() usage to JSON.parse and safe alternatives in JavaScript."
deprecated_function: "eval(data)"
replacement_function: "JSON.parse(data)"
languages: ["javascript"]
deprecated_since: "All versions"
---

# [Solution] Deprecated Function Migration: eval() to JSON.parse and safe alternatives

The `eval(data)` has been deprecated in favor of `JSON.parse(data)`.

## Migration Guide

eval() executes arbitrary code creating security vulnerabilities. Use JSON.parse for JSON data.

## Before (Deprecated)

```javascript
var data = eval("(" + jsonString + ")");
var fn = eval("(" + funcString + ")");
var prop = "name";
var value = eval("obj." + prop);
```

## After (Modern)

```javascript
const data = JSON.parse(jsonString);
const prop = "name";
const value = obj[prop];
const fn = new Function("return " + funcString)();
```

## Key Differences

- Never use eval for JSON -- use JSON.parse
- Use bracket notation for dynamic properties
- eval is a security vulnerability
