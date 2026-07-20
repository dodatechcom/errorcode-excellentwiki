---
title: "[Solution] PostgreSQL PDO Errors — Connection and SQLSTATE Issues"
description: "Fix PostgreSQL PDO errors. Check connection strings, handle PostgreSQL-specific SQLSTATE codes, verify pg_hba.conf. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 237
---

# PostgreSQL PDO Errors — Connection and SQLSTATE Issues

PostgreSQL PDO errors include connection failures, authentication issues, and PostgreSQL-specific SQLSTATE codes. Common problems involve incorrect DSN strings, pg_hba.conf configuration, SSL requirements, and PostgreSQL-specific syntax differences from MySQL.

## Common Causes

```php
// Wrong DSN format for PostgreSQL
$pdo = new PDO('pgsql:host=localhost;dbname=mydb', 'user', 'pass');
// SQLSTATE[08006]: could not connect to server
```

```php
// pg_hba.conf rejects connection
$pdo = new PDO('pgsql:host=192.168.1.100;dbname=mydb', 'user', 'pass');
// FATAL: no pg_hba.conf entry for host "192.168.1.100"
```

```php
// SSL required but not configured
$pdo = new PDO('pgsql:host=localhost;dbname=mydb;sslmode=require', 'user', 'pass');
// FATAL: no pg_hba.conf entry for SSL connection
```

```php
// PostgreSQL-specific syntax error
$stmt = $pdo->query("SELECT * FROM users LIMIT 1, 10"); // MySQL syntax
// ERROR: syntax error at or near ","
```

```php
// Wrong port or database name
$pdo = new PDO('pgsql:host=localhost;port=5433;dbname=wrongdb', 'user', 'pass');
// FATAL: database "wrongdb" does not exist
```

## How to Fix

### Fix 1: Use Correct PostgreSQL DSN Format

```php
// PostgreSQL DSN format
$dsn = 'pgsql:host=localhost;port=5432;dbname=mydb;options=\'--client_encoding=utf8\'';
$pdo = new PDO($dsn, 'user', 'pass');
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

// Alternative: Use connection string
$dsn = 'pgsql:dbname=mydb host=localhost port=5432';
```

### Fix 2: Verify pg_hba.conf Configuration

```bash
# Find pg_hba.conf location
sudo -u postgres psql -c "SHOW hba_file"

# Add entry for your user/host
# TYPE  DATABASE  USER  ADDRESS       METHOD
# host  mydb      user  192.168.1.0/24 md5
# host  mydb      user  127.0.0.1/32  md5

# Reload PostgreSQL config
sudo systemctl reload postgresql
```

### Fix 3: Handle SSL Connections

```php
// With SSL
$dsn = 'pgsql:host=localhost;port=5432;dbname=mydb;sslmode=require';
$pdo = new PDO($dsn, 'user', 'pass', [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::PGSQL_ATTR_SSL_CERT => '/path/to/client.crt',
    PDO::PGSQL_ATTR_SSL_KEY => '/path/to/client.key',
    PDO::PGSQL_ATTR_SSL_ROOT_CERT => '/path/to/root.crt',
]);

// Without SSL (if allowed)
$dsn = 'pgsql:host=localhost;port=5432;dbname=mydb;sslmode=disable';
```

### Fix 4: Use PostgreSQL-Compatible Syntax

```php
// Instead of MySQL LIMIT offset, count syntax:
// WRONG: LIMIT 10 OFFSET 5 (MySQL style)
// CORRECT: PostgreSQL uses same syntax but with different features

// PostgreSQL specific features:
$stmt = $pdo->query("SELECT * FROM users ORDER BY id LIMIT 10 OFFSET 5");

// PostgreSQL UPSERT
$stmt = $pdo->prepare("
    INSERT INTO users (email, name)
    VALUES (:email, :name)
    ON CONFLICT (email)
    DO UPDATE SET name = EXCLUDED.name
");
$stmt->execute([':email' => 'john@test.com', ':name' => 'John']);

// PostgreSQL array parameters
$stmt = $pdo->prepare("SELECT * FROM users WHERE id = ANY(:ids::int[])");
$stmt->execute([':ids' => '{1,2,3}']);
```

