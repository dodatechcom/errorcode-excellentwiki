---
title: "[Solution] Deprecated Function Migration: eregi/spliti to preg_match with i modifier"
description: "Migrate from deprecated POSIX regex functions to PCRE in PHP."
deprecated_function: "eregi() / spliti()"
replacement_function: "preg_match('/pattern/i')"
languages: ["php"]
deprecated_since: "PHP 5.3 / removed PHP 7.0"
---

# [Solution] Deprecated Function Migration: eregi/spliti to preg_match with i modifier

The `eregi() / spliti()` has been deprecated in favor of `preg_match('/pattern/i')`.

## Migration Guide

POSIX regex functions were removed in PHP 7.0. Use PCRE with the i modifier for case-insensitive matching.

## Before (Deprecated)

```php
if (eregi("^(test)$", $input)) {
    echo "Match";
}
$parts = spliti(",", $input);
```

## After (Modern)

```php
if (preg_match("/^(test)$/i", $input)) {
    echo "Match";
}
$parts = preg_split("/,/i", $input);
```

## Key Differences

- Use /pattern/i for case-insensitive matching
- PCRE is more powerful than POSIX
- preg_match returns 1 (match), 0 (no match)
