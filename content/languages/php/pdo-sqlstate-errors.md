---
title: "[Solution] PDO SQLSTATE Error Code Reference"
description: "Fix PDO SQLSTATE errors including HY000, 23000, 42S02. Check SQLSTATE codes, handle specific errors, use error info. Copy-paste solutions."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 230
---

# PDO SQLSTATE Error Code Reference

PDO uses SQLSTATE codes to identify database errors. These five-character codes follow the ANSI/ISO SQL standard and are returned by `PDO::errorCode()` and `PDO::errorInfo()`. Understanding SQLSTATE codes helps you diagnose and handle database errors systematically.

## Common Causes

```php
// HY000: General driver error
$stmt = $pdo->query("SELECT * FROM nonexistent_table");
// SQLSTATE[HY000]: General error
```

```php
// 23000: Integrity constraint violation
$stmt = $pdo->exec("INSERT INTO users (email) VALUES ('a@a.com')");
// SQLSTATE[23000]: Duplicate entry 'a@a.com' for key 'email'
```

```php
// 42S02: Base table or view not found
$stmt = $pdo->query("SELECT * FROM missing_table");
// SQLSTATE[42S02]: Table 'db.missing_table' doesn't exist
```

```php
// 42000: Syntax error or access violation
$stmt = $pdo->query("SELCT * FROM users");
// SQLSTATE[42000]: General SQL syntax error
```

```php
// HY090: Invalid driver ID
$pdo = new PDO("invalid_dsn");
// SQLSTATE[HY090]: Invalid driver ID
```

## How to Fix

### Fix 1: Check SQLSTATE Code With errorCode()

```php
try {
    $pdo = new PDO($dsn, $user, $pass);
    $stmt = $pdo->query("SELECT * FROM users");
} catch (PDOException $e) {
    $code = $pdo->errorCode();
    $info = $pdo->errorInfo();

    switch ($code) {
        case 'HY000':
            error_log("General error: " . $info[2]);
            break;
        case '23000':
            error_log("Constraint violation: " . $info[2]);
            break;
        case '42S02':
            error_log("Table not found: " . $info[2]);
            break;
        default:
            error_log("SQLSTATE $code: " . $info[2]);
    }
}
```

### Fix 2: Use errorInfo() for Detailed Messages

```php
function executeQuery(PDO $pdo, string $sql, array $params = []): ?PDOStatement
{
    try {
        $stmt = $pdo->prepare($sql);
        $stmt->execute($params);
        return $stmt;
    } catch (PDOException $e) {
        $errorInfo = $stmt->errorInfo();
        $sqlState = $errorInfo[0] ?? 'Unknown';
        $driverCode = $errorInfo[1] ?? 0;
        $message = $errorInfo[2] ?? $e->getMessage();

        error_log(sprintf(
            "PDO Error [SQLSTATE: %s, Driver: %d]: %s | SQL: %s",
            $sqlState,
            $driverCode,
            $message,
            $sql
        ));

        return null;
    }
}

$result = executeQuery($pdo, "SELECT * FROM users WHERE id = ?", [1]);
```

### Fix 3: Handle Common SQLSTATE Categories

```php
class PdoErrorHandler
{
    private const FATAL_STATES = ['HY000', 'HY090', '08006', '08001', '08004'];
    private const CONSTRAINT_STATES = ['23000', '23505', '23503', '23502'];
    private const SYNTAX_STATES = ['42000', '42601', '42P01'];

    public static function handleError(PDO $pdo, PDOException $e): string
    {
        $state = $pdo->errorCode();
        $info = $pdo->errorInfo();

        if (in_array($state, self::FATAL_STATES)) {
            return "FATAL [$state]: " . ($info[2] ?? $e->getMessage());
        }

        if (in_array($state, self::CONSTRAINT_STATES)) {
            return "CONSTRAINT [$state]: " . ($info[2] ?? $e->getMessage());
        }

        if (in_array($state, self::SYNTAX_STATES)) {
            return "SYNTAX [$state]: " . ($info[2] ?? $e->getMessage());
        }

        return "UNKNOWN [$state]: " . ($info[2] ?? $e->getMessage());
    }
}
```

### Fix 4: Retry Logic for Transient Errors

