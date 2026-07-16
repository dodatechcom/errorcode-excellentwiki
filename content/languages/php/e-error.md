---
title: "[Solution] PHP E_ERROR — Fatal Runtime Error Fix"
description: "Fix PHP E_ERROR fatal runtime errors that halt script execution. Learn common causes and solutions for memory exhaustion, undefined functions, and type errors."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["e-error", "fatal", "runtime"]
weight: 5
---

# [Solution] PHP E_ERROR — Fatal Runtime Error Fix

`E_ERROR` is a fatal runtime error in PHP that stops script execution immediately. The PHP engine cannot recover from this type of error. Common causes include memory exhaustion, calling undefined functions, and uncaught exceptions in PHP 7+.

## Common Causes

- Exceeding the PHP memory limit
- Calling an undefined function
- Missing required files via `require`
- Encountering an uncaught exception

## How to Fix

### 1. Increase Memory Limit

```php
// WRONG — script runs out of memory
<?php
for ($i = 0; $i < 100000000; $i++) {
    $data[] = str_repeat("x", 1000);
}
?>

// CORRECT
<?php
ini_set('memory_limit', '256M');
// Process data in chunks instead
$chunk = [];
for ($i = 0; $i < 1000; $i++) {
    $chunk[] = str_repeat("x", 1000);
}
unset($chunk);
?>
```

### 2. Verify Functions Exist

```php
// WRONG — undefined function
<?php
array_flatten($matrix);
?>

// CORRECT
<?php
function array_flatten(array $array): array {
    $result = [];
    array_walk_recursive($array, function($value) use (&$result) {
        $result[] = $value;
    });
    return $result;
}
?>
```

### 3. Use require_once with File Checks

```php
// WRONG — fatal error if file is missing
<?php
require_once 'config/database.php';
?>

// CORRECT
<?php
$file = __DIR__ . '/config/database.php';
if (file_exists($file)) {
    require_once $file;
} else {
    die("Missing config file: {$file}");
}
?>
```

## Examples

```php
<?php
// E_ERROR: Allowed memory size exhausted
ini_set('memory_limit', '1M');
big_array();

// E_ERROR: Call to undefined function nonexistent()
nonexistent();

// E_ERROR: require(): Failed opening required 'missing.php'
require_once 'missing.php';
?>
```

## Related Errors

- [PHP Fatal Error]({{< relref "/languages/php/fatal-error" >}})
- [PHP Fatal Out of Memory]({{< relref "/languages/php/fatal-out-of-memory" >}})
- [PHP E_ERROR as Exception]({{< relref "/languages/php/error-256" >}})
- [PHP E_RECOVERABLE_ERROR]({{< relref "/languages/php/e-recoverable-error" >}})
