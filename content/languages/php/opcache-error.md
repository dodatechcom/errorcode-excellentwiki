---
title: "[Solution] PHP OPcache Error — Invalid File"
description: "Fix PHP OPcache errors. Resolve 'OPcache error: Invalid file' by clearing the cache, validating paths, and configuring OPcache correctly."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "php"
tags: ["php", "opcache", "performance"]
severity: "error"
---

# PHP OPcache Error

## Error Message

```
opcache_invalidate(): Failed to force revalidation of script: /var/www/app/cache/config.php
```

## Common Causes

- The OPcache has stale or corrupted entries for files that have been modified or deleted
- The script path does not exist in the OPcache's file table (e.g., after deployment)
- OPcache's validate_timestamps is set to 0, preventing automatic revalidation

## Solutions

### Solution 1: Clear OPcache After Deployment

Reset or invalidate the OPcache when deploying new code to ensure fresh bytecode is used.

```php
<?php
// Clear the entire OPcache
opcache_reset();
echo "OPcache cleared successfully\n";

// Or invalidate a specific file
$configPath = '/var/www/app/config/routes.php';
if (opcache_invalidate($configPath, true)) {
    echo "Invalidated: $configPath\n";
} else {
    echo "Failed to invalidate: $configPath\n";
}

// Check OPcache status
$status = opcache_get_status(false);
if ($status !== false) {
    echo "Cached scripts: " . $status['opcache_statistics']['num_cached_scripts'] . "\n";
    echo "Memory used: " . round($status['memory_usage']['used_memory'] / 1024 / 1024, 2) . "MB\n";
}
?>
```

### Solution 2: Create an OPcache Management Script

Use a dedicated script to validate and refresh the OPcache during maintenance windows.

```php
<?php
// opcache-clear.php — run from CLI or a deployment script
if (php_sapi_name() !== 'cli') {
    http_response_code(403);
    die('CLI only');
}

echo "Clearing OPcache...\n";
$start = microtime(true);

// Reset the entire cache
opcache_reset();

$elapsed = round((microtime(true) - $start) * 1000, 2);
echo "OPcache cleared in {$elapsed}ms\n";

// Verify new files are being compiled
$status = opcache_get_status(false);
if ($status !== false) {
    $stats = $status['opcache_statistics'];
    echo "Cached scripts: {$stats['num_cached_scripts']}\n";
    echo "Memory used: " . round($status['memory_usage']['used_memory'] / 1024 / 1024, 2) . "MB\n";
    echo "Restart count: {$stats['restart_count']}\n";
}

// Invalidate a specific file that was just updated
$updatedFile = '/var/www/app/routes/api.php';
if (opcache_invalidate($updatedFile, true)) {
    echo "Invalidated: $updatedFile\n";
}
?>
```

## Prevention Tips

- Add `opcache_invalidate()` calls to your deployment script
- Set opcache.validate_timestamps=1 in development for automatic cache refresh
- Use `opcache_get_status()` to monitor cache usage and detect issues

## Related Errors

- [Memory Limit Error]({{< relref "/languages/php/memory-limit-error" >}})
- [Memory Exhausted]({{< relref "/languages/php/memory-exhausted" >}})
