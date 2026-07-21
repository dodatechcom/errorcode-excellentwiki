---
title: "[Solution] Deprecated Function Migration: session_set_cookie_params to session configuration"
description: "Migrate from deprecated session_set_cookie_params to modern session configuration."
deprecated_function: "session_set_cookie_params(...)"
replacement_function: "ini_set('session.cookie_*')"
languages: ["php"]
deprecated_since: "PHP 7.0+"
---

# [Solution] Deprecated Function Migration: session_set_cookie_params to session configuration

The `session_set_cookie_params(...)` has been deprecated in favor of `ini_set('session.cookie_*')`.

## Migration Guide

ini_set provides more granular control

session_set_cookie_params sets multiple parameters at once. ini_set provides more control.

## Before (Deprecated)

```php
session_set_cookie_params(
    3600,
    "/",
    ".example.com",
    true,
    true
);
```

## After (Modern)

```php
ini_set('session.cookie_lifetime', 3600);
ini_set('session.cookie_path', '/');
ini_set('session.cookie_domain', '.example.com');
ini_set('session.cookie_secure', true);
ini_set('session.cookie_httponly', true);

// Or use session_start with options
session_start([
    'cookie_lifetime' => 3600,
    'cookie_secure' => true,
]);
```

## Key Differences

- ini_set for individual parameters
- session_start with options array
- More granular control
- Better for different environments
