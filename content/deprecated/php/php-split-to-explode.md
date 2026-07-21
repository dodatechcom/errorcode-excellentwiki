---
title: "[Solution] Deprecated Function Migration: split() to explode() or preg_split()"
description: "Migrate from deprecated split() to explode() or preg_split() in PHP."
deprecated_function: "split()"
replacement_function: "explode() / preg_split()"
languages: ["php"]
deprecated_since: "PHP 5.3 / removed PHP 7.0"
---

# [Solution] Deprecated Function Migration: split() to explode() or preg_split()

The `split()` has been deprecated in favor of `explode() / preg_split()`.

## Migration Guide

split() was removed in PHP 7.0. Use explode() for simple splitting, preg_split() for regex-based.

## Before (Deprecated)

```php
$parts = split(",", $csv);
$words = split("\\s+", $text);
```

## After (Modern)

```php
$parts = explode(",", $csv);
$words = preg_split("/\\s+/", $text);
$parts = explode(",", $csv, 3);
```

## Key Differences

- explode() for simple delimiter splitting
- preg_split() for regex-based splitting
- explode is faster than preg_split
