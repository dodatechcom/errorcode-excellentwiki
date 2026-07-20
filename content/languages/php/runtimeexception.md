---
title: "[Solution] PHP RuntimeException — Base Runtime Error Exception"
description: "Fix PHP RuntimeException by adding try-catch blocks, handling errors gracefully, and logging exceptions."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# RuntimeException — Base Runtime Error Exception

RuntimeException is the base class for all runtime exceptions — errors that occur during script execution due to external factors rather than logic bugs. It covers filesystem errors, network failures, database connection issues, and other problems that cannot be predicted at compile time. Many SPL exceptions extend RuntimeException.

## Common Causes

- File not found or permission denied during operations
- Database connection or query failures
- Network timeouts or connection refused
- Resource exhaustion (memory, file handles, etc.)
- External service unavailable

## How to Fix

### Fix 1: Add Try-Catch Blocks for Exception Handling

Wrap potentially failing operations in try-catch blocks.

```php
<?php
try {
    $content = file_get_contents('/path/to/file.txt');
    if ($content === false) {
        throw new RuntimeException("Failed to read file: /path/to/file.txt");
    }
} catch (RuntimeException $e) {
    error_log("File error: " . $e->getMessage());
    $content = '';
}
?>
```

### Fix 2: Handle Errors Gracefully with Fallbacks

Provide sensible fallbacks when operations fail.

```php
<?php
function loadConfig(string $path): array
{
    try {
        $json = file_get_contents($path);
        if ($json === false) {
            throw new RuntimeException("Cannot read config file: $path");
        }

        $config = json_decode($json, true);
        if (json_last_error() !== JSON_ERROR_NONE) {
            throw new RuntimeException("Invalid JSON in config: $path");
        }

        return $config;
    } catch (RuntimeException $e) {
        error_log($e->getMessage());
        return ['debug' => false, 'cache' => true]; // Default config
    }
}
?>
```

### Fix 3: Log Exceptions for Debugging

Always log exceptions to aid in debugging and monitoring.

```php
<?php
function processData(array $data): Result
{
    try {
        // Process data
        $result = $this->processor->run($data);
        return $result;
    } catch (RuntimeException $e) {
        error_log(sprintf(
            "[%s] RuntimeException in %s:%d - %s",
            date('Y-m-d H:i:s'),
            $e->getFile(),
            $e->getLine(),
            $e->getMessage()
        ));
        throw $e; // Re-throw after logging
    }
}
?>
```

### Fix 4: Use Custom RuntimeException Subclasses

Create specific exception types for different runtime errors.

```php
<?php
class DatabaseConnectionException extends RuntimeException {}
class FilePermissionException extends RuntimeException {}
class NetworkTimeoutException extends RuntimeException {}

try {
    $db->connect($host, $port);
} catch (DatabaseConnectionException $e) {
    // Handle database-specific error
    $fallback = $this->getCachedData();
} catch (RuntimeException $e) {
    // Handle general runtime error
    $fallback = [];
}
?>
```

## Examples

```php
<?php
// Example 1: File operation failure
$file = fopen('nonexistent.txt', 'r');
// RuntimeException or Warning depending on error handling
// Fix: check file existence before opening

// Example 2: Database query failure
$pdo = new PDO($dsn, $user, $pass);
$pdo->query('SELECT * FROM nonexistent_table');
// RuntimeException via PDOException
// Fix: wrap in try-catch and handle gracefully

// Example 3: Network request failure
$response = file_get_contents('https://api.example.com/data');
// RuntimeException if URL is unreachable
// Fix: use curl with timeout and error handling
?>
```

## Related Errors

- [PHP LogicException]({{< relref "/languages/php/logicexception" >}})
- [PHP BadFunctionCallException]({{< relref "/languages/php/badfunctioncallexception" >}})
- [PHP Fatal Error: Allowed memory size exhausted]({{< relref "/languages/php/fatal-out-of-memory" >}})
