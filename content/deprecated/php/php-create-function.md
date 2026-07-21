---
title: "[Solution] Deprecated Function Migration: create_function to anonymous functions"
description: "Migrate from deprecated create_function() to anonymous functions or closures in PHP."
deprecated_function: "create_function()"
replacement_function: "anonymous functions / closures"
languages: ["php"]
deprecated_since: "PHP 7.2 / removed PHP 8.0"
---

# [Solution] Deprecated Function Migration: create_function to anonymous functions

The `create_function()` has been deprecated in favor of `anonymous functions / closures`.

## Migration Guide

create_function() was removed in PHP 8.0. Use anonymous functions which are faster and safer.

## Before (Deprecated)

```php
$greet = create_function("$name", "return \"Hello, $name!\";");
echo $greet("Alice");
```

## After (Modern)

```php
$greet = function($name) {
    return "Hello, $name!";
};
echo $greet("Alice");

// Arrow functions (PHP 7.4+)
$greet = fn($name) => "Hello, $name!";
$double = fn($x) => $x * 2;
```

## Key Differences

- Anonymous functions compiled at parse time
- No code injection risk
- Arrow functions (fn) for single expressions
- Support closures and use keyword
