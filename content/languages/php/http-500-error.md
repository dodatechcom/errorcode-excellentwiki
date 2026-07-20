---
title: "[Solution] PHP HTTP 500 Internal Server Error — Uncaught Exceptions and White Screen of Death"
description: "Fix PHP HTTP 500 Internal Server Error: uncaught exceptions, white screen of death. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1101
---

# PHP HTTP 500 Internal Server Error — Uncaught Exceptions and White Screen of Death

An HTTP 500 Internal Server Error indicates something went wrong on the server but the server could not provide a more specific error message. In PHP, this commonly manifests as an uncaught exception, a fatal error, or the "white screen of death" (WSOD) where the browser displays a blank page.

## Common Causes

```php
<?php
// Uncaught exception
throw new RuntimeException("Something failed");

// Fatal error hidden behind error suppression
$result = @include 'config.php'; // file has syntax error

// Database connection failure without error handling
$pdo = new PDO('mysql:host=wronghost;dbname=test', 'user', 'pass');

// Memory exhaustion
$largeArray = range(1, PHP_INT_MAX); // Fatal error: out of memory

// Undefined function call
undeclaredFunction(); // Fatal error: call to undefined function
```

## How to Fix

### Fix 1: Enable Error Reporting in Development

```php
<?php
// At the top of your script or in a bootstrap file
error_reporting(E_ALL);
ini_set('display_errors', '1');
ini_set('log_errors', '1');
ini_set('error_log', '/var/log/php_errors.log');

// In php.ini for development
// error_reporting = E_ALL
// display_errors = On
// log_errors = On
// error_log = /var/log/php_errors.log
```

### Fix 2: Check PHP Error Logs

```bash
# Check Apache error log
tail -f /var/log/apache2/error.log

# Check PHP-FPM error log
tail -f /var/log/php8.2-fpm.log

# Check Nginx error log
tail -f /var/log/nginx/error.log

# Search for recent errors
grep -i "error\|fatal\|warning" /var/log/apache2/error.log | tail -20
```

### Fix 3: Use Global Exception Handler

```php
<?php
// Register a global exception handler
set_exception_handler(function (Throwable $e) {
    error_log("Uncaught exception: " . $e->getMessage()
        . " in " . $e->getFile()
        . ":" . $e->getLine());

    http_response_code(500);

    // In development, show details
    if (getenv('APP_DEBUG') === 'true') {
        echo "<pre>" . htmlspecialchars($e->getMessage()) . "\n"
            . $e->getTraceAsString() . "</pre>";
    } else {
        echo "Internal Server Error";
    }
});

// Register a shutdown function to catch fatal errors
register_shutdown_function(function () {
    $error = error_get_last();
    if ($error !== null && in_array($error['type'], [E_ERROR, E_PARSE, E_CORE_ERROR])) {
        error_log("Fatal error: " . $error['message']
            . " in " . $error['file']
            . ":" . $error['line']);

        http_response_code(500);
        echo "Internal Server Error";
    }
});
```

### Fix 4: Use Try-Catch for Exception Handling

```php
<?php
function processOrder(array $data): array
{
    try {
        $user = findUser($data['user_id']);

        if ($user === null) {
            throw new InvalidArgumentException("User not found: {$data['user_id']}");
        }

        $order = createOrder($data);

        sendConfirmationEmail($user, $order);

        return $order;
    } catch (PDOException $e) {
        error_log("Database error: " . $e->getMessage());
        throw new RuntimeException("Database error occurred", 500, $e);
    } catch (Exception $e) {
        error_log("Order processing failed: " . $e->getMessage());
        throw new RuntimeException("Order processing failed", 500, $e);
    }
}
```

### Fix 5: Create a Custom Error Page

```php
<?php
// error_handler.php
function handleError(int $errno, string $errstr, string $errfile, int $errline): bool
{
    $logMessage = sprintf(
        "[%s] %s: %s in %s on line %d\n",
        date('Y-m-d H:i:s'),
        match ($errno) {
            E_ERROR => 'ERROR',
            E_WARNING => 'WARNING',
            E_NOTICE => 'NOTICE',
            default => "TYPE($errno)",
        },
        $errstr,
        $errfile,
        $errline
    );

    error_log($logMessage);

    if (error_reporting() & $errno) {
        http_response_code(500);
        require __DIR__ . '/templates/500.php';
    }

    return true;
}

set_error_handler('handleError');
```

## Examples

```php
<?php
// Example 1: Proper API error handling
header('Content-Type: application/json');

try {
    $data = json_decode(file_get_contents('php://input'), true);

    if ($data === null) {
        http_response_code(400);
        echo json_encode(['error' => 'Invalid JSON']);
        exit;
    }

    $result = processPayment($data);

    http_response_code(200);
    echo json_encode(['success' => true, 'transaction_id' => $result]);

} catch (PDOException $e) {
    error_log("DB error: " . $e->getMessage());
    http_response_code(500);
    echo json_encode(['error' => 'Database error']);

} catch (Exception $e) {
    error_log("Error: " . $e->getMessage());
    http_response_code(500);
    echo json_encode(['error' => 'Internal server error']);
}

// Example 2: White screen of death debugging
// Add to top of index.php during debugging:
error_reporting(E_ALL);
ini_set('display_errors', '1');

// Check if output is being buffered silently:
$bufferedContent = ob_get_contents();
if ($bufferedContent !== false && strlen($bufferedContent) > 0) {
    error_log("Buffered output detected: " . strlen($bufferedContent) . " bytes");
}
```

## Related Errors

- [PHP Fatal Error]({{< relref "/languages/php/fatal-error" >}})
- [PHP Fatal Out of Memory]({{< relref "/languages/php/fatal-out-of-memory" >}})
- [PHP Unhandled Match Error]({{< relref "/languages/php/unhandledmatcherror" >}})
