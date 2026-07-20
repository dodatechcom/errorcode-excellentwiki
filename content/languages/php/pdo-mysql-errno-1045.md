---
title: "[Solution] MySQL Error 1045 — Access Denied (PDO)"
description: "Fix MySQL PDO error 1045 access denied. Verify credentials, check user privileges, reset password, check host restrictions. Copy-paste solutions."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 233
---

# MySQL Error 1045 — Access Denied (PDO)

MySQL error 1045 occurs when the server rejects a connection due to incorrect username, password, or host restrictions. This error is common during deployment, after password changes, or when MySQL user privileges are misconfigured.

## Common Causes

```php
// Wrong password in connection
$pdo = new PDO('mysql:host=localhost;dbname=mydb', 'user', 'wrongpassword');
// SQLSTATE[HY000]: Access denied for user 'user'@'localhost'
```

```php
// Wrong host specification
$pdo = new PDO('mysql:host=127.0.0.1;dbname=mydb', 'user', 'pass');
// User 'user'@'localhost' cannot connect from '127.0.0.1'
```

```php
// Wrong port number
$pdo = new PDO('mysql:host=localhost;port=3307;dbname=mydb', 'user', 'pass');
// MySQL is on port 3306, not 3307
```

```php
// User doesn't exist in MySQL
$pdo = new PDO('mysql:host=localhost;dbname=mydb', 'nonexistent_user', 'pass');
// Access denied for user 'nonexistent_user'@'localhost'
```

```php
// Authentication plugin mismatch (MySQL 8.0)
$pdo = new PDO('mysql:host=localhost;dbname=mydb', 'user', 'pass');
// Error: The server requested authentication method unknown to the client
```

## How to Fix

### Fix 1: Verify Credentials in MySQL CLI

```bash
# Test connection from command line
mysql -u username -p -h localhost -P 3306

# If this works, the issue is in PHP configuration
# If this fails, the MySQL user needs to be fixed
```

### Fix 2: Check MySQL User Permissions

```sql
-- Check user exists and has correct host
SELECT user, host, plugin FROM mysql.user WHERE user = 'your_user';

-- Check privileges
SHOW GRANTS FOR 'your_user'@'localhost';

-- Grant privileges if missing
GRANT ALL PRIVILEGES ON yourdb.* TO 'your_user'@'localhost';
FLUSH PRIVILEGES;
```

### Fix 3: Reset MySQL Password

```bash
# Stop MySQL
sudo systemctl stop mysql

# Start without password
sudo mysqld_safe --skip-grant-tables &

# Connect and reset password
mysql -u root
UPDATE mysql.user SET authentication_string=PASSWORD('newpass') WHERE user='your_user';
FLUSH PRIVILEGES;

# Restart MySQL normally
sudo systemctl start mysql
```

### Fix 4: Handle MySQL 8.0 Authentication

```php
// MySQL 8.0 uses caching_sha2_password by default
// Use native_password plugin for PHP compatibility
$pdo = new PDO(
    'mysql:host=localhost;dbname=mydb',
    'user',
    'pass',
    [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::MYSQL_ATTR_FOUND_ROWS => true,
    ]
);

// If authentication fails, check MySQL user plugin:
// mysql> SELECT user, plugin FROM mysql.user WHERE user = 'your_user';
// mysql> ALTER USER 'your_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
```

### Fix 5: Fix Host Restrictions

```php
// If user can only connect from specific host
// Check what host the user is bound to
// mysql> SELECT user, host FROM mysql.user WHERE user = 'your_user';

// Match the host in your DSN
$hosts = [
    'localhost',    // Local socket connection
    '127.0.0.1',   // Local TCP/IP
    '%'            // Any host (not recommended)
];

// Try connecting with correct host
$dsn = 'mysql:host=localhost;dbname=mydb;port=3306';
$pdo = new PDO($dsn, 'user', 'pass');

// Or update MySQL user to accept connections from any host
// mysql> CREATE USER 'user'@'%' IDENTIFIED BY 'pass';
// mysql> GRANT ALL PRIVILEGES ON mydb.* TO 'user'@'%';
```

## Examples

```php
// Robust connection with error details
function connectToDatabase(): PDO
{
    $dsn = 'mysql:host=' . getenv('DB_HOST') . ';'
         . 'dbname=' . getenv('DB_NAME') . ';'
         . 'port=' . (getenv('DB_PORT') ?: '3306') . ';'
         . 'charset=utf8mb4';

    try {
        $pdo = new PDO(
            $dsn,
            getenv('DB_USER'),
            getenv('DB_PASS'),
            [
                PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
                PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
                PDO::ATTR_EMULATE_PREPARES => false,
            ]
        );

        return $pdo;
    } catch (PDOException $e) {
        $info = $e->errorInfo;

        // Log detailed error (hide password in logs)
        error_log(sprintf(
            "DB Connection failed [%s@%s]: %s",
            getenv('DB_USER'),
            getenv('DB_HOST'),
            $info[2] ?? $e->getMessage()
        ));

        // Show user-friendly message
        if (str_contains($e->getMessage(), 'Access denied')) {
            throw new RuntimeException('Database connection failed: Invalid credentials');
        }

        throw new RuntimeException('Database connection failed');
    }
}

$pdo = connectToDatabase();
```

```php
// Connection with retry and fallback
function connectWithFallback(): PDO
{
    $configs = [
        ['host' => 'localhost', 'port' => '3306'],
        ['host' => '127.0.0.1', 'port' => '3306'],
        ['host' => 'db-primary.internal', 'port' => '3306'],
    ];

    foreach ($configs as $config) {
        try {
            $dsn = sprintf('mysql:host=%s;port=%s;dbname=%s', $config['host'], $config['port'], getenv('DB_NAME'));
            $pdo = new PDO($dsn, getenv('DB_USER'), getenv('DB_PASS'));
            error_log("Connected to DB at {$config['host']}");
            return $pdo;
        } catch (PDOException $e) {
            error_log("Failed to connect to {$config['host']}: " . $e->getMessage());
            continue;
        }
    }

    throw new RuntimeException('All database connections failed');
}
```

## Related Errors

- [pdo-connection-error.md](/content/languages/php/pdo-connection-error.md) — PDO connection failures
- [pdo-error.md](/content/languages/php/pdo-error.md) — General PDO errors
- [pdo-sqlstate-errors.md](/content/languages/php/pdo-sqlstate-errors.md) — SQLSTATE error reference
- [pdo-mysql-errno-1062.md](/content/languages/php/pdo-mysql-errno-1062.md) — MySQL duplicate entry error
