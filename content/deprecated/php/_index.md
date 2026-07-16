---
title: "[Solution] PHP Deprecated Functions — Migration Guide & Replacements"
description: "PHP deprecated function migration guides. Replace ereg, split, each, mysql_*, and create_function with modern PHP equivalents."
deprecated: ["php"]
---

PHP removes deprecated functions in major version bumps — the PHP 5.x to 7.x transition removed over 70 functions, and PHP 8.0 and 8.1 removed or deprecated many more. Each entry below shows the old function, the reason it was removed, and the modern replacement with a copy-paste code snippet.

## Deprecated Functions

| Deprecated | Description | Replacement |
|------------|-------------|-------------|
| [create_function()](/deprecated/php/create-function/) | Deprecated in PHP 7.2 — creates a function from a string at runtime | Use anonymous functions (closures) with `function() {}` syntax |
| [each()](/deprecated/php/each-to-foreach/) | Removed in PHP 8.0 — iterates array with internal pointer | Replace with `foreach`, `key()`, and `current()` |
| [ereg()](/deprecated/php/ereg-to-preg-match/) | Removed in PHP 7.0 — POSIX regex matching | Replace with `preg_match()` using PCRE regex syntax |
| [mysql_*](/deprecated/php/mysql-to-mysqli/) | Removed in PHP 7.0 — the entire mysql extension | Migrate to `mysqli_*` functions or PDO with prepared statements |
| [split()](/deprecated/php/split-to-explode/) | Removed in PHP 7.0 — splits a string by a regex or delimiter | Replace with `explode()` for delimiter splits, or `preg_split()` for regex |

## Quick Check

```php
// Enable deprecation warnings in development
error_reporting(E_ALL);
ini_set('display_errors', 1);
```
