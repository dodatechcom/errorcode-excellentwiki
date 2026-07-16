---
title: "PHP Fatal Error: Allowed memory size exhausted"
description: "Fix PHP Fatal error: Allowed memory size of X bytes exhausted. Learn to increase memory limits, free memory, and process data efficiently."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["fatal-error", "memory", "memory-limit", "out-of-memory"]
weight: 5
---

# PHP Fatal Error: Allowed memory size exhausted

This fatal error occurs when a PHP script tries to use more memory than the configured `memory_limit`. PHP immediately halts execution because the process has exhausted its allocated memory.

## Common Causes

- Loading large files or datasets entirely into memory
- Unbounded loops accumulating data in arrays
- Recursive function calls that never terminate
- Processing large images, XML, or JSON structures without chunking

## How to Fix

### Increase the Memory Limit

```php
<?php
ini_set('memory_limit', '256M');
// Your code here
?>
```

Or set it in `php.ini`:

```ini
memory_limit = 256M
```

### Process Data in Chunks

```php
<?php
$handle = fopen('largefile.csv', 'r');
if ($handle) {
    $chunk = [];
    while (($line = fgets($handle)) !== false) {
        $chunk[] = trim($line);
        if (count($chunk) >= 1000) {
            processChunk($chunk);
            $chunk = [];
        }
    }
    if (!empty($chunk)) {
        processChunk($chunk);
    }
    fclose($handle);
}
?>
```

### Free Memory Manually

```php
<?php
unset($largeArray);
gc_collect_cycles();
?>
```

## Examples

```php
<?php
// This triggers the fatal error
$data = [];
for ($i = 0; $i < 10000000; $i++) {
    $data[] = str_repeat('x', 10000);
}
// Fatal error: Allowed memory size of 134217728 bytes exhausted
?>
```

## Related Errors

- [PHP Fatal Error]({{< relref "/languages/php/fatal-error" >}})
- [PHP Warning: count()]({{< relref "/languages/php/warning-count" >}})
- [PHP Notice: Undefined Variable]({{< relref "/languages/php/notice-undefined-variable" >}})
