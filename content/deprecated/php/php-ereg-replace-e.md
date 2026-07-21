---
title: "[Solution] Deprecated Function Migration: preg_replace with /e to preg_replace_callback"
description: "Migrate from deprecated preg_replace with /e modifier to preg_replace_callback."
deprecated_function: "preg_replace('/pattern/e', ...)"
replacement_function: "preg_replace_callback()"
languages: ["php"]
deprecated_since: "PHP 7.0"
---

# [Solution] Deprecated Function Migration: preg_replace with /e to preg_replace_callback

The `preg_replace('/pattern/e', ...)` has been deprecated in favor of `preg_replace_callback()`.

## Migration Guide

The /e modifier for evaluating replacement strings was removed in PHP 7.0. Use preg_replace_callback instead.

## Before (Deprecated)

```php
$pattern = "/(\\d+)/e";
$result = preg_replace($pattern, "$1 * 2", $input);
```

## After (Modern)

```php
$pattern = "/(\\d+)/";
$result = preg_replace_callback($pattern, function($matches) {
    return $matches[1] * 2;
}, $input);
```

## Key Differences

- /e modifier removed in PHP 7.0
- preg_replace_callback is the safe replacement
- Use anonymous function or Closure
- Much safer -- no code evaluation
