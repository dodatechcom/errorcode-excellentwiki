---
title: "[Solution] Deprecated Function Migration: key_exists to array_key_exists"
description: "Migrate from deprecated key_exists to array_key_exists."
deprecated_function: "key_exists($key, $arr)"
replacement_function: "array_key_exists($key, $arr)"
languages: ["php"]
deprecated_since: "PHP 4.0+"
---

# [Solution] Deprecated Function Migration: key_exists to array_key_exists

The `key_exists($key, $arr)` has been deprecated in favor of `array_key_exists($key, $arr)`.

## Migration Guide

array_key_exists is the standard.

## Before (Deprecated)

```php
if (key_exists($key, $arr)) { }
```

## After (Modern)

```php
if (array_key_exists($key, $arr)) { }
```

## Key Differences

- array_key_exists is the standard
