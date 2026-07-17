---
title: "[Solution] PHP Error 4096 — E_RECOVERABLE_ERROR Fix"
description: "Fix PHP error code 4096 E_RECOVERABLE_ERROR. Learn to handle recoverable fatal errors from type hint violations and recoverable conditions."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# [Solution] PHP Error 4096 — E_RECOVERABLE_ERROR Fix

PHP error code 4096 corresponds to `E_RECOVERABLE_ERROR` (4096). This is a fatal-level error that can be caught by a custom error handler. It typically occurs when a strict type hint is violated — PHP encounters a type mismatch that prevents the function from executing, but the error is theoretically recoverable.

## Common Causes

- Passing the wrong type to a type-hinted parameter
- Passing `null` to a non-nullable typed parameter
- Type coercion failures in strict mode
- Security-related violations that PHP classifies as recoverable

## How to Fix

### 1. Match the Expected Type

```php
// WRONG — passing int to string parameter
<?php
declare(strict_types=1);
function greet(string $name): string {
    return "Hello, $name";
}
echo greet(42); // E_RECOVERABLE_ERROR
?>

// CORRECT
<?php
declare(strict_types=1);
function greet(string $name): string {
    return "Hello, $name";
}
echo greet("Alice");
?>
```

### 2. Handle Null Values Properly

```php
// WRONG — null to non-nullable parameter
<?php
declare(strict_types=1);
function printLength(string $text): void {
    echo strlen($text);
}
printLength(null); // E_RECOVERABLE_ERROR
?>

// CORRECT — provide a default or check before calling
<?php
declare(strict_types=1);
function printLength(string $text): void {
    echo strlen($text);
}
$value = $input ?? '';
printLength($value);
?>
```

### 3. Use a Custom Error Handler

```php
<?php
function recoverable_handler($errno, $errstr, $errfile, $errline) {
    if ($errno === E_RECOVERABLE_ERROR) {
        throw new ErrorException($errstr, 0, $errno, $errfile, $errline);
    }
    return false;
}

set_error_handler('recoverable_handler');

try {
    // code that may trigger E_RECOVERABLE_ERROR
} catch (ErrorException $e) {
    echo "Recovered from: " . $e->getMessage();
}
?>
```

### 4. Validate Arguments Before Calling

```php
<?php
declare(strict_types=1);
function process(int $id, string $name): string {
    return "Processing $id: $name";
}

$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
$name = filter_input(INPUT_GET, 'name', FILTER_SANITIZE_FULL_SPECIAL_CHARS);

if ($id !== false && is_string($name)) {
    echo process($id, $name);
} else {
    echo "Invalid input";
}
?>
```

## Examples

```php
<?php
declare(strict_types=1);
function setAge(int $age): void {
    echo "Age: $age\n";
}

// Error 4096: E_RECOVERABLE_ERROR
setAge("twenty"); // cannot convert string to int in strict mode
setAge(null);     // null to non-nullable int
?>
```

## Related Errors

- [PHP E_RECOVERABLE_ERROR]({{< relref "/languages/php/e-recoverable-error" >}})
- [PHP E_ERROR]({{< relref "/languages/php/e-error" >}})
- [PHP E_USER_ERROR]({{< relref "/languages/php/e-user-error" >}})
- [PHP Fatal Error]({{< relref "/languages/php/fatal-error" >}})
