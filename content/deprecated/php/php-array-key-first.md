---
title: "[Solution] Deprecated Function Migration: reset($arr) to array_key_first($arr)"
description: "Migrate from deprecated reset() for first key to array_key_first()."
deprecated_function: "reset($arr)"
replacement_function: "array_key_first($arr)"
languages: ["php"]
deprecated_since: "PHP 7.3+"
---

# [Solution] Deprecated Function Migration: reset($arr) to array_key_first($arr)

The `reset($arr)` has been deprecated in favor of `array_key_first($arr)`.

## Migration Guide

array_key_first is more explicit.

## Before (Deprecated)

```php
reset($arr);
```

## After (Modern)

```php
array_key_first($arr);
```

## Key Differences

- array_key_first is explicit
