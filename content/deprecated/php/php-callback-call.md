---
title: "[Solution] Deprecated Function Migration: call_user_func to direct function call"
description: "Migrate from deprecated call_user_func to direct function call."
deprecated_function: "call_user_func($func, $arg)"
replacement_function: "$func($arg)"
languages: ["php"]
deprecated_since: "Best Practice"
---

# [Solution] Deprecated Function Migration: call_user_func to direct function call

The `call_user_func($func, $arg)` has been deprecated in favor of `$func($arg)`.

## Migration Guide

Direct calls are faster.

## Before (Deprecated)

```php
$result = call_user_func($callback, $arg1, $arg2);
```

## After (Modern)

```php
$result = $callback($arg1, $arg2);
```

## Key Differences

- Direct calls are faster
