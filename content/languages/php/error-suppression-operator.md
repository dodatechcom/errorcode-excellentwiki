---
title: "[Solution] PHP @ Error Suppression Operator"
description: "Fix PHP @ error suppression operator issues by using sparingly, combining with error_log(), preferring try-catch, and understanding what it suppresses. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 111
---

# PHP @ Error Suppression Operator

The `@` operator in PHP suppresses error messages from an expression. While useful in specific cases, it hides errors that may indicate real problems, making debugging difficult. It suppresses all error levels including `E_WARNING` and `E_NOTICE` but does not suppress `E_ERROR`, `E_PARSE`, or `E_CORE_ERROR`.

## Common Causes

```php
// Cause 1: Overusing @ to silence errors
$fileContents = @file_get_contents('config.json');
// If the file is missing, you have no idea why

// Cause 2: Using @ when exceptions are better
$result = @mysqli_query($connection, $sql);
// Exceptions give stack traces and better error context

// Cause 3: @ hides all errors from the expression
$value = @$array['key'] ?? null;
// Hides both E_WARNING and E_NOTICE

// Cause 4: @ affects performance slightly
$value = @someFunction();
// PHP still records the error internally even when suppressed
```

## How to Fix

### Fix 1: Use Sparingly and Combine with error_log()

```php
$value = @file_get_contents('config.json');
if ($value === false) {
    error_log("Failed to read config.json: " . error_get_last()['message']);
}
```

### Fix 2: Prefer try-catch for Exception-Throwing Functions

```php
// Instead of:
$result = @someFunctionThatThrows();

// Use:
try {
    $result = someFunctionThatThrows();
} catch (Exception $e) {
    error_log("Error: " . $e->getMessage());
    $result = null;
}
```

### Fix 3: Use Null Coalescing Instead of @ for Arrays

```php
// Instead of:
$value = @$array['key'];

// Use:
$value = $array['key'] ?? null;

// Or for nested access:
$value = $array['level1']['level2']['key'] ?? null;
```

### Fix 4: Suppress Only When Expected Errors Are Possible

```php
// Acceptable: checking if a file exists before reading
if (file_exists($path)) {
    $content = @file_get_contents($path);
    if ($content === false) {
        error_log("Failed to read $path");
    }
} else {
    error_log("File not found: $path");
}
```

## Examples

```php
// Example: Compare @ vs proper error handling
// Bad: @ hides the problem
$connection = @new PDO($dsn, $user, $pass);

// Good: Exception gives full context
try {
    $connection = new PDO($dsn, $user, $pass);
} catch (PDOException $e) {
    error_log("Database connection failed: " . $e->getMessage());
    $connection = null;
}

// Example: @ with class method calls
$result = @$object->methodName();
// Use when the method may not exist (e.g., dynamic methods)

// Example: Acceptable uses of @
$value = @$array[0]['key'] ?? 'default';  // Array access
$result = @include 'optional_file.php';    // Include that may not exist
$email = filter_var(@$_POST['email'], FILTER_VALIDATE_EMAIL);  // Input
```

## Related Errors

- [error_get_last()](/languages/php/error-get-last)
- [error_clear_last()](/languages/php/error-clear-last)
- [error_log()](/languages/php/error-log-function)
- [set_error_handler()](/languages/php/set-error-handler)
