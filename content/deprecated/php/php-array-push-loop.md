---
title: "[Solution] Deprecated Function Migration: foreach with array_push to [] operator"
description: "Migrate from deprecated array_push in loops to array spread or [] operator."
deprecated_function: "array_push($arr, $item)"
replacement_function: "$arr[] = $item"
languages: ["php"]
deprecated_since: "PHP 4+"
---

# [Solution] Deprecated Function Migration: foreach with array_push to [] operator

The `array_push($arr, $item)` has been deprecated in favor of `$arr[] = $item`.

## Migration Guide

[] operator is faster than array_push for single items

array_push has function call overhead. The [] operator is faster for adding single elements.

## Before (Deprecated)

```php
$arr = [];
foreach ($items as $item) {
    array_push($arr, $item);
}
```

## After (Modern)

```php
$arr = [];
foreach ($items as $item) {
    $arr[] = $item;
}

// Or use array spread (PHP 7.4+)
$arr = [...$existing, ...$new];

// Or use array_merge
$arr = array_merge($existing, $new);
```

## Key Differences

- [] operator is faster for single items
- array_push for adding multiple items at once
- Array spread for combining arrays
- array_merge for merging
