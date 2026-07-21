---
title: "[Solution] Deprecated Function Migration: each() to foreach"
description: "Migrate from deprecated each() to foreach or current/next in PHP."
deprecated_function: "each()"
replacement_function: "foreach / current+next"
languages: ["php"]
deprecated_since: "PHP 7.2 / removed PHP 8.0"
---

# [Solution] Deprecated Function Migration: each() to foreach

The `each()` has been deprecated in favor of `foreach / current+next`.

## Migration Guide

each() was removed in PHP 8.0. Use foreach for iteration or current/key/next for pointer access.

## Before (Deprecated)

```php
$arr = ["a" => 1, "b" => 2];
while (list($key, $value) = each($arr)) {
    echo "$key => $value\n";
}
```

## After (Modern)

```php
$arr = ["a" => 1, "b" => 2];

foreach ($arr as $key => $value) {
    echo "$key => $value\n";
}

// Pointer access
$key = key($arr);
$value = current($arr);
next($arr);
```

## Key Differences

- foreach is the standard iteration construct
- current/key/next for pointer-based access
- foreach copies the array (no pointer side effects)
