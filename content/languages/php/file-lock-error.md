---
title: "[Solution] PHP File Lock Error — Unable to Lock File"
description: "Fix PHP file lock errors. Resolve 'Unable to lock file' issues with flock, file locking strategies, and concurrent access."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "php"
tags: ["php", "filesystem", "locking"]
severity: "error"
---

# PHP File Lock Error

## Error Message

```
flock(): Failed to lock file: Resource temporarily unavailable
```

## Common Causes

- Another process or request holds an exclusive lock on the file
- The script timed out while waiting for a shared lock (LOCK_SH)
- A deadlocked process left a lock file behind without releasing it

## Solutions

### Solution 1: Implement Non-Blocking Lock Acquisition

Use LOCK_NB to fail immediately instead of blocking when the file is locked, and handle the failure gracefully.

```php
<?php
function acquireLock(string $lockFile, int $timeout = 5): resource|false {
    $lock = fopen($lockFile, 'c');
    if ($lock === false) {
        return false;
    }

    $start = time();
    while (!flock($lock, LOCK_EX | LOCK_NB)) {
        if ((time() - $start) >= $timeout) {
            fclose($lock);
            return false; // Timed out waiting for lock
        }
        usleep(100_000); // 100ms
    }

    return $lock;
}

// Usage
$lock = acquireLock('/tmp/myapp.lock', 10);
if ($lock === false) {
    http_response_code(503);
    die("Service temporarily unavailable — another process is running");
}

try {
    // Critical section — only one process runs this at a time
    $data = json_decode(file_get_contents('/var/www/data/state.json'), true);
    $data['counter']++;
    file_put_contents('/var/www/data/state.json', json_encode($data));
} finally {
    flock($lock, LOCK_UN);
    fclose($lock);
}
?>
```

### Solution 2: Clean Up Stale Lock Files

Detect and remove lock files left behind by crashed processes.

```php
<?php
function cleanStaleLock(string $lockFile, int $maxAge = 300): bool {
    if (!file_exists($lockFile)) {
        return true;
    }

    $age = time() - filemtime($lockFile);
    if ($age > $maxAge) {
        // Lock file is older than $maxAge seconds — likely stale
        error_log("Removing stale lock file: $lockFile (age: {$age}s)");
        return unlink($lockFile);
    }

    return false; // Lock file is recent; don't remove it
}

// Usage — run before acquiring the lock
cleanStaleLock('/tmp/myapp.lock');

$lock = fopen('/tmp/myapp.lock', 'c');
if ($lock && flock($lock, LOCK_EX | LOCK_NB)) {
    try {
        // ... critical section
    } finally {
        flock($lock, LOCK_UN);
        fclose($lock);
    }
}
?>
```

## Prevention Tips

- Always release locks in a finally block to prevent deadlocks
- Set reasonable lock timeouts — never wait indefinitely in web requests
- Use separate lock files for each resource instead of a single global lock

## Related Errors

- [File Exists Error]({{< relref "/languages/php/file-exists-error" >}})
- [File Write Error]({{< relref "/languages/php/file-write-error" >}})
