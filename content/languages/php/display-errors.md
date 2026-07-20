---
title: "[Solution] PHP display_errors — INI Setting Configuration"
description: "Fix PHP display_errors issues by setting to 1 for development, 0 for production, using error_log instead, and configuring per-environment. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 101
---

# PHP display_errors — INI Setting Configuration

The `display_errors` INI directive controls whether PHP errors are output to the screen. Leaving this enabled in production exposes sensitive information to users, while disabling it in development makes debugging difficult. Misconfiguring this setting is one of the most common PHP security and development issues.

## Common Causes

```php
// Cause 1: display_errors left enabled in production
// php.ini: display_errors = On

// Cause 2: display_errors disabled during development
// php.ini: display_errors = Off

// Cause 3: Not using error_log as a fallback
// (no logging configured when display_errors is Off)

// Cause 4: Trying to change display_errors after output has started
echo "Output started";
ini_set('display_errors', '1'); // Warning: headers already sent
```

## How to Fix

### Fix 1: Set display_errors to 1 for Development

```php
// Enable error display during development
ini_set('display_errors', '1');
ini_set('display_startup_errors', '1');
```

### Fix 2: Set display_errors to 0 for Production

```php
// Disable error display in production
ini_set('display_errors', '0');
ini_set('display_startup_errors', '0');
```

### Fix 3: Use error_log Instead of Displaying Errors

```php
// Log errors to a file instead of displaying them
ini_set('display_errors', '0');
ini_set('log_errors', '1');
ini_set('error_log', '/var/log/php_errors.log');
```

### Fix 4: Configure Per-Environment

```php
$env = getenv('APP_ENV') ?: 'production';

if ($env === 'development') {
    ini_set('display_errors', '1');
    ini_set('log_errors', '1');
} else {
    ini_set('display_errors', '0');
    ini_set('log_errors', '1');
    ini_set('error_log', '/var/log/php_errors.log');
}
```

## Examples

```php
// Example: Set before any output
ini_set('display_errors', '1');
error_reporting(E_ALL);

// Example: Verify current setting
echo ini_get('display_errors'); // "1" or "0"

// Example: Use .htaccess for Apache
// php_value display_errors 0
// php_value log_errors 1
// php_value error_log /var/log/php_errors.log
```

## Related Errors

- [error_reporting()](/languages/php/error-reporting-function)
- [error_log()](/languages/php/error-log-function)
- [warning-headers-sent-already](/languages/php/warning-headers-sent-already)
