---
title: "[Solution] PHP mysql_* Deprecated — Replace with mysqli_* Migration"
description: "Replace deprecated mysql_* functions with mysqli_* in PHP. Complete migration guide with prepared statements and PDO alternatives."
deprecated_function: "mysql_*"
replacement_function: "mysqli_*"
languages: ["php"]
deprecated_since: "PHP 5.5"
removed_in: "PHP 7.0"
error_message: "Call to undefined function mysql_connect()"
tags: ["mysql", "mysqli", "database", "pdo"]
weight: 40
---

# [Solution] PHP mysql_* Deprecated — Replace with mysqli_* Migration

The original `mysql_*` extension was deprecated in PHP 5.5 and removed in PHP 7.0. It was replaced by `mysqli_*` (MySQL Improved) and PDO (PHP Data Objects), both of which support prepared statements, which are critical for preventing SQL injection. Migrating is mandatory — your code will not run on PHP 7.0+ without updating.

## What You'll See

On PHP 7.0+:

```
Fatal error: Uncaught Error: Call to undefined function mysql_connect()
```

On PHP 5.5 through 5.6 (deprecated mode):

```
Deprecated: mysql_connect(): The mysql extension is deprecated and will be removed in the future: use mysqli or PDO instead in /path/to/script.php on line X
```

## Why Deprecated

The `mysql_*` extension was removed for several critical reasons:

- **No prepared statements**: Without prepared statements, every query required manual escaping, which developers frequently forgot, leading to SQL injection vulnerabilities.
- **Not maintained**: The extension had not received updates for years and was incompatible with modern MySQL features.
- **Security**: Prepared statements via `mysqli` or PDO provide parametrized queries that inherently prevent injection attacks.
- **Features**: `mysqli` supports transactions, multiple statements, and improved error handling.

## Old Code (Deprecated)

```php
// Connection
$conn = mysql_connect("localhost", "user", "password");
mysql_select_db("mydb", $conn);

// Simple query
$result = mysql_query("SELECT * FROM users WHERE id = 1", $conn);
$row = mysql_fetch_assoc($result);
echo $row['name'];

// Insert with manual escaping (SQL injection risk)
$name = $_POST['name'];
$query = "INSERT INTO users (name) VALUES ('" . mysql_real_escape_string($name) . "')";
mysql_query($query, $conn);

// Row count
$count = mysql_num_rows($result);

// Free result
mysql_free_result($result);

// Close connection
mysql_close($conn);
```

## New Code — mysqli_* Approach

```php
// Connection (object-oriented)
$conn = new mysqli("localhost", "user", "password", "mydb");

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Simple query
$result = $conn->query("SELECT * FROM users WHERE id = 1");
$row = $result->fetch_assoc();
echo $row['name'];

// Insert with prepared statement (SQL injection safe)
$stmt = $conn->prepare("INSERT INTO users (name) VALUES (?)");
$stmt->bind_param("s", $_POST['name']);
$stmt->execute();
$stmt->close();

// Row count
$count = $result->num_rows;

// Free result
$result->free();

// Close connection
$conn->close();
```

## New Code — PDO Approach (Recommended)

```php
// Connection
$pdo = new PDO(
    "mysql:host=localhost;dbname=mydb;charset=utf8mb4",
    "user",
    "password",
    [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        PDO::ATTR_EMULATE_PREPARES => false,
    ]
);

// Simple query
$stmt = $pdo->query("SELECT * FROM users WHERE id = 1");
$row = $stmt->fetch();
echo $row['name'];

// Insert with prepared statement
$stmt = $pdo->prepare("INSERT INTO users (name) VALUES (:name)");
$stmt->execute(['name' => $_POST['name']]);

// Fetch all rows
$stmt = $pdo->query("SELECT * FROM users WHERE active = 1");
$rows = $stmt->fetchAll();

// Using transaction
$pdo->beginTransaction();
try {
    $pdo->exec("UPDATE accounts SET balance = balance - 100 WHERE id = 1");
    $pdo->exec("UPDATE accounts SET balance = balance + 100 WHERE id = 2");
    $pdo->commit();
} catch (Exception $e) {
    $pdo->rollBack();
    throw $e;
}
```

## Migration Steps

1. **Find all mysql_* calls**:

```bash
grep -rn "\bmysql_" --include="*.php" /path/to/project/
```

2. **Choose your replacement**: `mysqli` is a closer drop-in match, but PDO is the modern standard and supports multiple database drivers.

3. **Replace the connection** with either `new mysqli()` or `new PDO()`.

4. **Convert every query** that uses user input to a prepared statement with bound parameters. This is the most important step for security.

5. **Replace row-count functions**: `mysql_num_rows($result)` becomes `$result->num_rows` (mysqli) or `$stmt->rowCount()` (PDO).

6. **Replace `mysql_fetch_*` calls** with `$result->fetch_assoc()` (mysqli) or `$stmt->fetch()` (PDO).

7. **Update error handling**. `mysqli` returns `false` on failure; PDO can throw exceptions with `ERRMODE_EXCEPTION`.

8. **Test every database interaction** in your application. This is a high-risk migration — do not skip testing.

For very large codebases, consider using [Rector](https://getrector.com/) to automate the mechanical parts of the conversion.
