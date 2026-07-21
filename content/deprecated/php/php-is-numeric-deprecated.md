---
title: "[Solution] Deprecated Function Migration: is_numeric to filter_var"
description: "Migrate from deprecated is_numeric for validation to filter_var."
deprecated_function: "is_numeric($val)"
replacement_function: "filter_var($val, FILTER_VALIDATE_INT)"
languages: ["php"]
deprecated_since: "Best Practice"
---

# [Solution] Deprecated Function Migration: is_numeric to filter_var

The `is_numeric($val)` has been deprecated in favor of `filter_var($val, FILTER_VALIDATE_INT)`.

## Migration Guide

filter_var provides more control.

## Before (Deprecated)

```php
if (is_numeric($val)) { }
```

## After (Modern)

```php
if (filter_var($val, FILTER_VALIDATE_INT) !== false) { }
```

## Key Differences

- filter_var provides more control
