---
title: "[Solution] PHP Deprecated: mysql_* Functions are Deprecated"
description: "Fix PHP Deprecated: mysql_* functions are deprecated. Migrate to mysqli or PDO, use prepared statements, update your database layer."
languages: ["php"]
severities: ["deprecated"]
error-types: ["runtime-error"]
weight: 108
---

# PHP Deprecated: mysql_* Functions are Deprecated

The `mysql_*` extension was deprecated in PHP 5.5 and removed in PHP 7.0. These functions (`mysql_connect`, `mysql_query`, `mysql_fetch_array`, etc.) do not support prepared statements and are vulnerable to SQL injection. You must migrate to `mysqli` or PDO.

## Common Causes

```php
// Cause 1: Using mysql_connect for database connections
<?php
$conn = mysql_connect("localhost", "user", "pass");
// Deprecated: mysql_connect()
?>
```

```php
// Cause 2: Using mysql_query directly
<?php
$result = mysql_query("SELECT * FROM users WHERE id = {$id}");
// Deprecated: mysql_query()
?>
```

```php
// Cause 3: Using mysql_fetch_array in loops
<?php
while ($row = mysql_fetch_array($result)) {
    echo $row['name'];
}
// Deprecated: mysql_fetch_array()
?>
```

```php
// Cause 4: Using mysql_real_escape_string for input sanitization
<?php
$safe = mysql_real_escape_string($userInput);
// Deprecated — should use prepared statements instead
?>
```

## How to Fix

### Fix 1: Migrate to PDO

PDO is the recommended database abstraction layer with support for multiple databases and prepared statements.

```php
<?php
// BEFORE (deprecated)
$conn = mysql_connect("localhost", "user", "pass");
mysql_select_db("mydb", $conn);
$result = mysql_query("SELECT * FROM users WHERE id = {$id}", $conn);
$row = mysql_fetch_assoc($result);

// AFTER — PDO
$dsn = "mysql:host=localhost;dbname=mydb;charset=utf8mb4";
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES   => false,
];

try {
    $pdo = new PDO($dsn, "user", "pass", $options);

    $stmt = $pdo->prepare("SELECT * FROM users WHERE id = :id");
    $stmt->execute([':id' => $id]);
    $row = $stmt->fetch();

    if ($row) {
        echo $row['name'];
    }
} catch (PDOException $e) {
    error_log("Database error: " . $e->getMessage());
    die("Database connection failed");
}
?>
```

### Fix 2: Migrate to mysqli

If you prefer a MySQL-specific extension, use mysqli with prepared statements.

```php
<?php
// BEFORE (deprecated)
$conn = mysql_connect("localhost", "user", "pass");
mysql_select_db("mydb", $conn);
$result = mysql_query("SELECT * FROM users WHERE email = '{$email}'", $conn);
$row = mysql_fetch_assoc($result);

// AFTER — mysqli with prepared statements
$conn = new mysqli("localhost", "user", "pass", "mydb");

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$conn->set_charset("utf8mb4");

$stmt = $conn->prepare("SELECT * FROM users WHERE email = ?");
$stmt->bind_param("s", $email); // "s" = string type
$stmt->execute();
$result = $stmt->get_result();
$row = $result->fetch_assoc();

if ($row) {
    echo $row['name'];
}

$stmt->close();
$conn->close();
?>
```

### Fix 3: Update Your Database Layer

Create a reusable database wrapper to centralize the migration.

```php
<?php
class Database
{
    private \PDO $pdo;

    public function __construct(string $dsn, string $user, string $pass)
    {
        $this->pdo = new PDO($dsn, $user, $pass, [
            PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
            PDO::ATTR_EMULATE_PREPARES   => false,
        ]);
    }

    public function query(string $sql, array $params = []): array
    {
        $stmt = $this->pdo->prepare($sql);
        $stmt->execute($params);
        return $stmt->fetchAll();
    }

    public function insert(string $table, array $data): string
    {
        $columns = implode(', ', array_keys($data));
        $placeholders = implode(', ', array_fill(0, count($data), '?'));

        $sql = "INSERT INTO {$table} ({$columns}) VALUES ({$placeholders})";
        $stmt = $this->pdo->prepare($sql);
        $stmt->execute(array_values($data));

        return $this->pdo->lastInsertId();
    }

    public function update(string $table, array $data, string $where, array $whereParams = []): int
    {
        $set = implode(', ', array_map(fn($col) => "{$col} = ?", array_keys($data)));
        $sql = "UPDATE {$table} SET {$set} WHERE {$where}";

        $stmt = $this->pdo->prepare($sql);
        $stmt->execute(array_merge(array_values($data), $whereParams));
        return $stmt->rowCount();
    }
}

// Usage
$db = new Database("mysql:host=localhost;dbname=mydb", "user", "pass");
$users = $db->query("SELECT * FROM users WHERE status = ?", ["active"]);
$id = $db->insert("users", ["name" => "Alice", "email" => "alice@example.com"]);
?>
```

### Fix 4: Search and Replace All mysql_* Calls

Use a systematic approach to find and replace all deprecated calls.

```php
<?php
// Migration mapping: mysql_* -> mysqli_*
$migrationMap = [
    'mysql_connect'       => 'mysqli_connect',
    'mysql_select_db'     => 'mysqli_select_db',
    'mysql_query'         => 'mysqli_query',
    'mysql_fetch_assoc'   => 'mysqli_fetch_assoc',
    'mysql_fetch_array'   => 'mysqli_fetch_array',
    'mysql_fetch_row'     => 'mysqli_fetch_row',
    'mysql_num_rows'      => 'mysqli_num_rows',
    'mysql_real_escape_string' => 'mysqli_real_escape_string',
    'mysql_close'         => 'mysqli_close',
    'mysql_error'         => 'mysqli_error',
    'mysql_insert_id'     => 'mysqli_insert_id',
];

// But prefer PDO over mysqli for new code
// Search your codebase:
// grep -rn "mysql_" --include="*.php" .
?>
```

## Examples

```php
<?php
// Complete before/after migration example
// === BEFORE (deprecated mysql_*) ===
/*
$conn = mysql_connect("localhost", "root", "");
mysql_select_db("shop", $conn);

$result = mysql_query("SELECT * FROM products WHERE price > {$minPrice}", $conn);
while ($row = mysql_fetch_assoc($result)) {
    echo "{$row['name']}: \${$row['price']}\n";
}
$count = mysql_num_rows($result);
mysql_close($conn);
*/

// === AFTER (PDO with prepared statements) ===
$dsn = "mysql:host=localhost;dbname=shop;charset=utf8mb4";
$pdo = new PDO($dsn, "root", "", [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
]);

$stmt = $pdo->prepare("SELECT * FROM products WHERE price > :min_price");
$stmt->execute([':min_price' => $minPrice]);
$products = $stmt->fetchAll();

foreach ($products as $product) {
    echo "{$product['name']}: \${$product['price']}\n";
}

echo count($products) . " products found";
?>
```

## Related Errors

- [PHP PDO Connection Error](/languages/php/pdo-connection-error)
- [PHP PDO Query Error](/languages/php/warning-pdo-query-failed)
- [PHP Deprecated: create_function()](/languages/php/warning-deprecated-create-function)
