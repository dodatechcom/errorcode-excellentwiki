---
title: "[Solution] Deprecated Function Migration: split() to explode()"
description: "Migrate from deprecated split() to explode()."
deprecated_function: "split(',', $str)"
replacement_function: "explode(',', $str)"
languages: ["php"]
deprecated_since: "PHP 5.3 / removed PHP 7.0"
---

# [Solution] Deprecated Function Migration: split() to explode()

The `split(',', $str)` has been deprecated in favor of `explode(',', $str)`.

## Migration Guide

split was removed in PHP 7.0.

## Before (Deprecated)

```php
$arr = split(',', $str);
```

## After (Modern)

```php
$arr = explode(',', $str);
```

## Key Differences

- split was removed in PHP 7.0