```php
function executeWithRetry(PDO $pdo, string $sql, array $params = [], int $maxRetries = 3): PDOStatement
{
    $attempt = 0;
    $transientStates = ['HY000', '08006', '08S01', '40001'];

    while ($attempt < $maxRetries) {
        try {
            $stmt = $pdo->prepare($sql);
            $stmt->execute($params);
            return $stmt;
        } catch (PDOException $e) {
            $state = $pdo->errorCode();
            $attempt++;

            if (!in_array($state, $transientStates) || $attempt >= $maxRetries) {
                throw $e;
            }

            usleep(pow(2, $attempt) * 100000); // Exponential backoff
        }
    }

    throw new RuntimeException("Max retries exceeded");
}
```

### Fix 5: Map SQLSTATE to Application Exceptions

```php
class SqlStateException extends RuntimeException
{
    private string $sqlState;
    private array $errorInfo;

    public function __construct(string $sqlState, array $errorInfo)
    {
        $this->sqlState = $sqlState;
        $this->errorInfo = $errorInfo;
        parent::__construct($errorInfo[2] ?? "SQLSTATE error: $sqlState");
    }

    public function getSqlState(): string { return $this->sqlState; }
    public function getErrorInfo(): array { return $this->errorInfo; }
}

function executeOrThrow(PDO $pdo, string $sql, array $params = []): PDOStatement
{
    try {
        $stmt = $pdo->prepare($sql);
        $stmt->execute($params);
        return $stmt;
    } catch (PDOException $e) {
        $state = $pdo->errorCode();
        $info = $pdo->errorInfo();
        throw new SqlStateException($state ?? 'HY000', $info);
    }
}

try {
    executeOrThrow($pdo, "INSERT INTO users (email) VALUES (?)", ['test@test.com']);
} catch (SqlStateException $e) {
    if ($e->getSqlState() === '23000') {
        echo "Email already exists";
    }
}
```

## Examples

```php
// Common SQLSTATE codes reference
$stateDescriptions = [
    'HY000' => 'General error',
    'HY001' => 'Memory allocation error',
    'HY090' => 'Invalid driver ID',
    '23000' => 'Integrity constraint violation',
    '23505' => 'Unique violation (PostgreSQL)',
    '23503' => 'Foreign key violation (PostgreSQL)',
    '42000' => 'Syntax error or access violation',
    '42S02' => 'Base table or view not found',
    '42P01' => 'Undefined table (PostgreSQL)',
    '08006' => 'Connection failure',
    '08S01' => 'Communication link failure',
    '40001' => 'Serialization failure',
    '57P01' => 'Admin shutdown (PostgreSQL)',
];

// Check error state
$stmt = $pdo->query("SELECT * FROM users");
if ($stmt === false) {
    $state = $pdo->errorCode();
    $desc = $stateDescriptions[$state] ?? 'Unknown error';
    error_log("Query failed [$state]: $desc");
}
```

```php
// Comprehensive error handler
function handleDbError(PDO $pdo, PDOException $e): void
{
    $state = $pdo->errorCode();
    $info = $pdo->errorInfo();

    $logMessage = sprintf(
        "[%s] SQLSTATE: %s | Code: %s | Message: %s",
        date('Y-m-d H:i:s'),
        $state,
        $info[1] ?? 'N/A',
        $info[2] ?? $e->getMessage()
    );

    error_log($logMessage);

    // Show user-friendly message based on error type
    if (in_array($state, ['23000', '23505'])) {
        http_response_code(409);
        echo json_encode(['error' => 'Data conflict']);
    } elseif ($state === '42S02') {
        http_response_code(500);
        echo json_encode(['error' => 'Configuration error']);
    } else {
        http_response_code(500);
        echo json_encode(['error' => 'Database error']);
    }
}
```

## Related Errors

- [pdo-error.md](/content/languages/php/pdo-error.md) — General PDO errors
- [pdo-connection-error.md](/content/languages/php/pdo-connection-error.md) — PDO connection failures
- [pdo-prepared-statement.md](/content/languages/php/pdo-prepared-statement.md) — PDO prepared statement issues
- [pdo-mysql-errno-1064.md](/content/languages/php/pdo-mysql-errno-1064.md) — MySQL 1064 syntax error
