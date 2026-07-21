---
title: "[Solution] Deprecated Function Migration: mysql_real_escape_string to prepared statements"
description: "Migrate from deprecated mysql_real_escape_string to prepared statements."
deprecated_function: "mysql_real_escape_string($str)"
replacement_function: "PDO prepared statements"
languages: ["php"]
deprecated_since: "PHP 5.5 / removed PHP 7.0"
---

# [Solution] Deprecated Function Migration: mysql_real_escape_string to prepared statements

The `mysql_real_escape_string($str)` has been deprecated in favor of `PDO prepared statements`.

## Migration Guide

Prepared statements prevent SQL injection.

## Before (Deprecated)

```php
$safe = mysql_real_escape_string($input);
```

## After (Modern)

```php
$stmt = $pdo->prepare("SELECT * FROM users WHERE name = ?");
$stmt->execute([$input]);
```

## Key Differences

- Always use prepared statements
