---
title: "[Solution] PDO Emulated Prepares — Limitations and Issues"
description: "Fix PDO emulated prepares issues. Set ATTR_EMULATE_PREPARES, understand limitations, use native prepares. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 231
---

# PDO Emulated Prepares — Limitations and Issues

PDO emulated prepares perform parameter binding at the client level instead of sending prepared statements to the database server. While faster in some cases, emulated prepares have limitations with data types, character encoding, and query features that can cause subtle bugs and security concerns.

## Common Causes

```php
// Emulated prepare truncates binary data
$stmt = $pdo->prepare("INSERT INTO files (data) VALUES (?)");
$stmt->execute([$binaryData]); // Binary data may be corrupted
```

```php
// LIMIT with emulated prepares requires casting
$stmt = $pdo->prepare("SELECT * FROM users LIMIT ?");
$stmt->execute([$limit]); // May fail: bound as string, not integer
```

```php
// Emulated prepares don't support multi-row VALUES
$stmt = $pdo->prepare("INSERT INTO users (name, email) VALUES (?, ?)");
foreach ($users as $user) {
    $stmt->execute([$user['name'], $user['email']]); // New prepare each time
}
```

```php
// Character encoding mismatch with emulated prepares
$pdo->exec("SET NAMES utf8mb4");
$stmt = $pdo->prepare("INSERT INTO posts (content) VALUES (?)");
// Emulated prepare may not respect character encoding properly
```

```php
// Last insert ID may not work with emulated prepares
$stmt = $pdo->prepare("INSERT INTO users (name) VALUES (?)");
$stmt->execute(['John']);
$id = $pdo->lastInsertId(); // May return 0 or wrong value
```

## How to Fix

### Fix 1: Enable Native Server-Side Prepares

```php
// Disable emulated prepares
$pdo->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);

// Verify
$emulated = $pdo->getAttribute(PDO::ATTR_EMULATE_PREPARES);
error_log("Emulated prepares: " . ($emulated ? 'ON' : 'OFF'));
```

### Fix 2: Handle Data Type Issues With Explicit Casting

```php
// With emulated prepares, bind parameters with explicit types
$stmt = $pdo->prepare("SELECT * FROM users LIMIT :limit");
$stmt->bindValue(':limit', (int) $limit, PDO::PARAM_INT);
$stmt->execute();

// Or use type hints in prepare
$stmt = $pdo->prepare("SELECT * FROM users WHERE id = :id AND status = :status");
$stmt->bindValue(':id', $id, PDO::PARAM_INT);
$stmt->bindValue(':status', $status, PDO::PARAM_STR);
$stmt->execute();
```

### Fix 3: Batch Insert Without Emulated Prepare Issues

```php
// Build batch insert manually to avoid per-row prepare
function batchInsert(PDO $pdo, string $table, array $rows): int
{
    if (empty($rows)) {
        return 0;
    }

    $columns = array_keys($rows[0]);
    $placeholders = [];
    $values = [];

    foreach ($rows as $row) {
        $rowPlaceholders = [];
        foreach ($columns as $col) {
            $rowPlaceholders[] = ':' . $col . '_' . count($placeholders);
            $values[':' . $col . '_' . count($placeholders)] = $row[$col] ?? null;
        }
        $placeholders[] = '(' . implode(', ', $rowPlaceholders) . ')';
    }

    $sql = sprintf(
        "INSERT INTO %s (%s) VALUES %s",
        $table,
        implode(', ', $columns),
        implode(', ', $placeholders)
    );

    $stmt = $pdo->prepare($sql);
    $stmt->execute($values);
    return $stmt->rowCount();
}
```

### Fix 4: Use Native Prepares for Complex Queries

