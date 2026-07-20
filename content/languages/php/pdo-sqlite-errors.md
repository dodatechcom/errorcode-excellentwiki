---
title: "[Solution] SQLite PDO Errors — Database Locked and Permissions"
description: "Fix SQLite PDO errors including database locked, busy timeout, WAL mode issues. Check permissions and handle concurrency. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 236
---

# SQLite PDO Errors — Database Locked and Permissions

SQLite PDO errors commonly involve database locking, permission issues, and WAL mode complications. SQLite uses file-level locking which can cause "database is locked" errors during concurrent access from multiple processes or requests.

## Common Causes

```php
// Database locked by another process
$stmt = $pdo->query("INSERT INTO users (name) VALUES ('John')");
// SQLSTATE[HY000]: General error: 5 database is locked
```

```php
// Insufficient file permissions
$pdo = new PDO('sqlite:/var/data/app.db');
// SQLSTATE[HY000]: unable to open database file
```

```php
// Long-running write blocks readers
$pdo->exec("BEGIN TRANSACTION");
$pdo->exec("UPDATE users SET status = 'active' WHERE id > 0");
// Other queries block until transaction completes
```

```php
// Multiple concurrent writes to WAL database
$pdo1 = new PDO('sqlite:app.db');
$pdo2 = new PDO('sqlite:app.db');
$pdo1->exec("INSERT INTO logs (msg) VALUES ('a')");
$pdo2->exec("INSERT INTO logs (msg) VALUES ('b')"); // May fail
```

```php
// Database file on read-only filesystem
$pdo = new PDO('sqlite:/readonly/path/app.db');
// Cannot create or write to database
```

## How to Fix

### Fix 1: Set Busy Timeout

```php
$pdo = new PDO('sqlite:' . $dbPath);
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

// Wait up to 5 seconds before failing
$pdo->exec('PRAGMA busy_timeout = 5000');
```

### Fix 2: Enable WAL Mode for Better Concurrency

```php
$pdo = new PDO('sqlite:' . $dbPath);
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

// Enable WAL (Write-Ahead Logging) mode
$pdo->exec('PRAGMA journal_mode = WAL');
$pdo->exec('PRAGMA synchronous = NORMAL');

// WAL mode allows concurrent reads while writing
```

### Fix 3: Check and Set File Permissions

```php
function openSqliteDatabase(string $dbPath): PDO
{
    $dir = dirname($dbPath);

    if (!is_dir($dir)) {
        if (!mkdir($dir, 0755, true)) {
            throw new RuntimeException("Cannot create directory: $dir");
        }
    }

    if (!is_writable($dir)) {
        throw new RuntimeException("Directory not writable: $dir");
    }

    // Check if file exists and is readable
    if (file_exists($dbPath) && !is_readable($dbPath)) {
        throw new RuntimeException("Database file not readable: $dbPath");
    }

    $pdo = new PDO("sqlite:$dbPath");
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $pdo->exec('PRAGMA busy_timeout = 5000');
    $pdo->exec('PRAGMA journal_mode = WAL');

    return $pdo;
}

$pdo = openSqliteDatabase('/var/data/app.db');
```

### Fix 4: Use Transactions for Batch Operations

```php
function batchInsert(PDO $pdo, string $table, array $rows): int
{
    $pdo->exec('PRAGMA busy_timeout = 10000');
    $pdo->beginTransaction();

    $columns = array_keys($rows[0]);
    $placeholders = implode(', ', array_fill(0, count($columns), '?'));
    $columnsList = implode(', ', $columns);

    $stmt = $pdo->prepare("INSERT INTO $table ($columnsList) VALUES ($placeholders)");

    $count = 0;
    foreach ($rows as $row) {
        $stmt->execute(array_values($row));
        $count++;
    }

    $pdo->commit();
    return $count;
}

$count = batchInsert($pdo, 'users', [
    ['name' => 'Alice', 'email' => 'alice@test.com'],
    ['name' => 'Bob', 'email' => 'bob@test.com'],
]);
```

### Fix 5: Handle Database Locked With Retry

```php
function executeWithRetry(PDO $pdo, string $sql, array $params = [], int $maxRetries = 3): PDOStatement
{
    $attempt = 0;

    while ($attempt < $maxRetries) {
        try {
            $stmt = $pdo->prepare($sql);
            $stmt->execute($params);
            return $stmt;
        } catch (PDOException $e) {
            $attempt++;

            if ($e->getCode() === 'HY000' && str_contains($e->getMessage(), 'database is locked')) {
                if ($attempt < $maxRetries) {
                    usleep(pow(2, $attempt) * 100000); // Exponential backoff
                    continue;
                }
            }

            throw $e;
        }
    }

    throw new RuntimeException("Max retries exceeded");
}
```

## Examples

```php
// Production SQLite configuration
function initSqliteDb(string $dbPath): PDO
{
    $pdo = new PDO("sqlite:$dbPath");
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);

    // Performance optimizations
    $pdo->exec('PRAGMA journal_mode = WAL');
    $pdo->exec('PRAGMA synchronous = NORMAL');
    $pdo->exec('PRAGMA busy_timeout = 5000');
    $pdo->exec('PRAGMA cache_size = -64000'); // 64MB cache
    $pdo->exec('PRAGMA foreign_keys = ON');
    $pdo->exec('PRAGMA temp_store = MEMORY');

    return $pdo;
}

$pdo = initSqliteDb(__DIR__ . '/data/app.db');
```

```php
// Thread-safe SQLite operations
class SqliteRepository
{
    private PDO $pdo;

    public function __construct(string $dbPath)
    {
        $this->pdo = new PDO("sqlite:$dbPath");
        $this->pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $this->pdo->exec('PRAGMA busy_timeout = 5000');
        $this->pdo->exec('PRAGMA journal_mode = WAL');
    }

    public function upsert(string $table, array $data, string $conflictColumn): bool
    {
        $columns = array_keys($data);
        $placeholders = implode(', ', array_fill(0, count($columns), '?'));
        $columnsList = implode(', ', $columns);
        $updateList = implode(', ', array_map(fn($c) => "$c = excluded.$c", $columns));

        $sql = "INSERT INTO $table ($columnsList) VALUES ($placeholders)
                ON CONFLICT($conflictColumn) DO UPDATE SET $updateList";

        $stmt = $this->pdo->prepare($sql);
        return $stmt->execute(array_values($data));
    }
}

$repo = new SqliteRepository('/var/data/app.db');
$repo->upsert('users', ['email' => 'john@test.com', 'name' => 'John'], 'email');
```

## Related Errors

- [pdo-connection-error.md](/content/languages/php/pdo-connection-error.md) — PDO connection failures
- [pdo-error.md](/content/languages/php/pdo-error.md) — General PDO errors
- [file-lock-error.md](/content/languages/php/file-lock-error.md) — File lock errors
- [pdo-transaction-error.md](/content/languages/php/pdo-transaction-error.md) — PDO transaction errors
