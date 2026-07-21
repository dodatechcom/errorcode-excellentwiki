---
title: "[Solution] Deprecated Function Migration: session_register() to $_SESSION"
description: "Migrate from deprecated session_register() to direct $_SESSION superglobal in PHP."
deprecated_function: "session_register()"
replacement_function: "$_SESSION[]"
languages: ["php"]
deprecated_since: "PHP 5.3 / removed PHP 7.0"
---

# [Solution] Deprecated Function Migration: session_register() to $_SESSION

The `session_register()` has been deprecated in favor of `$_SESSION[]`.

## Migration Guide

session_register() was removed in PHP 7.0. Use the $_SESSION superglobal directly.

## Before (Deprecated)

```php
session_register("username");
$username = "Alice";
session_register("user_id");
$user_id = 123;
```

## After (Modern)

```php
session_start();
$_SESSION["username"] = "Alice";
$_SESSION["user_id"] = 123;

echo $_SESSION["username"];
unset($_SESSION["username"]);
```

## Key Differences

- Use $_SESSION[key] = value to set variables
- Use session_start() at the beginning
- Use isset() to check if set
- Use unset() to remove
