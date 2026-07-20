---
title: "[Solution] PHP set_error_handler() — Custom Error Handler Usage"
description: "Fix PHP set_error_handler() issues by handling all error levels, returning bool, using set_exception_handler(), and understanding limitations. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 102
---

# PHP set_error_handler() — Custom Error Handler Usage

The `set_error_handler()` function lets you define a custom function to handle PHP errors. It is commonly used for centralized error logging, custom error pages, or transforming errors into exceptions. Issues arise when the handler returns the wrong type, fails to handle all error levels, or does not account for fatal errors that cannot be caught.

## Common Causes

```php
// Cause 1: Handler not returning a boolean
set_error_handler(function ($errno, $errstr) {
    echo "Error: $errstr";
    // Missing return value
});

// Cause 2: Not handling all error levels
set_error_handler(function ($errno, $errstr) {
    if ($errno === E_WARNING) {
        return true;
    }
    // E_NOTICE, E_ERROR, etc. not handled
});

// Cause 3: Trying to handle fatal errors
set_error_handler(function ($errno, $errstr) {
    // Fatal errors (E_ERROR, E_PARSE) cannot be caught
    return false;
});

// Cause 4: Not preserving previous error handler
set_error_handler(function ($errno, $errstr) {
    return true;
});
// Previous handler is lost
```

## How to Fix

### Fix 1: Return a Boolean from the Handler

```php
set_error_handler(function ($errno, $errstr, $errfile, $errline) {
    echo "Error [$errno]: $errstr in $errfile on line $errline";
    return true; // Prevent PHP's built-in error handler
});
```

### Fix 2: Handle All Error Levels

```php
set_error_handler(function ($errno, $errstr, $errfile, $errline) {
    $errorLevels = [
        E_WARNING      => 'Warning',
        E_NOTICE       => 'Notice',
        E_USER_ERROR   => 'User Error',
        E_USER_WARNING => 'User Warning',
        E_USER_NOTICE  => 'User Notice',
        E_DEPRECATED   => 'Deprecated',
    ];

    $level = $errorLevels[$errno] ?? "Unknown Error ($errno)";
    error_log("$level: $errstr in $errfile on line $errline");
    return true;
});
```

### Fix 3: Use set_exception_handler() for Uncaught Exceptions

```php
set_error_handler(function ($errno, $errstr, $errfile, $errline) {
    throw new ErrorException($errstr, 0, $errno, $errfile, $errline);
});

set_exception_handler(function (Throwable $e) {
    error_log($e->getMessage());
    http_response_code(500);
    echo "Internal Server Error";
});
```

### Fix 4: Restore After Use

```php
$previousHandler = set_error_handler(function ($errno, $errstr) {
    return true;
});

// ... custom handling ...

restore_error_handler();
// Previous handler is restored
```

## Examples

```php
// Example: Convert errors to exceptions
set_error_handler(function ($errno, $errstr, $errfile, $errline) {
    if (error_reporting() & $errno) {
        throw new ErrorException($errstr, 0, $errno, $errfile, $errline);
    }
    return false;
});

// Example: Log with context
set_error_handler(function ($errno, $errstr, $errfile, $errline) {
    $context = [
        'error' => $errstr,
        'file'  => $errfile,
        'line'  => $errline,
    ];
    error_log(json_encode($context));
    return true;
});
```

## Related Errors

- [restore_error_handler()](/languages/php/restore-error-handler)
- [set_exception_handler()](/languages/php/set-exception-handler)
- [ErrorException](/languages/php/errorexception)
- [trigger_error()](/languages/php/trigger-error)
