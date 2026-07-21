---
title: "[Solution] Deprecated Function Migration: string offsets to array functions"
description: "Migrate from deprecated string offset access to array functions."
deprecated_function: "str[0]"
replacement_function: "str_split($str)[0]"
languages: ["php"]
deprecated_since: "PHP 5.4+"
---

# [Solution] Deprecated Function Migration: string offsets to array functions

The `str[0]` has been deprecated in favor of `str_split($str)[0]`.

## Migration Guide

Array functions provide consistent behavior

String offset access works but is less consistent.

## Before (Deprecated)

```php
$str = "hello";
$first = $str[0];
```

## After (Modern)

```php
$chars = str_split("hello");
$first = $chars[0];

// For multibyte
$first = mb_substr($str, 0, 1, 'UTF-8');
```

## Key Differences

- str_split for converting to array
- mb_ functions for multibyte support
