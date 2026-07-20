---
title: "[Solution] PHP trigger_error() — User Error Triggering"
description: "Fix PHP trigger_error() issues by using E_USER_ERROR/WARNING/NOTICE, combining with error handler, throwing exceptions instead. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 104
---

# PHP trigger_error() — User Error Triggering

The `trigger_error()` function (alias `user_error()`) generates a user-level error at runtime. It is used to signal custom error conditions within application code. Issues include using the wrong error level, not combining it with an error handler, or using it when exceptions would be more appropriate.

## Common Causes

```php
// Cause 1: Using E_USER_ERROR in production code
trigger_error("Critical failure", E_USER_ERROR);
// E_USER_ERROR terminates script execution

// Cause 2: Not specifying an error level
trigger_error("Something went wrong");
// Defaults to E_USER_NOTICE

// Cause 3: Using trigger_error() when exceptions are more appropriate
function divide($a, $b) {
    if ($b == 0) {
        trigger_error("Division by zero", E_USER_WARNING);
    }
    return $a / $b;
}
// Exceptions are easier to catch and handle

// Cause 4: Not combining with set_error_handler()
trigger_error("Test error", E_USER_NOTICE);
// No handler to process it
```

## How to Fix

### Fix 1: Use E_USER_WARNING or E_USER_NOTICE

```php
// Use non-fatal error levels for recoverable conditions
function validateAge($age) {
    if ($age < 0) {
        trigger_error("Age cannot be negative", E_USER_WARNING);
    }
    if ($age > 150) {
        trigger_error("Age seems unrealistic", E_USER_NOTICE);
    }
    return $age;
}
```

### Fix 2: Combine with set_error_handler()

```php
set_error_handler(function ($errno, $errstr, $errfile, $errline) {
    error_log("User Error: $errstr in $errfile on line $errline");
    return true;
});

trigger_error("Custom validation failed", E_USER_WARNING);
```

### Fix 3: Throw Exceptions Instead

```php
// Instead of trigger_error(), use exceptions for better control
function processOrder($order) {
    if (empty($order)) {
        throw new \InvalidArgumentException("Order cannot be empty");
    }

    if ($order['total'] < 0) {
        throw new \RuntimeException("Order total cannot be negative");
    }

    return true;
}

try {
    processOrder(['total' => -10]);
} catch (\Exception $e) {
    error_log($e->getMessage());
}
```

### Fix 4: Use with Custom Error Handler for Logging

```php
set_error_handler(function ($errno, $errstr, $errfile, $errline) {
    $errorData = [
        'level'   => $errno,
        'message' => $errstr,
        'file'    => $errfile,
        'line'    => $errline,
        'time'    => date('Y-m-d H:i:s'),
    ];
    error_log(json_encode($errorData));
    return true;
});

trigger_error("Deprecated function called", E_USER_DEPRECATED);
```

## Examples

```php
// Example: Validate input and trigger errors
function setUserName($name) {
    if (strlen($name) < 3) {
        trigger_error("Name must be at least 3 characters", E_USER_WARNING);
        return false;
    }
    if (strlen($name) > 50) {
        trigger_error("Name must be at most 50 characters", E_USER_WARNING);
        return false;
    }
    return true;
}

// Example: Error levels and their behavior
trigger_error("Notice-level error", E_USER_NOTICE);    // Continues execution
trigger_error("Warning-level error", E_USER_WARNING);  // Continues execution
trigger_error("Deprecated usage", E_USER_DEPRECATED);  // Continues execution
// trigger_error("Fatal error", E_USER_ERROR);         // Terminates execution
```

## Related Errors

- [set_error_handler()](/languages/php/set-error-handler)
- [E_User_Error](/languages/php/e-user-error)
- [E_User_Warning](/languages/php/e-user-warning)
- [E_User_Notice](/languages/php/e-user-notice)