### Fix 5: Comprehensive PostgreSQL Error Handler

```php
class PostgresErrorHandler
{
    private const PG_ERRORS = [
        '08000' => 'Connection exception',
        '08003' => 'Connection does not exist',
        '08006' => 'Connection failure',
        '23000' => 'Integrity constraint violation',
        '23505' => 'Unique violation',
        '23503' => 'Foreign key violation',
        '42000' => 'Syntax error or access rule violation',
        '42601' => 'Syntax error',
        '42P01' => 'Undefined table',
        '42P02' => 'Undefined parameter',
        '57P01' => 'Admin shutdown',
        '57P02' => 'Crash shutdown',
        '57P03' => 'Cannot connect now',
        '40001' => 'Serialization failure',
        '40P01' => 'Deadlock detected',
    ];

    public static function handleError(PDO $pdo, PDOException $e): string
    {
        $state = $pdo->errorCode();
        $info = $pdo->errorInfo();

        $description = self::PG_ERRORS[$state] ?? 'Unknown error';
        $message = $info[2] ?? $e->getMessage();

        return sprintf("PostgreSQL [%s] %s: %s", $state, $description, $message);
    }

    public static function isRetryable(string $state): bool
    {
        return in_array($state, ['40001', '40P01', '57P03', '08006']);
    }
}
```

## Examples

```php
// Production PostgreSQL connection
function connectPostgres(): PDO
{
    $dsn = sprintf(
        'pgsql:host=%s;port=%s;dbname=%s;options=--client_encoding=utf8',
        getenv('PG_HOST') ?: 'localhost',
        getenv('PG_PORT') ?: '5432',
        getenv('PG_DBNAME') ?: 'myapp'
    );

    $options = [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        PDO::ATTR_EMULATE_PREPARES => false,
    ];

    // Add SSL if required
    if (getenv('PG_SSLMODE') === 'require') {
        $dsn .= ';sslmode=require';
    }

    $pdo = new PDO($dsn, getenv('PG_USER'), getenv('PG_PASS'), $options);

    // Set PostgreSQL-specific settings
    $pdo->exec("SET client_encoding = 'UTF8'");
    $pdo->exec("SET timezone = 'UTC'");

    return $pdo;
}

$pdo = connectPostgres();
```

```php
// PostgreSQL query with retry logic
function pgQueryWithRetry(PDO $pdo, string $sql, array $params = [], int $maxRetries = 3): PDOStatement
{
    $attempt = 0;

    while ($attempt < $maxRetries) {
        try {
            $stmt = $pdo->prepare($sql);
            $stmt->execute($params);
            return $stmt;
        } catch (PDOException $e) {
            $state = $pdo->errorCode();
            $attempt++;

            if (PostgresErrorHandler::isRetryable($state) && $attempt < $maxRetries) {
                usleep(pow(2, $attempt) * 100000);
                continue;
            }

            throw $e;
        }
    }

    throw new RuntimeException("Max retries exceeded");
}
```

```php
// PostgreSQL-specific features with PDO
function advancedPgQuery(PDO $pdo): array
{
    // Use RETURNING clause
    $stmt = $pdo->prepare("
        INSERT INTO users (email, name)
        VALUES (:email, :name)
        RETURNING id, created_at
    ");
    $stmt->execute([':email' => 'john@test.com', ':name' => 'John']);
    $result = $stmt->fetch();

    // Use CTE (Common Table Expressions)
    $stmt = $pdo->query("
        WITH active_users AS (
            SELECT id, name, email
            FROM users
            WHERE status = 'active'
        )
        SELECT * FROM active_users
        WHERE email LIKE '%@test.com'
    ");

    return $stmt->fetchAll();
}
```

## Related Errors

- [pdo-connection-error.md](/content/languages/php/pdo-connection-error.md) — PDO connection failures
- [pdo-sqlstate-errors.md](/content/languages/php/pdo-sqlstate-errors.md) — SQLSTATE error reference
- [pdo-error.md](/content/languages/php/pdo-error.md) — General PDO errors
- [pdo-mysql-errno-1045.md](/content/languages/php/pdo-mysql-errno-1045.md) — MySQL access denied
