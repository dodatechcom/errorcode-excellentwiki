---
title: "[Solution] PHP register_shutdown_function() — Shutdown Callback Usage"
description: "Fix PHP register_shutdown_function() issues by catching fatal errors at shutdown, using error_get_last(), and cleaning up resources. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 110
---

# PHP register_shutdown_function() — Shutdown Callback Usage

The `register_shutdown_function()` function registers a function to be executed when the script finishes or terminates. It is the only way to catch fatal errors, memory exhaustion, and other script-terminating conditions. Issues include not checking `error_get_last()` in the callback or registering too many shutdown functions.

## Common Causes

```php
// Cause 1: Not checking for errors in the shutdown function
register_shutdown_function(function () {
    echo "Script finished";
    // Fatal errors are not detected
});

// Cause 2: Not using error_get_last() to check for fatal errors
register_shutdown_function(function () {
    $error = error_get_last();
    // Not checking if $error is a fatal error type
});

// Cause 3: Registering shutdown function too late
// (after a fatal error has already occurred)
register_shutdown_function(function () {
    // This may not execute if registered too late
});

// Cause 4: Shutdown function throws an exception
register_shutdown_function(function () {
    throw new RuntimeException("Shutdown failed");
    // Exceptions in shutdown functions are not caught
});
```

## How to Fix

### Fix 1: Check error_get_last() for Fatal Errors

```php
register_shutdown_function(function () {
    $error = error_get_last();

    if ($error !== null && in_array($error['type'], [
        E_ERROR,
        E_PARSE,
        E_CORE_ERROR,
        E_CORE_WARNING,
        E_COMPILE_ERROR,
        E_COMPILE_WARNING,
        E_USER_ERROR,
    ])) {
        error_log(sprintf(
            "Fatal error [%d]: %s in %s on line %d",
            $error['type'],
            $error['message'],
            $error['file'],
            $error['line']
        ));

        http_response_code(500);
        echo 'An unexpected error occurred.';
    }
});
```

### Fix 2: Clean Up Resources

```php
$database = new PDO($dsn, $user, $pass);
$tempFile = tempnam('/tmp', 'app_');

register_shutdown_function(function () use ($database, $tempFile) {
    $error = error_get_last();
    if ($error !== null && $error['type'] === E_ERROR) {
        error_log("Fatal error: " . $error['message']);
    }

    // Clean up resources
    if ($database) {
        $database = null;
    }
    if ($tempFile && file_exists($tempFile)) {
        unlink($tempFile);
    }
});
```

### Fix 3: Use with Multiple Shutdown Functions

```php
// Register multiple cleanup functions
register_shutdown_function(function () {
    error_log("Shutdown 1: Flushing buffers");
    ob_end_flush();
});

register_shutdown_function(function () {
    error_log("Shutdown 2: Closing database");
    // Close database connections
});

register_shutdown_function(function () {
    error_log("Shutdown 3: Final checks");
    $error = error_get_last();
    if ($error !== null) {
        error_log("Last error: " . $error['message']);
    }
});
```

## Examples

```php
// Example: Complete error handling with shutdown function
register_shutdown_function(function () {
    $error = error_get_last();
    if ($error === null) {
        return;
    }

    $fatalTypes = [
        E_ERROR, E_PARSE, E_CORE_ERROR,
        E_COMPILE_ERROR, E_USER_ERROR,
    ];

    if (in_array($error['type'], $fatalTypes)) {
        $logEntry = [
            'timestamp' => date('c'),
            'level'     => 'FATAL',
            'message'   => $error['message'],
            'file'      => $error['file'],
            'line'      => $error['line'],
        ];
        error_log(json_encode($logEntry) . PHP_EOL, 3, '/var/log/fatal.log');
    }
});

// Example: Measure script execution time
register_shutdown_function(function () {
    $elapsed = microtime(true) - $_SERVER['REQUEST_TIME_FLOAT'];
    error_log(sprintf("Script execution time: %.4f seconds", $elapsed));
});
```

## Related Errors

- [error_get_last()](/languages/php/error-get-last)
- [error_log()](/languages/php/error-log-function)
- [fatal-error](/languages/php/fatal-error)
