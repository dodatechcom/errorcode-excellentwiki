---
title: "[Solution] Deprecated Function Migration: set_magic_quotes_runtime to ini_set"
description: "Migrate from deprecated set_magic_quotes_runtime to ini_set."
deprecated_function: "set_magic_quotes_runtime(0)"
replacement_function: "ini_set('magic_quotes_runtime', 0)"
languages: ["php"]
deprecated_since: "PHP 5.3 / removed PHP 5.4"
---

# [Solution] Deprecated Function Migration: set_magic_quotes_runtime to ini_set

The `set_magic_quotes_runtime(0)` has been deprecated in favor of `ini_set('magic_quotes_runtime', 0)`.

## Migration Guide

Magic quotes were removed.

## Before (Deprecated)

```php
set_magic_quotes_runtime(0);
```

## After (Modern)

```php
ini_set('magic_quotes_runtime', 0);
```

## Key Differences

- ini_set is the standard
