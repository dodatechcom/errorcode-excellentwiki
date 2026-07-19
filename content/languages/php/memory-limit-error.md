---
title: "[Solution] PHP Allowed Memory Size Exhausted Error"
description: "Fix PHP memory limit errors. Resolve 'Allowed memory size exhausted' by optimizing code, increasing limits, and using generators."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "php"
tags: ["php", "memory", "performance"]
severity: "error"
---

# PHP Allowed Memory Size Exhausted Error

## Error Message

```
Allowed memory size of 134217728 bytes exhausted (tried to allocate 262144 bytes)
```

## Common Causes

- Loading large datasets entirely into memory (e.g., large database results or files)
- Unintentional memory leaks from circular references or static variables accumulating
- Recursive function calls creating deep call stacks that consume memory

## Solutions

### Solution 1: Increase Memory Limit Appropriately

Raise the memory limit for scripts that legitimately need more than the default.

```php
<?php
// Check the current limit
echo "Current memory limit: " . ini_get('memory_limit') . "\n";
// Output: Current memory limit: 128M

// Increase for this specific script
ini_set('memory_limit', '512M');
echo "New memory limit: " . ini_get('memory_limit') . "\n";

// Verify the increase was applied
if (ini_get('memory_limit') === '512M') {
    echo "Memory limit increased successfully\n";
}

// Monitor usage during execution
echo "Current usage: " . round(memory_get_usage() / 1024 / 1024, 2) . "MB\n";
echo "Peak usage: " . round(memory_get_peak_usage() / 1024 / 1024, 2) . "MB\n";
?>
```

### Solution 2: Process Large Datasets with Generators

Replace array-based loops with generators to keep memory usage constant regardless of dataset size.

```php
<?php
// Bad — loads all rows into memory
function getAllOrders(PDO $pdo): array {
    $stmt = $pdo->query("SELECT * FROM orders WHERE status = 'pending'");
    return $stmt->fetchAll(PDO::FETCH_ASSOC); // Could use hundreds of MB
}

// Good — yields one row at a time
function streamOrders(PDO $pdo): Generator {
    $stmt = $pdo->query("SELECT * FROM orders WHERE status = 'pending'");
    while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
        yield $row;
    }
}

// Usage — memory stays constant no matter how many rows exist
$pdo = new PDO('mysql:host=localhost;dbname=shop', 'user', 'pass');
$processed = 0;

foreach (streamOrders($pdo) as $order) {
    processOrder($order);
    $processed++;

    if ($processed % 1000 === 0) {
        echo "Processed: $processed, Memory: "
             . round(memory_get_usage() / 1024 / 1024, 2) . "MB\n";
    }
}
echo "Total processed: $processed\n";
?>
```

## Prevention Tips

- Set a reasonable memory_limit in php.ini (256M is a common production default)
- Use `memory_get_peak_usage()` in development to identify memory-hungry code paths
- Profile with Xdebug or Blackfire to find the exact source of memory leaks

## Related Errors

- [Memory Exhausted]({{< relref "/languages/php/memory-exhausted" >}})
- [Fatal Out Of Memory]({{< relref "/languages/php/fatal-out-of-memory" >}})
