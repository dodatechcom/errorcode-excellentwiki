---
title: "[Solution] Deprecated Function Migration: ereg to preg_match"
description: "Migrate from deprecated ereg functions to preg_match and preg_replace in PHP."
deprecated_function: "ereg() / ereg_replace()"
replacement_function: "preg_match() / preg_replace()"
languages: ["php"]
deprecated_since: "PHP 5.3 / removed PHP 7.0"
---

# [Solution] Deprecated Function Migration: ereg to preg_match

The `ereg() / ereg_replace()` has been deprecated in favor of `preg_match() / preg_replace()`.

## Migration Guide

ereg functions used POSIX regex and were removed in PHP 7.0. preg_match uses PCRE which is more powerful.

## Before (Deprecated)

```php
if (ereg("^[a-z]+$", $input)) {
    echo "Lowercase only";
}
$output = ereg_replace("old", "new", $input);
```

## After (Modern)

```php
if (preg_match("/^[a-z]+$/", $input)) {
    echo "Lowercase only";
}
$output = preg_replace("/old/", "new", $input);
```

## Key Differences

- Add delimiters to regex patterns (/pattern/)
- PCRE supports more features than POSIX
- preg_match returns 1 for match, 0 for no match
