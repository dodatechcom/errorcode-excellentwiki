---
title: "[Solution] PHP ErrorException — Error Handler Exception"
description: "Fix PHP ErrorException by using set_error_handler(), try-catch blocks, and checking error severity levels."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 51
---

# ErrorException — Error Handler Exception

ErrorException is thrown when PHP's error handler is triggered and converts a standard PHP error into an exception. This typically occurs when `set_error_handler()` is configured to throw exceptions, or when error reporting settings cause warnings to become fatal.

## Common Causes

```php
<?php
// Cause 1: set_error_handler converting errors to exceptions
set_error_handler(function ($severity, $message, $file, $line) {
    throw new ErrorException($message, 0, $severity, $file, $line);
});

// Cause 2: Unhandled warning triggering exception
$array = [];
echo $array['missing_key']; // E_WARNING -> ErrorException

// Cause 3: Strict type coercion failure
set_error_handler(function ($err, $msg) {
    throw new ErrorException($msg);
});
"strconv: " . (int)"not_a_number"; // May trigger ErrorException

// Cause 4: Custom error handler with severity filter
set_error_handler(function ($errno, $errstr, $errfile, $errline) {
    if (!(error_reporting() & $errno)) {
        return false;
    }
    throw new ErrorException($errstr, 0, $errno, $errfile, $errline);
}, E_ALL);
?>
```

## How to Fix

### Fix 1: Use try-catch to handle ErrorException

```php
<?php
set_error_handler(function ($severity, $message, $file, $line) {
    throw new ErrorException($message, 0, $severity, $file, $line);
});

try {
    $result = someOperation();
} catch (ErrorException $e) {
    error_log('Error: ' . $e->getMessage());
    echo 'An error occurred: ' . $e->getMessage();
}
?>
```

### Fix 2: Check error severity before throwing

```php
<?php
set_error_handler(function ($severity, $message, $file, $line) {
    if ($severity === E_NOTICE || $severity === E_USER_NOTICE) {
        return false; // Let PHP handle notices normally
    }
    if ($severity === E_WARNING || $severity === E_USER_WARNING) {
        error_log("Warning: $message in $file on line $line");
        return true; // Suppress warnings
    }
    throw new ErrorException($message, 0, $severity, $file, $line);
});
?>
```

### Fix 3: Validate data before operations

```php
<?php
set_error_handler(function ($severity, $message, $file, $line) {
    throw new ErrorException($message, 0, $severity, $file, $line);
});

try {
    $data = $_GET['key'] ?? null;
    if ($data === null) {
        throw new InvalidArgumentException('Missing required parameter');
    }
    $result = process($data);
} catch (ErrorException $e) {
    http_response_code(400);
    echo json_encode(['error' => $e->getMessage()]);
}
?>
```

## Examples

```php
<?php
// Converting all errors to ErrorException
set_error_handler(function ($severity, $message, $file, $line) {
    if (error_reporting() & $severity) {
        throw new ErrorException($message, 0, $severity, $file, $line);
    }
});

// Now warnings become catchable exceptions
try {
    $value = $undefinedVar;
} catch (ErrorException $e) {
    echo "Caught: " . $e->getMessage();
}
?>
```

## Related Errors

- [PHP Fatal Error]({{< relref "/languages/php/fatal-error" >}}) — fatal error
- [PHP Warning]({{< relref "/languages/php/e-warning" >}}) — warning
- [PHP Notice]({{< relref "/languages/php/e-notice" >}}) — notice
