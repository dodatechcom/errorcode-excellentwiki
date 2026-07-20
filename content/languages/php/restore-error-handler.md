---
title: "[Solution] PHP restore_error_handler() — Restore Previous Error Handler"
description: "Fix PHP restore_error_handler() issues by restoring after custom handler, pairing with set_error_handler(), and understanding scope. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 103
---

# PHP restore_error_handler() — Restore Previous Error Handler

The `restore_error_handler()` function reverts the error handler to the one that was active before the most recent `set_error_handler()` call. Failing to restore the error handler can cause unexpected behavior in libraries or frameworks that install their own handlers. Understanding scope and proper pairing is essential.

## Common Causes

```php
// Cause 1: Not restoring after custom handling
set_error_handler(function ($errno, $errstr) {
    return true;
});
// ... later code relies on the default handler
// But it was never restored

// Cause 2: Restoring too early
set_error_handler(function ($errno, $errstr) {
    restore_error_handler(); // Restores before handling completes
    return true;
});

// Cause 3: Assuming restore_error_handler() resets to the default
// It actually restores to the previously set handler, not necessarily the default

// Cause 4: Using restore_error_handler() without set_error_handler()
restore_error_handler(); // May produce a warning
```

## How to Fix

### Fix 1: Pair with set_error_handler()

```php
set_error_handler(function ($errno, $errstr, $errfile, $errline) {
    error_log("$errstr in $errfile on line $errline");
    return true;
});

// ... perform operations that need custom handling ...

restore_error_handler(); // Restore previous handler when done
```

### Fix 2: Restore After Temporary Override

```php
function performWithCustomErrorHandler(callable $fn) {
    set_error_handler(function ($errno, $errstr, $errfile, $errline) {
        throw new ErrorException($errstr, 0, $errno, $errfile, $errline);
    });

    try {
        $result = $fn();
    } finally {
        restore_error_handler();
    }

    return $result;
}

// Usage
$result = performWithCustomErrorHandler(function () {
    // Code that may trigger errors
    return some_risky_operation();
});
```

### Fix 3: Store Previous Handler Manually

```php
$previousHandler = set_error_handler(function ($errno, $errstr) {
    error_log("Custom: $errstr");
    return true;
});

// ... operations ...

// Restore to specific handler
restore_error_handler(); // Goes back to $previousHandler
```

## Examples

```php
// Example: Scoped error handling in a class
class ErrorHandler
{
    private ?\callable $previousHandler = null;

    public function enable(): void
    {
        $this->previousHandler = set_error_handler(
            function ($errno, $errstr, $errfile, $errline) {
                error_log("Custom: $errstr in $errfile:$errline");
                return true;
            }
        );
    }

    public function disable(): void
    {
        restore_error_handler();
        $this->previousHandler = null;
    }
}

// Example: Verify handler restoration
set_error_handler(function ($errno, $errstr) {
    echo "Handler A\n";
    return true;
});

set_error_handler(function ($errno, $errstr) {
    echo "Handler B\n";
    return true;
});

restore_error_handler(); // Restores Handler A
```

## Related Errors

- [set_error_handler()](/languages/php/set-error-handler)
- [error_reporting()](/languages/php/error-reporting-function)
