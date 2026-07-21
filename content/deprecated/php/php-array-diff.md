---
title: "[Solution] Deprecated Function Migration: manual array diff to array_diff"
description: "Migrate from deprecated manual comparison to array_diff functions."
deprecated_function: "Manual foreach comparison"
replacement_function: "array_diff()"
languages: ["php"]
deprecated_since: "PHP 4+"
---

# [Solution] Deprecated Function Migration: manual array diff to array_diff

The `Manual foreach comparison` has been deprecated in favor of `array_diff()`.

## Migration Guide

array_diff is built-in and optimized

Manual array comparison is error-prone.

## Before (Deprecated)

```php
$diff = [];
foreach ($arr1 as $val) {
    if (!in_array($val, $arr2)) {
        $diff[] = $val;
    }
}
```

## After (Modern)

```php
$diff = array_diff($arr1, $arr2);
$intersect = array_intersect($arr1, $arr2);
```

## Key Differences

- array_diff for difference
- array_intersect for intersection
