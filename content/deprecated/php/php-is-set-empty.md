---
title: "[Solution] Deprecated Function Migration: empty() to explicit checks"
description: "Migrate from deprecated empty() to explicit type checks."
deprecated_function: "empty($var)"
replacement_function: "$var === '' || $var === null"
languages: ["php"]
deprecated_since: "Best Practice"
---

# [Solution] Deprecated Function Migration: empty() to explicit checks

The `empty($var)` has been deprecated in favor of `$var === '' || $var === null`.

## Migration Guide

empty() has surprising behavior with 0 and '0'

empty() treats 0, '', null, false as empty.

## Before (Deprecated)

```php
$val = 0;
if (empty($val)) { /* true! */ }
```

## After (Modern)

```php
$val = 0;
if ($val === null || $val === '') {
    // only truly empty
}
```

## Key Differences

- empty() has surprising behavior
- 0, '0', false are treated as empty
- Use explicit checks for clarity
