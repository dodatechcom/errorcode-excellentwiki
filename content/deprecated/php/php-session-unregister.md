---
title: "[Solution] Deprecated Function Migration: session_unregister to unset($_SESSION)"
description: "Migrate from deprecated session_unregister to unset."
deprecated_function: "session_unregister('var')"
replacement_function: "unset($_SESSION['var'])"
languages: ["php"]
deprecated_since: "PHP 5.3 / removed PHP 7.0"
---

# [Solution] Deprecated Function Migration: session_unregister to unset($_SESSION)

The `session_unregister('var')` has been deprecated in favor of `unset($_SESSION['var'])`.

## Migration Guide

session_unregister was removed

session_unregister was removed in PHP 7.0.

## Before (Deprecated)

```php
session_unregister('username');
```

## After (Modern)

```php
unset($_SESSION['username']);
```

## Key Differences

- session_unregister was removed
- unset removes session variables
