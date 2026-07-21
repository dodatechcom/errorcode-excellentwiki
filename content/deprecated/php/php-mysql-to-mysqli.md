---
title: "[Solution] Deprecated Function Migration: mysql_* to mysqli_* or PDO"
description: "Migrate from deprecated mysql_* functions to mysqli or PDO in PHP for security."
deprecated_function: "mysql_*"
replacement_function: "mysqli_* / PDO"
languages: ["php"]
deprecated_since: "PHP 5.5 / removed PHP 7.0"
---

# [Solution] Deprecated Function Migration: mysql_* to mysqli_* or PDO

The `mysql_*` has been deprecated in favor of `mysqli_* / PDO`.

## Migration Guide

The mysql extension was deprecated in PHP 5.5 and removed in PHP 7.0. Use mysqli or PDO for database access.

## Before (Deprecated)

```php
$conn = mysql_connect("localhost", "user", "pass");
mysql_select_db("mydb", $conn);
$result = mysql_query("SELECT * FROM users WHERE id = $id", $conn);
while ($row = mysql_fetch_assoc($result)) {
    echo $row["name"];
}
mysql_close($conn);
```

## After (Modern)

```php
// MySQLi with prepared statements
$conn = new mysqli("localhost", "user", "pass", "mydb");
$stmt = $conn->prepare("SELECT * FROM users WHERE id = ?");
$stmt->bind_param("i", $id);
$stmt->execute();
$result = $stmt->get_result();
while ($row = $result->fetch_assoc()) {
    echo $row["name"];
}

// PDO
$pdo = new PDO("mysql:host=localhost;dbname=mydb", "user", "pass");
$stmt = $pdo->prepare("SELECT * FROM users WHERE id = ?");
$stmt->execute([$id]);
while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
    echo $row["name"];
}
```

## Key Differences

- Use prepared statements to prevent SQL injection
- mysqli supports both procedural and object-oriented
- PDO supports multiple database drivers
