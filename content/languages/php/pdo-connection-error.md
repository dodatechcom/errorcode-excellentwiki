---
title: "[Solution] PHP PDO Connection Refused Error"
description: "Fix PHP PDO SQLSTATE[HY000] Connection refused error. Learn to resolve database connection failures with PDO."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "php"
tags: ["php", "pdo", "database", "connection", "mysql"]
severity: "error"
---

# SQLSTATE[HY000] Connection Refused

## Error Message

```
SQLSTATE[HY000] [2002] Connection refused
```

## Common Causes

- Database server is not running or has crashed
- Wrong hostname, port, or socket path in the DSN string
- Firewall is blocking the connection to the database port
- The MySQL/MariaDB service is bound to a different interface than expected

## Solutions

### Solution 1: Verify the Database Server Is Running

Check that your MySQL or MariaDB service is actively running before attempting to connect.

```php
<?php
$host = '127.0.0.1';
$port = 3306;
$dsn = "mysql:host={$host};port={$port};dbname=myapp;charset=utf8mb4";

try {
    $pdo = new PDO($dsn, 'dbuser', 'dbpassword', [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    ]);
    echo "Connected successfully";
} catch (PDOException $e) {
    if (str_contains($e->getMessage(), 'Connection refused')) {
        error_log("Database server is not running on {$host}:{$port}");
        die('Service temporarily unavailable. Please try again later.');
    }
    throw $e;
}
```

### Solution 2: Use Connection Retry Logic

Implement exponential backoff retry logic to handle temporary network interruptions gracefully.

```php
<?php
function createPdoConnection(string $dsn, string $user, string $pass, int $maxRetries = 3): PDO
{
    $attempt = 0;
    $delay = 1; // seconds

    while ($attempt < $maxRetries) {
        try {
            return new PDO($dsn, $user, $pass, [
                PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
                PDO::ATTR_PERSISTENT => true,
            ]);
        } catch (PDOException $e) {
            $attempt++;
            if ($attempt >= $maxRetries) {
                throw $e;
            }
            error_log("PDO connection attempt {$attempt} failed: {$e->getMessage()}");
            sleep($delay);
            $delay *= 2; // exponential backoff
        }
    }

    throw new RuntimeException('Could not connect to database after retries');
}
```

### Solution 3: Check DSN Configuration and Port

Verify that the DSN string uses the correct host, port, and database name for your environment.

```php
<?php
// Common DSN formats for different configurations
$dsnLocal = 'mysql:host=127.0.0.1;port=3306;dbname=myapp;charset=utf8mb4';
$dsnSocket = 'mysql:unix_socket=/var/run/mysqld/mysqld.sock;dbname=myapp;charset=utf8mb4';
$dsnRemote = 'mysql:host=10.0.1.50;port=3306;dbname=myapp;charset=utf8mb4';

// Validate connection parameters before connecting
$host = getenv('DB_HOST') ?: '127.0.0.1';
$port = getenv('DB_PORT') ?: '3306';
$dbname = getenv('DB_NAME') ?: 'myapp';

if (empty($host) || empty($port) || empty($dbname)) {
    throw new InvalidArgumentException('Missing required database configuration');
}

$dsn = "mysql:host={$host};port={$port};dbname={$dbname};charset=utf8mb4";
$pdo = new PDO($dsn, getenv('DB_USER'), getenv('DB_PASS'), [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
]);
```

## Prevention Tips

- Always store database credentials in environment variables, never hardcoded in source files
- Enable PDO::ERRMODE_EXCEPTION during development to catch connection issues immediately
- Use connection pooling or persistent connections in production to reduce connection overhead

## Related Errors

- [PHP PDOException: SQLSTATE[HY000]]({{< relref "/languages/php/pdo-error" >}})
- [Doctrine Connection Error]({{< relref "/languages/php/doctrine-connection" >}})
- [PHP Fatal Error: Allowed memory size exhausted]({{< relref "/languages/php/fatal-out-of-memory" >}})
