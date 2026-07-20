---
title: "[Solution] PHP error_clear_last() — Clear Last Error"
description: "Fix PHP error_clear_last() issues by clearing before operations, using in error handling, and understanding behavior. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 107
---

# PHP error_clear_last() — Clear Last Error

The `error_clear_last()` function clears the last PHP error so that `error_get_last()` returns `null`. It is essential when you need to check whether a specific operation triggered an error, rather than seeing a stale error from a previous operation. Introduced in PHP 7.0.

## Common Causes

```php
// Cause 1: Not clearing before an operation
$riskyOperation();
$error = error_get_last();
// May contain an error from a previous operation

// Cause 2: Calling error_get_last() without clearing first
$error = error_get_last();
// Could be a stale error from unknown origin

// Cause 3: Not using with @ operator
error_clear_last();
@someFunction(); // Silences errors but still records them
$error = error_get_last(); // May still have the error

// Cause 4: Assuming it affects error_reporting or display_errors
error_clear_last();
// This does NOT change error reporting behavior
```

## How to Fix

### Fix 1: Clear Before Operations

```php
// Clear before checking if an operation succeeds
error_clear_last();
$result = @fopen('nonexistent.txt', 'r');

$error = error_get_last();
if ($error !== null) {
    echo "Operation failed: " . $error['message'];
}
```

### Fix 2: Use in Error Handling Workflows

```php
function safeExecute(callable $fn, $context = '') {
    error_clear_last();
    $result = $fn();
    $error = error_get_last();

    if ($error !== null) {
        error_log("$context: " . $error['message'] . " in " . $error['file'] . ':' . $error['line']);
        return null;
    }

    return $result;
}

$result = safeExecute(function () {
    return json_decode('invalid json', true);
}, 'JSON decode');
```

### Fix 3: Combine with error_get_last() in Conditionals

```php
error_clear_last();
@include 'config.php';

$error = error_get_last();
if ($error !== null && $error['type'] === E_WARNING) {
    echo "Config file not found, using defaults";
}

error_clear_last();
$connection = @new PDO($dsn, $user, $pass);

$error = error_get_last();
if ($error !== null) {
    echo "Database connection failed: " . $error['message'];
}
```

## Examples

```php
// Example: Test multiple operations
$operations = [
    'json'    => fn() => json_decode('bad', true),
    'file'    => fn() => @file_get_contents('missing.txt'),
    'include' => fn() => @include 'missing.php',
];

foreach ($operations as $name => $op) {
    error_clear_last();
    $op();
    $error = error_get_last();

    if ($error !== null) {
        echo "$name failed: " . $error['message'] . PHP_EOL;
    } else {
        echo "$name succeeded" . PHP_EOL;
    }
}

// Example: Verify null after clear
error_clear_last();
$error = error_get_last();
var_dump($error); // NULL
```

## Related Errors

- [error_get_last()](/languages/php/error-get-last)
- [error_reporting()](/languages/php/error-reporting-function)
- [@ error suppression operator](/languages/php/error-suppression-operator)
