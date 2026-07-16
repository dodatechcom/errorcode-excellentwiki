---
title: "[Solution] PHP Error 7 — ENOMEM Out of Memory Fix"
description: "Fix PHP error code 7 ENOMEM out of memory fatal error. Learn to increase memory limits, process data in chunks, and prevent memory exhaustion."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["error-7", "ENOMEM", "out-of-memory", "memory"]
weight: 5
---

# [Solution] PHP Error 7 — ENOMEM Out of Memory Fix

PHP error code 7 corresponds to `ENOMEM` (error number 7), the out-of-memory condition. PHP reports this as `Fatal error: Allowed memory size of X bytes exhausted (tried to allocate Y bytes)`. The script halts immediately when PHP cannot allocate more memory from the system.

## Common Causes

- Loading very large datasets entirely into memory
- Infinite loops that accumulate data without releasing it
- Insufficient `memory_limit` in `php.ini`
- Large file reads or string operations on big files

## How to Fix

### 1. Increase the Memory Limit

```php
// WRONG — script runs out of 128M default limit
<?php
$data = file_get_contents('huge-file.csv'); // may exhaust memory
?>

// CORRECT — increase memory limit
<?php
ini_set('memory_limit', '512M');
$data = file_get_contents('huge-file.csv');
?>
```

### 2. Process Data in Chunks

```php
// WRONG — loading entire file into memory
<?php
$lines = file('large-file.csv');
foreach ($lines as $line) {
    process_line($line);
}
?>

// CORRECT — read line by line
<?php
$handle = fopen('large-file.csv', 'r');
if ($handle) {
    while (($line = fgets($handle)) !== false) {
        process_line(trim($line));
    }
    fclose($handle);
}
?>
```

### 3. Free Memory When Done

```php
<?php
$largeArray = range(1, 1000000);
process_data($largeArray);
unset($largeArray); // free memory
gc_collect_cycles(); // force garbage collection
?>
```

### 4. Use Generators for Large Datasets

```php
<?php
function readLargeFile(string $file): Generator {
    $handle = fopen($file, 'r');
    if ($handle) {
        while (($line = fgets($handle)) !== false) {
            yield trim($line);
        }
        fclose($handle);
    }
}

foreach (readLargeFile('huge-file.csv') as $line) {
    process_line($line);
}
?>
```

## Examples

```php
<?php
// Fatal error: Allowed memory size of 134217728 bytes exhausted
$bigArray = array_fill(0, 10000000, str_repeat('x', 100));

// Fatal error after increasing limit to 256M
ini_set('memory_limit', '256M');
$evenBiggerArray = array_fill(0, 50000000, str_repeat('x', 100));
?>
```

## Related Errors

- [PHP Fatal Error]({{< relref "/languages/php/fatal-error" >}})
- [PHP Fatal Out of Memory]({{< relref "/languages/php/fatal-out-of-memory" >}})
- [PHP E_ERROR]({{< relref "/languages/php/e-error" >}})
- [PHP E_ALL]({{< relref "/languages/php/e-all" >}})
