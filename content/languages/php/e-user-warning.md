---
title: "[Solution] PHP E_USER_WARNING — User-Triggered Warning Fix"
description: "Fix PHP E_USER_WARNING non-fatal warnings triggered by user code via trigger_error(). Learn to handle and resolve user-triggered warnings."
languages: ["php"]
severities: ["warning"]
error-types: ["runtime-error"]
weight: 5
---

# [Solution] PHP E_USER_WARNING — User-Triggered Warning Fix

`E_USER_WARNING` is a non-fatal warning triggered by user code using `trigger_error()`. The script continues executing after the warning. It is useful for flagging non-critical problems in your own code that developers should address.

## Common Causes

- Flagging non-critical validation issues in custom functions
- Using `trigger_error()` to report recoverable problems
- Legacy code using `trigger_error` instead of exceptions or logging
- Reporting deprecated usage patterns in helper libraries

## How to Fix

### 1. Use Exceptions or Logging Instead

```php
// WRONG — using trigger_error for warnings
<?php
function setDiscount(float $rate) {
    if ($rate > 1.0) {
        trigger_error('Discount rate exceeds 100%', E_USER_WARNING);
    }
    return $rate;
}
?>

// CORRECT — use exceptions or return error state
<?php
function setDiscount(float $rate): float {
    if ($rate > 1.0) {
        throw new RangeException('Discount rate exceeds 100%: ' . $rate);
    }
    return $rate;
}
?>
```

### 2. Implement a Custom Warning Handler

```php
<?php
function user_warning_handler($errno, $errstr, $errfile, $errline) {
    if ($errno === E_USER_WARNING) {
        error_log("E_USER_WARNING: $errstr in $errfile on line $errline");
        return true;
    }
    return false;
}

set_error_handler('user_warning_handler');
?>
```

### 3. Use Modern Error Handling Patterns

```php
<?php
class Result {
    public bool $success;
    public string $message;

    public static function ok(string $msg = ''): self {
        return new self(true, $msg);
    }

    public static function fail(string $msg): self {
        return new self(false, $msg);
    }
}

function processData(array $data): Result {
    if (empty($data)) {
        return Result::fail('No data provided');
    }
    return Result::ok('Processed successfully');
}
?>
```

## Examples

```php
<?php
// E_USER_WARNING: custom warning from user code
function connect(string $host) {
    if (filter_var(gethostbyname($host), FILTER_VALIDATE_IP) === false) {
        trigger_error("Host $host could not be resolved", E_USER_WARNING);
    }
    // continue connection attempt
}
connect('invalid-hostname.test');
?>
```

## Related Errors

- [PHP E_USER_ERROR]({{< relref "/languages/php/e-user-error" >}})
- [PHP E_USER_NOTICE]({{< relref "/languages/php/e-user-notice" >}})
- [PHP E_WARNING]({{< relref "/languages/php/e-warning" >}})
- [PHP E_USER_DEPRECATED]({{< relref "/languages/php/e-user-deprecated" >}})
