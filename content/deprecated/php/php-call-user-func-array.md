---
title: "[Solution] Deprecated Function Migration: call_user_func_array to spread operator"
description: "Migrate from deprecated call_user_func_array to spread operator."
deprecated_function: "call_user_func_array($func, $args)"
replacement_function: "$func(...$args)"
languages: ["php"]
deprecated_since: "PHP 5.6+"
---

# [Solution] Deprecated Function Migration: call_user_func_array to spread operator

The `call_user_func_array($func, $args)` has been deprecated in favor of `$func(...$args)`.

## Migration Guide

Spread operator is cleaner and faster

call_user_func_array has function call overhead.

## Before (Deprecated)

```php
$result = call_user_func_array('strtoupper', ['hello']);
```

## After (Modern)

```php
$result = strtoupper('hello');

// Dynamic call with spread
$func = 'strtoupper';
$result = $func(...['hello']);
```

## Key Differences

- Spread operator is more direct
- No function call overhead
