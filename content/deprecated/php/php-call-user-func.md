---
title: "[Solution] Deprecated Function Migration: call_user_func to direct function calls"
description: "Migrate from deprecated call_user_func patterns to direct calls or first-class callable syntax."
deprecated_function: "call_user_func($func)"
replacement_function: "$func() or $func(...)"
languages: ["php"]
deprecated_since: "PHP 8.0+"
---

# [Solution] Deprecated Function Migration: call_user_func to direct function calls

The `call_user_func($func)` has been deprecated in favor of `$func() or $func(...)`.

## Migration Guide

call_user_func is slower than direct calls. In PHP 8.0+, use first-class callable syntax.

## Before (Deprecated)

```php
call_user_func($callback, $arg1, $arg2);
call_user_func_array($callback, [$arg1, $arg2]);
```

## After (Modern)

```php
$callback($arg1, $arg2);

// For dynamic calls
$func = $useFunc ? "strtoupper" : "strtolower";
$result = $func("hello");

// First-class callable (PHP 8.1+)
$strlen = strlen(...);
$len = $strlen("hello");
```

## Key Differences

- Direct calls are faster than call_user_func
- First-class callable syntax in PHP 8.1
- $func() is cleaner than call_user_func($func)
- Use call_user_func_array for dynamic args
