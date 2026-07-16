---
title: "[Solution] PHP E_USER_DEPRECATED — User-Triggered Deprecation Fix"
description: "Fix PHP E_USER_DEPRECATED deprecation notices triggered by user code. Learn to handle and replace user-triggered deprecation warnings in PHP."
languages: ["php"]
severities: ["notice"]
error-types: ["runtime-error"]
tags: ["e-user-deprecated", "user-deprecated", "trigger-error"]
weight: 5
---

# [Solution] PHP E_USER_DEPRECATED — User-Triggered Deprecation Fix

`E_USER_DEPRECATED` is a non-fatal deprecation notice triggered by user code using `trigger_error()`. The script continues executing, but the notice indicates that a function, method, or pattern is deprecated and should be replaced. It is commonly used in libraries and frameworks to signal API changes to users.

## Common Causes

- Calling a deprecated method in a library or framework
- Using outdated API patterns that the maintainer has flagged
- Passing deprecated configuration options
- Using a function marked for removal in a future release

## How to Fix

### 1. Update Deprecated API Calls

```php
// WRONG — using deprecated method
<?php
class Logger {
    public function log($msg) {
        trigger_error('Logger::log() is deprecated, use Logger::info()', E_USER_DEPRECATED);
        $this->info($msg);
    }

    public function info($msg) {
        error_log($msg);
    }
}

$logger = new Logger();
$logger->log('test'); // triggers E_USER_DEPRECATED
?>

// CORRECT — use the current method
<?php
$logger = new Logger();
$logger->info('test');
?>
```

### 2. Suppress Deprecation Warnings During Migration

```php
<?php
// Temporarily suppress during transition period
$old_value = @getDeprecatedConfig(); // suppresses E_USER_DEPRECATED
?>
```

### 3. Add a Custom Handler During Development

```php
<?php
function deprecation_handler($errno, $errstr, $errfile, $errline) {
    if ($errno === E_USER_DEPRECATED) {
        error_log("DEPRECATED: $errstr in $errfile on line $errline");
        return true;
    }
    return false;
}

set_error_handler('deprecation_handler');
error_reporting(E_ALL | E_USER_DEPRECATED);
?>
```

### 4. Use Version Checks in Libraries

```php
<?php
class MyLibrary {
    public function newMethod(): string {
        return 'current behavior';
    }

    /** @deprecated Use newMethod() instead */
    public function oldMethod(): string {
        trigger_error('oldMethod() is deprecated, use newMethod()', E_USER_DEPRECATED);
        return $this->newMethod();
    }
}
?>
```

## Examples

```php
<?php
// E_USER_DEPRECATED: custom deprecation from user code
function getUserName(int $id): string {
    trigger_error('getUserName() is deprecated, use User::find()', E_USER_DEPRECATED);
    return "User#$id";
}
getUserName(42);
?>
```

## Related Errors

- [PHP E_DEPRECATED]({{< relref "/languages/php/e-deprecated" >}})
- [PHP Deprecated Warning]({{< relref "/languages/php/deprecated-filter" >}})
- [PHP E_STRICT]({{< relref "/languages/php/e-strict" >}})
- [PHP E_USER_NOTICE]({{< relref "/languages/php/e-user-notice" >}})
