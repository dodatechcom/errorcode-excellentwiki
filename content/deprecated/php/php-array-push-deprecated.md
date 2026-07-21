---
title: "[Solution] Deprecated Function Migration: array_push to [] operator"
description: "Migrate from deprecated array_push to [] operator."
deprecated_function: "array_push($arr, $item)"
replacement_function: "$arr[] = $item"
languages: ["php"]
deprecated_since: "PHP 5.0+"
---

# [Solution] Deprecated Function Migration: array_push to [] operator

The `array_push($arr, $item)` has been deprecated in favor of `$arr[] = $item`.

## Migration Guide

[] operator is faster.

## Before (Deprecated)

```php
array_push($arr, $item);
```

## After (Modern)

```php
$arr[] = $item;
```

## Key Differences

- [] operator is faster
