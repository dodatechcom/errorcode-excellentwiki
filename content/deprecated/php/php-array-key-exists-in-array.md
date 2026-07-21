---
title: "[Solution] Deprecated Function Migration: array_key_exists to isset for value checking"
description: "Migrate from deprecated array_key_exists for value checking to isset in PHP."
deprecated_function: "array_key_exists($key, $arr)"
replacement_function: "isset($arr[$key])"
languages: ["php"]
deprecated_since: "PHP 7.0+"
---

# [Solution] Deprecated Function Migration: array_key_exists to isset for value checking

The `array_key_exists($key, $arr)` has been deprecated in favor of `isset($arr[$key])`.

## Migration Guide

isset is faster and checks for null values too

array_key_exists is slower than isset. isset also checks if the value is null.

## Before (Deprecated)

```php
$arr = ["name" => "Alice", "age" => null];
if (array_key_exists("age", $arr)) {
    echo "Key exists";
}
```

## After (Modern)

```php
$arr = ["name" => "Alice", "age" => null];
if (isset($arr["age"])) {
    echo "Key exists and is not null";
}

// array_key_exists still works for null values
if (array_key_exists("age", $arr)) {
    echo "Key exists (even if null)";
}
```

## Key Differences

- isset is faster than array_key_exists
- isset returns false for null values
- Use array_key_exists when null is a valid value
- array_key_exists cannot be used with objects
