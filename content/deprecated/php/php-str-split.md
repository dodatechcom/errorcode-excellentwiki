---
title: "[Solution] Deprecated Function Migration: split to str_split"
description: "Migrate from deprecated split to str_split."
deprecated_function: "split('', $str)"
replacement_function: "str_split($str)"
languages: ["php"]
deprecated_since: "PHP 5.0+ / split removed 7.0"
---

# [Solution] Deprecated Function Migration: split to str_split

The `split('', $str)` has been deprecated in favor of `str_split($str)`.

## Migration Guide

str_split is the standard.

## Before (Deprecated)

```php
$arr = split('', $str);
```

## After (Modern)

```php
$arr = str_split($str);
```

## Key Differences

- str_split is the standard
