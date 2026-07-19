---
title: "[Solution] PHP PDO Quote Error"
description: "Fix PHP PDO SQLSTATE[HY000] Quote error. Learn to handle string escaping and quoting failures."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "php"
tags: ["php", "pdo", "database", "quote", "escaping", "sql-injection"]
severity: "error"
---

# SQLSTATE[HY000] Quote Error

## Error Message

```
SQLSTATE[HY000] General error in quote()
```

## Common Causes

- The PDO driver does not support the quote() method
- The database connection has been lost before calling quote()
- The input string contains special characters that cause encoding issues
- Using quote() for values when prepared statements should be used instead

## Solutions

### Solution 1: Use Prepared Statements Instead of quote()

Prepared statements with parameter binding are always preferred over manual quoting for security and reliability.

```php
<?php
// WRONG: Manual quoting (prone to errors and less secure)
$name = $pdo->quote($_POST['name']);
$sql = "SELECT * FROM users WHERE name = {$name}";

// CORRECT: Use prepared statements with parameter binding
$stmt = $pdo->prepare('SELECT * FROM users WHERE name = :name AND email = :email');
$stmt->execute([
    ':name' => $_POST['name'],
    ':email' => $_POST['email'],
]);
$user = $stmt->fetch(PDO::FETCH_ASSOC);

// For dynamic table/column names, use an allowlist
$allowedColumns = ['name', 'email', 'created_at', 'status'];
$sortBy = in_array($_GET['sort'] ?? '', $allowedColumns, true) ? $_GET['sort'] : 'created_at';

$stmt = $pdo->prepare("SELECT * FROM users ORDER BY {$sortBy} DESC");
$stmt->execute();
```

### Solution 2: Handle quote() for Drivers That Do Not Support It

Check if your PDO driver supports quote() and implement a fallback using addslashes() or prepared statements.

```php
<?php
function safeQuote(PDO $pdo, string $value): string
{
    // PDO::quote() may not be supported by all drivers
    try {
        $quoted = $pdo->quote($value);
        if ($quoted !== false) {
            return $quoted;
        }
    } catch (PDOException) {
        // quote() is not supported by this driver
    }

    // Fallback: use parameterized queries instead
    // This is a wrapper that signals to use prepared statements
    throw new RuntimeException(
        'PDO::quote() is not supported by this driver. Use prepared statements instead.'
    );
}

// Better approach: Build a query builder that always uses parameter binding
class QueryBuilder
{
    private PDO $pdo;

    public function __construct(PDO $pdo)
    {
        $this->pdo = $pdo;
    }

    public function selectWhere(string $table, array $conditions): array
    {
        $where = [];
        $params = [];
        foreach ($conditions as $column => $value) {
            $where[] = "{$column} = :{$column}";
            $params[":{$column}"] = $value;
        }

        $sql = "SELECT * FROM {$table} WHERE " . implode(' AND ', $where);
        $stmt = $this->pdo->prepare($sql);
        $stmt->execute($params);
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }
}
```

### Solution 3: Handle Multibyte String Quoting Issues

Ensure proper character set configuration to prevent quoting issues with multibyte strings like UTF-8.

```php
<?php
// Configure character set to prevent encoding-related quoting errors
$pdo = new PDO($dsn, $user, $pass, [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::MYSQL_ATTR_INIT_COMMAND => "SET NAMES utf8mb4 COLLATE utf8mb4_unicode_ci",
]);

// Handle strings with special multibyte characters safely
function insertWithUnicode(PDO $pdo, string $table, array $data): int
{
    $columns = array_keys($data);
    $placeholders = array_map(fn($col) => ":{$col}", $columns);

    $sql = sprintf(
        'INSERT INTO %s (%s) VALUES (%s)',
        $table,
        implode(', ', $columns),
        implode(', ', $placeholders)
    );

    $stmt = $pdo->prepare($sql);

    // PDO handles UTF-8 encoding automatically with prepared statements
    foreach ($data as $key => $value) {
        $stmt->bindValue(":{$key}", $value, PDO::PARAM_STR);
    }

    $stmt->execute();
    return (int) $pdo->lastInsertId();
}

// Usage with unicode content
$insertId = insertWithUnicode($pdo, 'articles', [
    'title' => 'Ünïcödé Tëst: 日本語テスト',
    'body' => '内容を含む記事本文 — с русским текстом',
    'lang' => 'multi',
]);
```

## Prevention Tips

- Never rely on quote() for SQL injection prevention; always use prepared statements with bound parameters
- Set the connection charset in the DSN string (e.g., charset=utf8mb4) to prevent encoding issues
- If quote() is not supported, build queries exclusively with parameter binding

## Related Errors

- [PHP PDOException: SQLSTATE[HY000]]({{< relref "/languages/php/pdo-error" >}})
- [PHP PDO Prepare Statement Error]({{< relref "/languages/php/pdo-prepared-statement" >}})
- [PHP PDO Set Attribute Error]({{< relref "/languages/php/pdo-set-attribute" >}})
