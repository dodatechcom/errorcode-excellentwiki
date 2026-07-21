---
title: "[Solution] Deprecated Function Migration: ereg functions to preg_match"
description: "Migrate from deprecated ereg functions to preg_match."
deprecated_function: "ereg(pattern, string)"
replacement_function: "preg_match('/pattern/', string)"
languages: ["php"]
deprecated_since: "PHP 5.3 / removed PHP 7.0"
---

# [Solution] Deprecated Function Migration: ereg functions to preg_match

The `ereg(pattern, string)` has been deprecated in favor of `preg_match('/pattern/', string)`.

## Migration Guide

ereg was removed in PHP 7.0.

## Before (Deprecated)

```php
if (ereg('^[a-z]+$', $input)) { }
```

## After (Modern)

```php
if (preg_match('/^[a-z]+$/', $input)) { }
```

## Key Differences

- Add delimiters to regex
