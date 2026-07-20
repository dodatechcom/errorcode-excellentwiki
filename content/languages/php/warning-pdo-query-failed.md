---
title: "[Solution] PHP Warning: PDO::query() — Invalid Parameter Number"
description: "Fix PHP Warning: PDO::query() SQLSTATE[HY093] Invalid parameter number. Bind parameters correctly, check SQL syntax, verify count."
languages: ["php"]
severities: ["warning"]
error-types: ["runtime-error"]
weight: 104
---

# PHP Warning: PDO::query() — Invalid Parameter Number

This warning means the SQL query passed to PDO contains a mismatch between the number of placeholders (`:name` or `?`) and the actual values bound to it. PDO throws an `SQLSTATE[HY093]` error when parameter counts do not match.

## Common Causes

```php
// Cause 1: Mismatched placeholder count
<?php
$stmt = $pdo->prepare("SELECT * FROM users WHERE id = :id AND name = :name");
$stmt->execute([':id' => 1]); // Missing :name parameter
// SQLSTATE[HY093]: Invalid parameter number
?>
```

```php
// Cause 2: Wrong placeholder names
<?php
$stmt = $pdo->prepare("SELECT * FROM users WHERE id = :id");
$stmt->execute([':uid' => 1]); // Wrong key name
?>
```

```php
// Cause 3: Using numbered placeholders with named parameters
<?php
$stmt = $pdo->prepare("SELECT * FROM users WHERE id = ? AND name = ?");
$stmt->execute([':id' => 1, ':name' => 'Alice']); // Wrong format
?>
```

```php
// Cause 4: Extra placeholders in SQL
<?php
$stmt = $pdo->prepare("SELECT * FROM users WHERE id = :id AND status = :status");
$stmt->execute([':id' => 1]);
// :status is not bound
?>
```

```php
// Cause 5: Conditional placeholders
<?php
$sql = "SELECT * FROM users WHERE id = :id";
if ($includeEmail) {
    $sql .= " AND email = :email";
}
$stmt = $pdo->prepare($sql);
$params = [':id' => 1];
// :email is in SQL but not in params when $includeEmail is true
?>
```

## How to Fix

### Fix 1: Bind Parameters Correctly

Ensure every placeholder in the SQL statement has a corresponding value.

```php
<?php
$stmt = $pdo->prepare("SELECT * FROM users WHERE id = :id AND name = :name");

// All placeholders must be present
$stmt->execute([
    ':id'   => 1,
    ':name' => 'Alice',
]);

$user = $stmt->fetch();
?>
```

### Fix 2: Check SQL Syntax for Errors

Use named placeholders consistently and verify your SQL is well-formed.

```php
<?php
// WRONG — mixing placeholder types
$stmt = $pdo->prepare("SELECT * FROM users WHERE id = :id AND age > ?");
$stmt->execute([':id' => 1, 25]);

// CORRECT — use one type consistently
$stmt = $pdo->prepare("SELECT * FROM users WHERE id = :id AND age > :age");
$stmt->execute([':id' => 1, ':age' => 25]);
?>
```

### Fix 3: Verify Parameter Count

Count placeholders and parameters before executing.

```php
<?php
function executeSafe(\PDO $pdo, string $sql, array $params): \PDOStatement
{
    preg_match_all('/:(\w+)/', $sql, $matches);
    $placeholders = array_unique($matches[1]);

    $paramKeys = array_keys($params);
    $cleanKeys = array_map(function ($k) {
        return ltrim($k, ':');
    }, $paramKeys);

    $missing = array_diff($placeholders, $cleanKeys);
    $extra = array_diff($cleanKeys, $placeholders);

    if (!empty($missing)) {
        throw new \RuntimeException(
            "Missing parameters: " . implode(', ', $missing)
        );
    }
    if (!empty($extra)) {
        throw new \RuntimeException(
            "Extra parameters: " . implode(', ', $extra)
        );
    }

    $stmt = $pdo->prepare($sql);
    $stmt->execute($params);
    return $stmt;
}

$stmt = executeSafe(
    $pdo,
    "SELECT * FROM users WHERE id = :id AND name = :name",
    [':id' => 1, ':name' => 'Alice']
);
?>
```

### Fix 4: Use rowCount or bindValue for Dynamic Queries

Handle conditional parameters properly.

```php
<?php
$sql = "SELECT * FROM users WHERE id = :id";
$params = [':id' => 1];

if (!empty($email)) {
    $sql .= " AND email = :email";
    $params[':email'] = $email;
}

if (!empty($status)) {
    $sql .= " AND status = :status";
    $params[':status'] = $status;
}

$stmt = $pdo->prepare($sql);
$stmt->execute($params); // Only bound parameters are used
?>
```

## Examples

```php
<?php
// Safe CRUD operation with parameter validation
function createUser(\PDO $pdo, string $name, string $email, int $age): int
{
    $sql = "INSERT INTO users (name, email, age) VALUES (:name, :email, :age)";
    $stmt = $pdo->prepare($sql);
    $stmt->execute([
        ':name'  => $name,
        ':email' => $email,
        ':age'   => $age,
    ]);
    return (int) $pdo->lastInsertId();
}

function findUser(\PDO $pdo, int $id, ?string $status = null): ?array
{
    $sql = "SELECT * FROM users WHERE id = :id";
    $params = [':id' => $id];

    if ($status !== null) {
        $sql .= " AND status = :status";
        $params[':status'] = $status;
    }

    $stmt = $pdo->prepare($sql);
    $stmt->execute($params);
    $user = $stmt->fetch(PDO::FETCH_ASSOC);
    return $user ?: null;
}
?>
```

```php
<?php
// Bulk insert with parameter validation
function bulkInsert(\PDO $pdo, string $table, array $rows, array $columns): void
{
    $placeholders = [];
    $values = [];
    $i = 0;

    foreach ($rows as $row) {
        $rowPlaceholders = [];
        foreach ($columns as $col) {
            $key = ":col_{$i}_{$col}";
            $rowPlaceholders[] = $key;
            $values[$key] = $row[$col] ?? null;
        }
        $placeholders[] = '(' . implode(', ', $rowPlaceholders) . ')';
        $i++;
    }

    $sql = "INSERT INTO {$table} (" . implode(', ', $columns) . ") VALUES "
         . implode(', ', $placeholders);

    $stmt = $pdo->prepare($sql);
    $stmt->execute($values);
}
?>
```

## Related Errors

- [PHP PDO Connection Error](/languages/php/pdo-connection-error)
- [PHP PDO Query Error](/languages/php/pdo-error)
- [PHP PDO Prepared Statement Error](/languages/php/pdo-prepared-statement)
