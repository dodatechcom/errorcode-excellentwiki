---
title: "[Solution] PHP E_RECOVERABLE_ERROR — Recoverable Error Fix"
description: "Fix PHP E_RECOVERABLE_ERROR fatal errors that can be caught. Learn to handle type hint failures and other recoverable errors in PHP."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["e-recoverable-error", "recoverable", "type-hint"]
weight: 5
---

# [Solution] PHP E_RECOVERABLE_ERROR — Recoverable Error Fix

`E_RECOVERABLE_ERROR` is a fatal-level error that can be caught using a custom error handler. It typically occurs when a strict type hint is violated in a function call, or when a security check fails. Unlike `E_ERROR`, PHP allows a custom error handler to intercept and potentially recover from this error.

## Common Causes

- Passing the wrong type to a type-hinted function parameter
- Type mismatches in function arguments
- Security-related violations that PHP treats as recoverable
- Passing `null` to a non-nullable typed parameter

## How to Fix

### 1. Pass the Correct Type to Functions

```php
// WRONG — passing string to int parameter
<?php
declare(strict_types=1);
function add(int $a, int $b): int {
    return $a + $b;
}
echo add("hello", 5); // E_RECOVERABLE_ERROR
?>

// CORRECT
<?php
declare(strict_types=1);
function add(int $a, int $b): int {
    return $a + $b;
}
echo add(3, 5); // 8
?>
```

### 2. Use a Custom Error Handler for Recovery

```php
<?php
function recoverable_error_handler($errno, $errstr, $errfile, $errline) {
    if ($errno === E_RECOVERABLE_ERROR) {
        echo "Recoverable error: $errstr in $errfile on line $errline\n";
        return true; // suppress the error
    }
    return false;
}

set_error_handler('recoverable_error_handler');
?>
```

### 3. Avoid Passing Null to Non-Nullable Parameters

```php
// WRONG — null to non-nullable int
<?php
declare(strict_types=1);
function printLength(string $text): void {
    echo strlen($text);
}
printLength(null); // E_RECOVERABLE_ERROR
?>

// CORRECT
<?php
declare(strict_types=1);
function printLength(string $text): void {
    echo strlen($text);
}
printLength("hello"); // 5
?>
```

## Examples

```php
<?php
declare(strict_types=1);
function process(array $data): void {
    foreach ($data as $item) {
        echo $item;
    }
}

// E_RECOVERABLE_ERROR: argument 1 must be of type array, string given
process("not an array");
?>
```

## Related Errors

- [PHP E_ERROR]({{< relref "/languages/php/e-error" >}})
- [PHP E_RECOVERABLE_ERROR (4096)]({{< relref "/languages/php/error-4096" >}})
- [PHP E_CORE_ERROR]({{< relref "/languages/php/e-core-error" >}})
- [PHP Fatal Error]({{< relref "/languages/php/fatal-error" >}})
