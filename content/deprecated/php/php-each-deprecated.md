---
title: "[Solution] Deprecated Function Migration: each() to foreach loop"
description: "Migrate from deprecated each() to foreach."
deprecated_function: "each($array)"
replacement_function: "foreach ($array as $key => $value)"
languages: ["php"]
deprecated_since: "PHP 7.2 / removed PHP 8.0"
---

# [Solution] Deprecated Function Migration: each() to foreach loop

The `each($array)` has been deprecated in favor of `foreach ($array as $key => $value)`.

## Migration Guide

foreach is cleaner and more performant

each() was removed in PHP 8.0.

## Before (Deprecated)

```php
$arr = ['a' => 1];
while (list($k, $v) = each($arr)) {
    echo "$k => $v\n";
}
```

## After (Modern)

```php
$arr = ['a' => 1];
foreach ($arr as $key => $value) {
    echo "$key => $value\n";
}
```

## Key Differences

- foreach is the standard iteration
- each() removed in PHP 8.0
