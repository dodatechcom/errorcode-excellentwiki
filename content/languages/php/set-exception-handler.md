---
title: "[Solution] PHP set_exception_handler() — Uncaught Exception Handler"
description: "Fix PHP set_exception_handler() issues by handling uncaught exceptions, using set_error_handler(), logging exceptions, and sending error pages. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 109
---

# PHP set_exception_handler() — Uncaught Exception Handler

The `set_exception_handler()` function registers a handler for uncaught exceptions. It is the last line of defense for exceptions that escape try-catch blocks. Issues include not logging exceptions, exposing sensitive details in error pages, or not using it alongside `set_error_handler()`.

## Common Causes

```php
// Cause 1: Not logging the exception
set_exception_handler(function (Throwable $e) {
    echo "Something went wrong";
    // Exception details are lost
});

// Cause 2: Exposing stack traces to users
set_exception_handler(function (Throwable $e) {
    echo $e->getMessage() . "\n" . $e->getTraceAsString();
});

// Cause 3: Not setting HTTP response code
set_exception_handler(function (Throwable $e) {
    error_log($e->getMessage());
    // Default 200 status code sent to user
});

// Cause 4: Handler itself throws an exception
set_exception_handler(function (Throwable $e) {
    error_log($e->getMessage());
    throw new RuntimeException("Handler failed");
    // Fatal error
});
```

## How to Fix

### Fix 1: Log Exceptions and Send Generic Error Page

```php
set_exception_handler(function (Throwable $e) {
    error_log(sprintf(
        "Uncaught %s: %s in %s on line %d",
        get_class($e),
        $e->getMessage(),
        $e->getFile(),
        $e->getLine()
    ));

    http_response_code(500);
    header('Content-Type: text/html');
    echo '<!DOCTYPE html><html><body><h1>Internal Server Error</h1></body></html>';
});
```

### Fix 2: Use with set_error_handler()

```php
// Convert errors to exceptions
set_error_handler(function ($errno, $errstr, $errfile, $errline) {
    throw new ErrorException($errstr, 0, $errno, $errfile, $errline);
});

// Handle all uncaught exceptions
set_exception_handler(function (Throwable $e) {
    error_log($e->getMessage());
    http_response_code(500);
    echo 'Internal Server Error';
});
```

### Fix 3: Log Full Context

```php
set_exception_handler(function (Throwable $e) {
    $logEntry = [
        'timestamp' => date('c'),
        'class'     => get_class($e),
        'message'   => $e->getMessage(),
        'file'      => $e->getFile(),
        'line'      => $e->getLine(),
        'trace'     => $e->getTraceAsString(),
        'code'      => $e->getCode(),
    ];
    error_log(json_encode($logEntry) . PHP_EOL, 3, '/var/log/exceptions.log');

    http_response_code(500);
    echo 'An error occurred. Please try again later.';
});
```

## Examples

```php
// Example: Environment-aware handler
set_exception_handler(function (Throwable $e) {
    error_log($e->getMessage());

    if (getenv('APP_ENV') === 'development') {
        echo "<pre>" . $e->getMessage() . "\n" . $e->getTraceAsString() . "</pre>";
    } else {
        http_response_code(500);
        echo 'An unexpected error occurred.';
    }
});

// Example: Send email on critical exceptions
set_exception_handler(function (Throwable $e) {
    error_log($e->getMessage());

    if ($e->getCode() >= 500 || $e instanceof ErrorException) {
        mail(
            'admin@example.com',
            'Critical Error',
            "Exception: " . $e->getMessage() . "\nFile: " . $e->getFile() . ":" . $e->getLine()
        );
    }

    http_response_code(500);
    echo 'An error occurred.';
});
```

## Related Errors

- [set_error_handler()](/languages/php/set-error-handler)
- [ErrorException](/languages/php/errorexception)
- [error_log()](/languages/php/error-log-function)
