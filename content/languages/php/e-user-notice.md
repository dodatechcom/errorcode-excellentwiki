---
title: "[Solution] PHP E_USER_NOTICE — User-Triggered Notice Fix"
description: "Fix PHP E_USER_NOTICE non-fatal notices triggered by user code via trigger_error(). Learn to handle user-triggered notices in PHP."
languages: ["php"]
severities: ["notice"]
error-types: ["runtime-error"]
weight: 5
---

# [Solution] PHP E_USER_NOTICE — User-Triggered Notice Fix

`E_USER_NOTICE` is a non-fatal notice triggered by user code using `trigger_error()`. The script continues executing. It is the least severe of the user-triggered error levels and is useful for flagging minor informational issues in your own code.

## Common Causes

- Informational notices from custom validation logic
- Reporting optional but missing configuration values
- Flagging minor code-quality issues in helper libraries
- Legacy debugging patterns using `trigger_error`

## How to Fix

### 1. Use Proper Logging Instead

```php
// WRONG — using trigger_error for informational messages
<?php
function getConfig(string $key, string $default = '') {
    if (!isset($GLOBALS['config'][$key])) {
        trigger_error("Config key '$key' not set, using default", E_USER_NOTICE);
    }
    return $GLOBALS['config'][$key] ?? $default;
}
?>

// CORRECT — use error_log or a logger
<?php
function getConfig(string $key, string $default = '') {
    if (!isset($GLOBALS['config'][$key])) {
        error_log("Config key '$key' not set, using default");
    }
    return $GLOBALS['config'][$key] ?? $default;
}
?>
```

### 2. Implement a Custom Notice Handler

```php
<?php
function user_notice_handler($errno, $errstr, $errfile, $errline) {
    if ($errno === E_USER_NOTICE) {
        error_log("E_USER_NOTICE: $errstr in $errfile on line $errline");
        return true;
    }
    return false;
}

set_error_handler('user_notice_handler');
?>
```

### 3. Return Status Objects Instead of Notices

```php
<?php
class ProcessingResult {
    public function __construct(
        public bool $ok,
        public string $message = '',
        public array $data = []
    ) {}
}

function validate(array $input): ProcessingResult {
    if (empty($input['email'])) {
        return new ProcessingResult(false, 'Email is required');
    }
    return new ProcessingResult(true, '', $input);
}
?>
```

## Examples

```php
<?php
// E_USER_NOTICE: informational message from user code
function processItem($item) {
    if ($item === null) {
        trigger_error('Item was null, skipping', E_USER_NOTICE);
        return null;
    }
    return strtoupper($item);
}
processItem(null);
?>
```

## Related Errors

- [PHP E_USER_WARNING]({{< relref "/languages/php/e-user-warning" >}})
- [PHP E_USER_ERROR]({{< relref "/languages/php/e-user-error" >}})
- [PHP E_NOTICE]({{< relref "/languages/php/e-notice" >}})
- [PHP E_USER_DEPRECATED]({{< relref "/languages/php/e-user-deprecated" >}})
