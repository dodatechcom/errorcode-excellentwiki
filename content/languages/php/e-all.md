---
title: "[Solution] PHP E_ALL — Enable All Error Reporting"
description: "Configure PHP E_ALL to report all errors, warnings, notices, and deprecation notices. Learn to use E_ALL for comprehensive error reporting in development."
languages: ["php"]
severities: ["warning"]
error-types: ["runtime-error"]
weight: 5
---

# [Solution] PHP E_ALL — Enable All Error Reporting

`E_ALL` is a PHP constant that represents all possible error, warning, and notice levels. Using `E_ALL` in `error_reporting()` ensures every type of PHP issue is reported, including notices, warnings, deprecation notices, and strict standards. It is the recommended setting for development environments.

## Common Causes

- Missing `error_reporting = E_ALL` in `php.ini` for development
- Production environments hiding errors that developers need to see
- Misconfigured `display_errors` masking important notices
- Not combining `E_ALL` with other flags for full coverage

## How to Fix

### 1. Set `E_ALL` in PHP Code

```php
<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
?>
```

### 2. Set `E_ALL` in `php.ini`

```ini
; Development php.ini
error_reporting = E_ALL
display_errors = On
display_startup_errors = On
log_errors = On
```

### 3. Combine with Additional Flags

```php
<?php
// Include deprecation notices and strict standards
error_reporting(E_ALL | E_DEPRECATED | E_STRICT);
?>
```

### 4. Use `E_ALL` with Bitwise Operators for Exclusions

```php
<?php
// Report everything except notices (not recommended)
error_reporting(E_ALL & ~E_NOTICE);

// Report everything except deprecated (for legacy code migration)
error_reporting(E_ALL & ~E_DEPRECATED);
?>
```

### 5. Production vs Development Settings

```php
<?php
// Development
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Production
error_reporting(E_ALL & ~E_DEPRECATED & ~E_NOTICE);
ini_set('display_errors', 0);
ini_set('log_errors', 1);
ini_set('error_log', '/var/log/php_errors.log');
?>
```

## Examples

```php
<?php
// These E_ALL flag values are combined via bitwise OR
// E_ERROR       = 1
// E_WARNING     = 2
// E_PARSE       = 4
// E_NOTICE      = 8
// E_STRICT      = 2048
// E_DEPRECATED  = 8192
// E_USER_ERROR  = 256
// E_USER_WARNING = 512
// E_USER_NOTICE = 1024
// E_USER_DEPRECATED = 16384
// E_ALL         = 32767 (all of the above combined)

echo E_ALL; // 32767
?>
```

## Related Errors

- [PHP E_ERROR]({{< relref "/languages/php/e-error" >}})
- [PHP E_WARNING]({{< relref "/languages/php/e-warning" >}})
- [PHP E_NOTICE]({{< relref "/languages/php/e-notice" >}})
- [PHP E_DEPRECATED]({{< relref "/languages/php/e-deprecated" >}})
