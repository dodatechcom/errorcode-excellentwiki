---
title: "[Solution] Deprecated Function Migration: is_null($var) to $var === null"
description: "Migrate from deprecated is_null() to direct comparison."
deprecated_function: "is_null($var)"
replacement_function: "$var === null"
languages: ["php"]
deprecated_since: "Best Practice"
---

# [Solution] Deprecated Function Migration: is_null($var) to $var === null

The `is_null($var)` has been deprecated in favor of `$var === null`.

## Migration Guide

Direct comparison is faster.

## Before (Deprecated)

```php
if (is_null($var)) { }
```

## After (Modern)

```php
if ($var === null) { }
```

## Key Differences

- Direct comparison is faster
