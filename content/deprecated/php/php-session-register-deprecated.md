---
title: "[Solution] Deprecated Function Migration: session_register to $_SESSION"
description: "Migrate from deprecated session_register to $_SESSION."
deprecated_function: "session_register('var')"
replacement_function: "$_SESSION['var']"
languages: ["php"]
deprecated_since: "PHP 5.3 / removed PHP 5.4"
---

# [Solution] Deprecated Function Migration: session_register to $_SESSION

The `session_register('var')` has been deprecated in favor of `$_SESSION['var']`.

## Migration Guide

session_register was removed.

## Before (Deprecated)

```php
session_register('username');
$username = 'Alice';
```

## After (Modern)

```php
$_SESSION['username'] = 'Alice';
```

## Key Differences

- $_SESSION is the standard
