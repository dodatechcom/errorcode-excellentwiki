---
title: "[Solution] Deprecated Function Migration: foreach with array_push to array_map"
description: "Migrate from deprecated foreach with push to array_map."
deprecated_function: "foreach + array_push"
replacement_function: "array_map()"
languages: ["php"]
deprecated_since: "PHP 5.3+"
---

# [Solution] Deprecated Function Migration: foreach with array_push to array_map

The `foreach + array_push` has been deprecated in favor of `array_map()`.

## Migration Guide

array_map is functional and concise

foreach with array_push is verbose. array_map is more functional.

## Before (Deprecated)

```php
$result = [];
foreach ($items as $item) {
    $result[] = strtoupper($item);
}
```

## After (Modern)

```php
$result = array_map(function($item) {
    return strtoupper($item);
}, $items);

// Arrow function (PHP 7.4+)
$result = array_map(fn($item) => strtoupper($item), $items);
```

## Key Differences

- array_map is more functional
- Arrow functions make it concise
- foreach for complex operations
- array_filter for filtering
