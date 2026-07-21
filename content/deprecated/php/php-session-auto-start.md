---
title: "[Solution] Deprecated Function Migration: session.auto_start to manual session_start"
description: "Migrate from deprecated session.auto_start to explicit session_start."
deprecated_function: "session.auto_start = 1"
replacement_function: "session_start()"
languages: ["php"]
deprecated_since: "PHP 5.4+"
---

# [Solution] Deprecated Function Migration: session.auto_start to manual session_start

The `session.auto_start = 1` has been deprecated in favor of `session_start()`.

## Migration Guide

Manual start provides more control

session.auto_start starts session on every request. Manual start provides control.

## Before (Deprecated)

```php
; php.ini
session.auto_start = 1
```

## After (Modern)

```php
session_start();  // explicit start

// Or use session_start with options
session_start([
    'cookie_lifetime' => 86400,
    'cookie_secure' => true,
]);
```

## Key Differences

- Manual start provides control
- Can set options per request
- Better for different environments
- auto_start is global setting
