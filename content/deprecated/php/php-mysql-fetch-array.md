---
title: "[Solution] Deprecated Function Migration: mysql_fetch_array to mysqli_fetch_assoc"
description: "Migrate from deprecated mysql_fetch_array to mysqli_fetch_assoc in PHP."
deprecated_function: "mysql_fetch_array()"
replacement_function: "mysqli_fetch_assoc()"
languages: ["php"]
deprecated_since: "PHP 5.5 / removed PHP 7.0"
---

# [Solution] Deprecated Function Migration: mysql_fetch_array to mysqli_fetch_assoc

The `mysql_fetch_array()` has been deprecated in favor of `mysqli_fetch_assoc()`.

## Migration Guide

mysql_fetch_array was part of the removed mysql extension. Use mysqli_fetch_assoc for associative arrays.

## Before (Deprecated)

```php
$result = mysql_query("SELECT * FROM users");
while ($row = mysql_fetch_array($result)) {
    echo $row["name"];
}
```

## After (Modern)

```php
$result = $conn->query("SELECT * FROM users");
while ($row = $result->fetch_assoc()) {
    echo $row["name"];
}
```

## Key Differences

- Use mysqli object-oriented or procedural style
- fetch_assoc returns associative array
- Always use prepared statements
