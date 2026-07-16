---
title: "PHP PDOException: SQLSTATE[HY000]"
description: "Fix PHP PDOException SQLSTATE[HY000] errors. Learn to resolve database connection failures and query errors."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["pdo", "database", "sqlstate", "hy000", "connection", "exception"]
weight: 5
---

# PHP PDOException: SQLSTATE[HY000]

PDO exceptions with SQLSTATE codes indicate database connection or query failures. HY000 is the generic driver error code, with specific sub-codes providing more detail.

## Common Causes

- Database server is down or unreachable
- Wrong hostname, port, username, or password in DSN
- Database does not exist or was dropped
- Too many concurrent connections exceeding server limit

## How to Fix

### Use try-catch for PDO Errors

```php
<?php
try {
    $pdo = new PDO(
        'mysql:host=localhost;dbname=myapp;charset=utf8mb4',
        'user',
        'password',
        [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        ]
    );
} catch (PDOException $e) {
    error_log('Database error: ' . $e->getMessage());
    die('Database connection failed. Please try again later.');
}
?>
```

### Verify Connection Parameters

```php
<?php
// Test connection separately
$dsn = 'mysql:host=localhost;port=3306;dbname=testdb';
try {
    $pdo = new PDO($dsn, 'user', 'pass');
    echo 'Connected successfully';
} catch (PDOException $e) {
    echo 'Connection failed: ' . $e->getMessage();
}
?>
```

### Increase Connection Limit

```sql
-- Check MySQL max connections
SHOW VARIABLES LIKE 'max_connections';
SET GLOBAL max_connections = 200;
```

### Use Connection Pooling for Production

```php
<?php
// Use persistent connections
$pdo = new PDO($dsn, $user, $pass, [
    PDO::ATTR_PERSISTENT => true,
]);
?>
```

## Examples

```php
<?php
// Example 1: Connection refused
try {
    $pdo = new PDO('mysql:host=192.168.1.999;dbname=mydb', 'user', 'pass');
} catch (PDOException $e) {
    echo $e->getMessage();
    // SQLSTATE[HY000] [2002] Connection refused
    // Fix: verify host is correct and MySQL is running
}

// Example 2: Unknown database
try {
    $pdo = new PDO('mysql:host=localhost;dbname=nonexistent', 'user', 'pass');
} catch (PDOException $e) {
    echo $e->getMessage();
    // SQLSTATE[HY000] [1049] Unknown database 'nonexistent'
    // Fix: create the database or correct the name
}

// Example 3: Too many connections
try {
    $pdo = new PDO('mysql:host=localhost;dbname=mydb', 'user', 'pass');
} catch (PDOException $e) {
    echo $e->getMessage();
    // SQLSTATE[HY000] [1040] Too many connections
    // Fix: increase max_connections or use connection pooling
}
?>
```

## Related Errors

- [PHP Fatal Error: Allowed memory size exhausted]({{< relref "/languages/php/fatal-error" >}})
- [PHP Fatal error: Call to undefined function]({{< relref "/languages/php/call-to-undefined" >}})
- [PHP Cannot modify header information]({{< relref "/languages/php/headers-sent" >}})
