---
title: "[Solution] PHP error_get_last() — Retrieve Last Error"
description: "Fix PHP error_get_last() issues by retrieving last error, checking error type/message/file, and using in error handling. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 106
---

# PHP error_get_last() — Retrieve Last Error

The `error_get_last()` function returns the last error that occurred, or `null` if no error occurred. It returns an associative array with `type`, `message`, `file`, and `line` keys. Common issues include not checking for `null`, using it at the wrong time, or not filtering by error type.

## Common Causes

```php
// Cause 1: Not checking for null return
$error = error_get_last();
echo $error['message']; // Warning: Trying to access array offset on null

// Cause 2: Using after another error_get_last() call has cleared it
error_get_last(); // First call
error_get_last(); // Returns null

// Cause 3: Not filtering by error type
$error = error_get_last();
// Returns the LAST error of any type, not necessarily the one you want

// Cause 4: Not clearing before an operation
error_get_last(); // May return a stale error
// Should use error_clear_last() first
```

## How to Fix

### Fix 1: Check for null Before Accessing

```php
$error = error_get_last();

if ($error !== null) {
    echo "Type: " . $error['type'] . PHP_EOL;
    echo "Message: " . $error['message'] . PHP_EOL;
    echo "File: " . $error['file'] . PHP_EOL;
    echo "Line: " . $error['line'] . PHP_EOL;
}
```

### Fix 2: Check Error Type Before Processing

```php
error_clear_last();
$riskyOperation();

$error = error_get_last();

if ($error !== null) {
    $fatalTypes = [E_ERROR, E_PARSE, E_CORE_ERROR, E_COMPILE_ERROR];
    if (in_array($error['type'], $fatalTypes)) {
        error_log("Fatal error: " . $error['message']);
    }
}
```

### Fix 3: Use in Shutdown Function

```php
register_shutdown_function(function () {
    $error = error_get_last();
    if ($error !== null && in_array($error['type'], [E_ERROR, E_PARSE, E_CORE_ERROR])) {
        error_log("Shutdown error: " . $error['message'] . " in " . $error['file']);
    }
});
```

## Examples

```php
// Example: Clear before operation
error_clear_last();
$result = @include 'nonexistent_file.php';
$error = error_get_last();

if ($error !== null && $error['type'] === E_WARNING) {
    echo "File not found: " . $error['message'];
}

// Example: Map error types to human-readable strings
function getErrorTypeName($type) {
    $types = [
        E_ERROR             => 'Error',
        E_WARNING           => 'Warning',
        E_NOTICE            => 'Notice',
        E_PARSE             => 'Parse Error',
        E_DEPRECATED        => 'Deprecated',
        E_USER_ERROR        => 'User Error',
        E_USER_WARNING      => 'User Warning',
        E_USER_NOTICE       => 'User Notice',
        E_USER_DEPRECATED   => 'User Deprecated',
        E_STRICT            => 'Strict',
        E_RECOVERABLE_ERROR => 'Recoverable Error',
        E_CORE_ERROR        => 'Core Error',
        E_CORE_WARNING      => 'Core Warning',
        E_COMPILE_ERROR     => 'Compile Error',
        E_COMPILE_WARNING   => 'Compile Warning',
    ];
    return $types[$type] ?? "Unknown ($type)";
}

$error = error_get_last();
if ($error !== null) {
    echo getErrorTypeName($error['type']) . ": " . $error['message'];
}
```

## Related Errors

- [error_clear_last()](/languages/php/error-clear-last)
- [error_log()](/languages/php/error-log-function)
- [error_reporting()](/languages/php/error-reporting-function)