```php
// For complex queries with specific needs, disable emulated prepares
$pdo->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);

// Native prepare works better with:
// - JSON columns
// - Binary data
// - Large TEXT fields
// - Multiple statements
// - Stored procedures

$stmt = $pdo->prepare("
    INSERT INTO documents (id, content, metadata)
    VALUES (:id, :content, CAST(:metadata AS JSON))
");
$stmt->execute([
    ':id' => $docId,
    ':content' => $content,
    ':metadata' => json_encode($meta),
]);
```

### Fix 5: Configuration for Production

```php
function createProductionPdo(string $dsn, string $user, string $pass): PDO
{
    $pdo = new PDO($dsn, $user, $pass, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        PDO::ATTR_EMULATE_PREPARES => false, // Use native prepares
        PDO::MYSQL_ATTR_INIT_COMMAND => "SET NAMES utf8mb4 COLLATE utf8mb4_unicode_ci",
    ]);

    // Verify native prepares are enabled
    if ($pdo->getAttribute(PDO::ATTR_EMULATE_PREPARES)) {
        $pdo->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);
    }

    return $pdo;
}

$pdo = createProductionPdo($dsn, $user, $pass);
```

## Examples

```php
// Comparison: emulated vs native prepares
$pdo->setAttribute(PDO::ATTR_EMULATE_PREPARES, true);

// Emulated: PHP sends complete query with bound values
$stmt = $pdo->prepare("SELECT * FROM users WHERE created > ?");
$stmt->execute(['2024-01-01']);

$pdo->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);

// Native: PHP sends PREPARE statement, then EXECUTE
$stmt = $pdo->prepare("SELECT * FROM users WHERE created > ?");
$stmt->execute(['2024-01-01']);
```

```php
// Detect and handle prepare limitations
function safePrepare(PDO $pdo, string $sql, array $params = []): PDOStatement
{
    $emulated = $pdo->getAttribute(PDO::ATTR_EMULATE_PREPARES);

    if ($emulated) {
        // Check for known emulated prepare issues
        if (preg_match('/LIMIT\s+?$/i', trim($sql))) {
            // LIMIT without bound parameter type may fail
            $sql = preg_replace('/LIMIT\s+?$/i', 'LIMIT ?', $sql);
        }
    }

    $stmt = $pdo->prepare($sql);

    if ($emulated) {
        // Bind parameters with explicit types
        foreach ($params as $key => $value) {
            $param = is_int($key) ? $key + 1 : $key;
            $type = is_int($value) ? PDO::PARAM_INT : PDO::PARAM_STR;
            $stmt->bindValue($param, $value, $type);
        }
        $stmt->execute();
    } else {
        $stmt->execute($params);
    }

    return $stmt;
}
```

```php
// Test emulated vs native prepare behavior
function testPrepareModes(PDO $pdo): void
{
    $pdo->setAttribute(PDO::ATTR_EMULATE_PREPARES, true);
    $emulatedResult = testQuery($pdo, "SELECT 1 + 1");

    $pdo->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);
    $nativeResult = testQuery($pdo, "SELECT 1 + 1");

    echo "Emulated: " . ($emulatedResult ? 'OK' : 'FAIL') . PHP_EOL;
    echo "Native: " . ($nativeResult ? 'OK' : 'FAIL') . PHP_EOL;

    // Restore default
    $pdo->setAttribute(PDO::ATTR_EMULATE_PREPARES, true);
}

function testQuery(PDO $pdo, string $sql): bool
{
    try {
        $stmt = $pdo->prepare($sql);
        return $stmt->execute() !== false;
    } catch (PDOException $e) {
        return false;
    }
}
```

## Related Errors

- [pdo-prepared-statement.md](/content/languages/php/pdo-prepared-statement.md) — PDO prepared statement issues
- [pdo-error.md](/content/languages/php/pdo-error.md) — General PDO errors
- [pdo-column-error.md](/content/languages/php/pdo-column-error.md) — PDO column binding errors
- [pdo-connection-error.md](/content/languages/php/pdo-connection-error.md) — PDO connection failures
