---
title: "[Solution] Deprecated Function Migration: mysql_connect to mysqli_connect"
description: "Migrate from deprecated mysql_connect to mysqli_connect."
deprecated_function: "mysql_connect($host, $user, $pass)"
replacement_function: "mysqli_connect($host, $user, $pass)"
languages: ["php"]
deprecated_since: "PHP 5.0 / removed PHP 7.0"
---

# [Solution] Deprecated Function Migration: mysql_connect to mysqli_connect

The `mysql_connect($host, $user, $pass)` has been deprecated in favor of `mysqli_connect($host, $user, $pass)`.

## Migration Guide

mysql_* functions were removed.

## Before (Deprecated)

```php
$conn = mysql_connect($host, $user, $pass);
```

## After (Modern)

```php
$conn = mysqli_connect($host, $user, $pass);
```

## Key Differences

- mysql_* was removed in PHP 7.0
