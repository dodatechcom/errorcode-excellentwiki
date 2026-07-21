---
title: "[Solution] Deprecated Function Migration: array_merge in loop to array spread"
description: "Migrate from deprecated array_merge in loop to array spread."
deprecated_function: "array_merge($arr, $new)"
replacement_function: "[...$arr, ...$new]"
languages: ["php"]
deprecated_since: "PHP 7.4+"
---

# [Solution] Deprecated Function Migration: array_merge in loop to array spread

The `array_merge($arr, $new)` has been deprecated in favor of `[...$arr, ...$new]`.

## Migration Guide

Array spread is more concise.

## Before (Deprecated)

```php
$result = [];
foreach ($arrays as $arr) {
    $result = array_merge($result, $arr);
}
```

## After (Modern)

```php
$result = array_merge(...$arrays);
```

## Key Differences

- array_merge with spread operator
