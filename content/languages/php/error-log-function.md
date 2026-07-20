---
title: "[Solution] PHP error_log() — Error Logging Function"
description: "Fix PHP error_log() issues by logging to file, syslog, email, using proper message format, and handling errors. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 105
---

# PHP error_log() — Error Logging Function

The `error_log()` function sends an error message to a defined error handling routine. It can log to a file, system logger, or remote destination via TCP. Issues include incorrect destination types, missing log file configuration, and unformatted messages that make debugging difficult.

## Common Causes

```php
// Cause 1: Using default destination without configuring log_errors
error_log("Something went wrong");
// Nothing happens if log_errors is Off

// Cause 2: Wrong destination type parameter
error_log("Error message", 3, "/var/log/app.log", 1); // Incorrect format

// Cause 3: Logging email without proper message format
error_log("Error details", 1, "admin@example.com");
// message parameter needs to be a valid email message

// Cause 4: Not validating the return value
error_log("Error", 3, "/nonexistent/path/app.log");
// Returns false on failure
```

## How to Fix

### Fix 1: Log to a File

```php
// Enable error logging first
ini_set('log_errors', '1');
ini_set('error_log', '/var/log/php_errors.log');

// Then use error_log for custom messages
error_log("Application error: " . $e->getMessage(), 3, '/var/log/app.log');
```

### Fix 2: Log to System Logger (syslog)

```php
// destination type 0 = PHP system logger (syslog)
error_log("Critical system error", 0);
// Uses syslog identifier from error_log ini setting
```

### Fix 3: Log via Email

```php
// destination type 1 = email
$to = "admin@example.com";
$subject = "Application Error";
$message = "An error occurred: " . $errorMessage;
$headers = "From: noreply@example.com\r\n";

error_log($message, 1, $to, $headers);
```

### Fix 4: Use Proper Message Format

```php
function logError($level, $message, $file = null, $line = null) {
    $timestamp = date('Y-m-d H:i:s');
    $formatted = "[$timestamp] [$level] $message";
    if ($file && $line) {
        $formatted .= " in $file:$line";
    }
    $formatted .= PHP_EOL;

    error_log($formatted, 3, '/var/log/app.log');
}

logError('ERROR', 'Database connection failed', 'db.php', 42);
```

## Examples

```php
// Example: Log with return value check
$result = error_log("Test message", 3, '/var/log/app.log');
if ($result === false) {
    echo "Failed to write to log file";
}

// Example: Log to TCP socket
error_log("Remote log message", 2, "logserver.example.com:514");

// Example: Structured logging
$logEntry = json_encode([
    'timestamp' => date('c'),
    'level'     => 'ERROR',
    'message'   => 'Failed to process request',
    'context'   => [
        'user_id' => 123,
        'url'     => $_SERVER['REQUEST_URI'],
    ],
]);
error_log($logEntry . PHP_EOL, 3, '/var/log/app.log');
```

## Related Errors

- [error_reporting()](/languages/php/error-reporting-function)
- [display_errors](/languages/php/display-errors)
- [error_get_last()](/languages/php/error-get-last)
