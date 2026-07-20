---
title: "[Solution] PHP error_reporting() — Function Configuration"
description: "Fix PHP error_reporting() issues by using E_ALL, setting in php.ini, using ini_set(), and understanding error levels. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 100
---

# PHP error_reporting() — Function Configuration

The `error_reporting()` function in PHP controls which errors are reported by the engine. Misconfiguring this function can hide critical errors during development or expose sensitive information in production. Common issues include not reporting all errors, setting the wrong level, or failing to override the php.ini setting.

## Common Causes

```php
// Cause 1: Not reporting all errors during development
error_reporting(0);

// Cause 2: Using a single error level instead of bitwise OR
error_reporting(E_ERROR);

// Cause 3: Relying on php.ini without runtime override
// (no code — error_reporting remains at the php.ini default)

// Cause 4: Suppressing errors instead of configuring proper reporting
error_reporting(E_ERROR | E_WARNING);

// Cause 5: Not checking the current error reporting level
$currentLevel = error_reporting();
```

## How to Fix

### Fix 1: Use E_ALL for Full Development Reporting

```php
// Report all errors during development
error_reporting(E_ALL);

// Include deprecated notices as well (PHP 8.x)
error_reporting(E_ALL | E_DEPRECATED);
```

### Fix 2: Set in php.ini

```ini
; php.ini
error_reporting = E_ALL
display_errors = On
log_errors = On
```

### Fix 3: Use ini_set() for Runtime Configuration

```php
// Override php.ini at runtime
ini_set('error_reporting', E_ALL);
ini_set('display_errors', '1');
ini_set('log_errors', '1');
```

### Fix 4: Configure Per-Environment

```php
// Detect environment and set appropriate level
$env = getenv('APP_ENV') ?: 'production';

if ($env === 'development') {
    error_reporting(E_ALL);
    ini_set('display_errors', '1');
} else {
    error_reporting(E_ALL & ~E_DEPRECATED & ~E_NOTICE);
    ini_set('display_errors', '0');
    ini_set('log_errors', '1');
}
```

## Examples

```php
// Example: Check current error reporting level
$currentLevel = error_reporting();
echo sprintf('Current error reporting level: %d', $currentLevel);

// Example: Temporarily suppress specific error levels
$previousLevel = error_reporting(E_ERROR);
// ... code that triggers warnings ...
error_reporting($previousLevel);

// Example: Verify E_ALL includes expected levels
echo (E_ALL & E_WARNING) ? 'E_WARNING is included' : 'E_WARNING is not included';
```

## Related Errors

- [E_ALL](/languages/php/e-all)
- [E_Error](/languages/php/e-error)
- [E_Warning](/languages/php/e-warning)
- [E_Notice](/languages/php/e-notice)
- [display_errors](/languages/php/display-errors)
