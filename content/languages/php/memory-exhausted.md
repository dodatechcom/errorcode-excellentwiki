---
title: "[Solution] PHP Out of Memory Fatal Error"
description: "Fix PHP out of memory fatal errors. Resolve complete memory exhaustion with optimization, cleanup, and process management."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "php"
tags: ["php", "memory", "fatal"]
severity: "error"
---

# PHP Out of Memory Error

## Error Message

```
Fatal error: Out of memory (allocated 262144) in /var/www/app/script.php on line 42
```

## Common Causes

- The script has already consumed all available memory and cannot allocate more
- An infinite loop or unbounded recursion is consuming memory rapidly
- A large string concatenation in a loop is creating increasingly large temporary strings

## Solutions

### Solution 1: Identify and Eliminate Memory Leaks

Profile memory usage to find variables that grow unexpectedly and free them proactively.

```php
<?php
function monitorMemory(string $label): void {
    $usage = round(memory_get_usage(true) / 1024 / 1024, 2);
    $peak  = round(memory_get_peak_usage(true) / 1024 / 1024, 2);
    error_log("[MEMORY] $label — Usage: {$usage}MB, Peak: {$peak}MB");
}

// Example: processing a large dataset with controlled memory usage
function processLargeDataset(array $items): void {
    monitorMemory("Before processing");

    $batchSize = 100;
    $batch = [];

    foreach ($items as $index => $item) {
        $batch[] = $item;

        if (count($batch) >= $batchSize) {
            processBatch($batch);
            $batch = []; // Free the batch from memory
            monitorMemory("After batch " . ($index + 1));
        }
    }

    // Process remaining items
    if (!empty($batch)) {
        processBatch($batch);
    }

    monitorMemory("After all processing");
}
?>
```

### Solution 2: Use Generators and Streaming Instead of Loading Everything

Rewrite code that loads entire datasets to process items one at a time.

```php
<?php
// Bad — concatenates strings in a loop, doubling memory each time
function buildBadString(array $words): string {
    $result = '';
    foreach ($words as $word) {
        $result .= $word . ' '; // Each append creates a new string copy
    }
    return $result;
}

// Good — uses implode for a single allocation
function buildGoodString(array $words): string {
    return implode(' ', $words);
}

// Good — streams large files line by line
function countLines(string $filePath): int {
    $count = 0;
    $handle = fopen($filePath, 'r');
    if ($handle === false) {
        throw new RuntimeException("Cannot open: $filePath");
    }

    try {
        while (fgets($handle) !== false) {
            $count++;
        }
    } finally {
        fclose($handle);
    }

    return $count;
}

echo "Line count: " . countLines('/var/www/logs/access.log') . "\n";
echo "Current memory: " . round(memory_get_usage() / 1024 / 1024, 2) . "MB\n";
?>
```

## Prevention Tips

- Use `unset($largeVariable)` to free memory before the next loop iteration
- Set memory_limit in php.ini to prevent a single script from crashing the server
- Use `php -d memory_limit=512M script.php` to test with more memory from CLI

## Related Errors

- [Memory Limit Error]({{< relref "/languages/php/memory-limit-error" >}})
- [Fatal Out Of Memory]({{< relref "/languages/php/fatal-out-of-memory" >}})
