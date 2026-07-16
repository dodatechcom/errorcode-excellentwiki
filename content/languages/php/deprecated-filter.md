---
title: "[Solution] PHP Deprecated: Filter Extensions — Migrate to filter_input Fix"
description: "Fix PHP Deprecated filter extension warnings. Migrate from ereg and split to filter_input, filter_var, and the modern filter API."
languages: ["php"]
severities: ["warning"]
error_types: ["runtime"]
tags: ["deprecated", "filter", "filter_input", "filter_var", "migration"]
date: 2026-07-15
---

# PHP Deprecated: Filter Extensions Warning

This deprecation warning appears when your code uses legacy filtering functions such as `ereg()`, `ereg_replace()`, `split()`, or `session_register()` that relied on the old POSIX regex-based filter extensions. These functions have been removed from PHP 7.0+.

## Common Causes

- Using `ereg()`, `ereg_replace()`, or `eregi()` for pattern matching
- Using `split()` to split strings by a delimiter
- Calling `session_register()` to register session variables
- Using `mysql_*` functions that relied on the removed extension

## Solutions

### 1. Migrate to `filter_input()` for User Input

Replace `ereg`-based input validation with PHP's built-in filter functions.

```php
// Old — deprecated ereg
if (ereg("^[a-zA-Z0-9]+$", $_POST["username"])) {
    // valid
}

// New — use filter_input with FILTER_VALIDATE_REGEXP
$username = filter_input(INPUT_POST, "username", FILTER_VALIDATE_REGEXP, [
    "options" => ["regexp" => "/^[a-zA-Z0-9]+$/"]
]);

if ($username !== false) {
    // valid
}
```

### 2. Migrate to `filter_var()` for Variable Filtering

Use `filter_var()` to sanitize and validate strings, emails, URLs, and more.

```php
// Old — deprecated ereg for email
if (ereg("^[^@]+@[^@]+\\.[a-zA-Z]{2,}$", $email)) {
    // valid
}

// New — use FILTER_VALIDATE_EMAIL
if (filter_var($email, FILTER_VALIDATE_EMAIL)) {
    // valid
}
```

### 3. Replace `split()` with `explode()` or `preg_split()`

The old `split()` function is gone — use modern alternatives.

```php
// Old — deprecated split
$parts = split(",", "a,b,c");

// New — use explode (simple delimiter)
$parts = explode(",", "a,b,c");

// Or use preg_split (regex delimiter)
$parts = preg_split("/\s+/", "hello world foo bar");
```

### 4. Update Session Handling

Replace `session_register()` with direct `$_SESSION` assignment.

```php
// Old — deprecated session_register
session_register("user_id");

// New — direct assignment
session_start();
$_SESSION["user_id"] = $userId;
```

### 5. Use the Modern Filter API for Sanitization

```php
// Sanitize a string for safe HTML output
$clean = filter_input(INPUT_POST, "comment", FILTER_SANITIZE_FULL_SPECIAL_CHARS);

// Validate an integer
$age = filter_input(INPUT_GET, "age", FILTER_VALIDATE_INT, [
    "options" => ["min_range" => 1, "max_range" => 150]
]);
```

## Migration Checklist

| Old Function | Modern Replacement |
|---|---|
| `ereg()` | `preg_match()` or `filter_var()` |
| `ereg_replace()` | `preg_replace()` or `filter_var()` |
| `split()` | `explode()` or `preg_split()` |
| `session_register()` | Direct `$_SESSION[]` assignment |

## Related Errors

- [PHP Notice: Undefined Variable](/languages/php/notice-undefined-variable)
- [PHP Warning: Cannot Modify Header Info](/languages/php/warning-header-sent)
