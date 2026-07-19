---
title: "[Solution] PHP Deprecated Use of Deprecated Functionality (E_DEPRECATED) Fix"
description: "Fix E_DEPRECATED warnings in PHP 8.4 for deprecated functionality. Migrate to modern PHP APIs and patterns."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "php"
tags: ["php", "php84", "deprecation", "e-deprecated", "migration"]
severity: "error"
---

# Deprecated: Use of Deprecated Functionality

## Error Message

```
Deprecated: function_name(): Automatically nullifying incompatible parameters is deprecated in /path/to/file.php:15
```

## Common Causes

- Using deprecated functions, classes, or interfaces that are scheduled for removal in PHP 9.0
- Passing incompatible types to built-in functions that relied on implicit type juggling
- Using configuration directives or INI settings that have been deprecated in PHP 8.4
- Relying on deprecated behavior that PHP now warns about, like automatic null conversion

## Solutions

### Solution 1: Replace deprecated functions with their modern equivalents

Find the deprecated function in the PHP migration guide and use the recommended replacement.

```php
<?php
// WRONG: Deprecated functions in PHP 8.4
// mb_convert_encoding() with incompatible parameters
// strtolower() on null
// utf8_encode() / utf8_decode()

// CORRECT: Modern alternatives
$text = 'HELLO WORLD';

// Use mb_strtolower instead of strtolower for multibyte safety
$lower = mb_strtolower($text, 'UTF-8');
echo $lower; // 'hello world'

// Use mb_convert_encoding properly
$encoded = mb_convert_encoding($text, 'HTML-ENTITIES', 'UTF-8');

// PHP 8.4+: Use the new functions
// $clean = mb_strupcase($text); // if available
?>
```

### Solution 2: Update code to handle nullable parameters explicitly

Many PHP 8.4 deprecations relate to implicit null handling — add explicit null checks.

```php
<?php
// WRONG: Implicitly nullifying incompatible types
function processData(string $data, array $options = null): string {
    return strtoupper($data);
}

// Passing null where string is expected
// processData(null); // Deprecated in PHP 8.4

// CORRECT: Explicit null handling
function processData(string $data, ?array $options = null): string {
    if ($options !== null) {
        // process options
    }
    return strtoupper($data);
}

// Safe call with explicit null
processData('hello', null); // OK: explicit null

// Or provide actual values
processData('hello', ['strict' => true]);
?>
```

### Solution 3: Suppress deprecations during transition with error handling

Temporarily suppress specific deprecation warnings while migrating large codebases.

```php
<?php
// In your error handler or bootstrap file
function customErrorHandler(int $errno, string $errstr, string $errfile, int $errline): bool {
    if ($errno === E_DEPRECATED) {
        // Log deprecation for tracking
        error_log("[DEPRECATED] $errstr in $errfile:$errline");

        // Optionally collect for migration tracking
        $deprecations = $_ENV['DEPRECATIONS'] ?? [];
        $deprecations[] = [
            'message' => $errstr,
            'file'    => $errfile,
            'line'    => $errline,
            'time'    => date('c'),
        ];
        $_ENV['DEPRECATIONS'] = $deprecations;

        return true; // suppress the warning
    }
    return false;
}

set_error_handler('customErrorHandler', E_DEPRECATED);

// Now deprecated calls won't halt execution but are logged
// for later migration
?>

```

## Prevention Tips

- Check the PHP 8.4 migration guide (php.net/manual/en/migration84.php) for the full list of deprecations
- Run your test suite with error_reporting(E_ALL) to surface all deprecation warnings
- Use Rector (getrector.com) to automatically upgrade deprecated code patterns
- Address deprecations promptly — they will become errors in PHP 9.0

## Related Errors

- [PHP Deprecated Function Usage]({{< relref "/languages/php/php-deprecated" >}})
- [PHP Deprecated Filter Error]({{< relref "/languages/php/deprecated-filter" >}})
- [PHP Nullable Type Deprecation]({{< relref "/languages/php/php84-nullable-type" >}})
