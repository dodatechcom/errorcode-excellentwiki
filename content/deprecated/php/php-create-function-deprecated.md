---
title: "[Solution] Deprecated Function Migration: create_function to anonymous function"
description: "Migrate from deprecated create_function to anonymous function."
deprecated_function: "create_function('$a, $b', 'return $a + $b;')"
replacement_function: "function($a, $b) { return $a + $b; }"
languages: ["php"]
deprecated_since: "PHP 7.2 / removed PHP 8.0"
---

# [Solution] Deprecated Function Migration: create_function to anonymous function

The `create_function('$a, $b', 'return $a + $b;')` has been deprecated in favor of `function($a, $b) { return $a + $b; }`.

## Migration Guide

create_function was removed.

## Before (Deprecated)

```php
$add = create_function('$a, $b', 'return $a + $b;');
```

## After (Modern)

```php
$add = function($a, $b) { return $a + $b; };
```

## Key Differences

- Anonymous functions are safer
