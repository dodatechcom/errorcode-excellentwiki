---
title: "[Solution] PHP File Exists Error — File Already Exists"
description: "Fix PHP 'File exists' errors. Handle file already exists conditions when creating, renaming, or moving files in PHP."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "php"
tags: ["php", "filesystem", "file-exists"]
severity: "error"
---

# PHP File Already Exists Error

## Error Message

```
rename(/tmp/old.log, /tmp/new.log): File exists
```

## Common Causes

- The destination file already exists when using rename() or copy()
- A race condition where two concurrent requests try to create the same file
- Using fopen with 'x' mode (exclusive creation) and the file is already present

## Solutions

### Solution 1: Check Before Creating or Renaming

Use file_exists() to check whether the target already exists, then decide how to handle it.

```php
<?php
$destination = '/var/www/uploads/report_2026.pdf';

if (file_exists($destination)) {
    // Option A: Append a timestamp to make the name unique
    $destination = '/var/www/uploads/report_2026_' . time() . '.pdf';
    // Option B: Overwrite by removing the old file first
    // unlink($destination);
}

// Now safe to copy or move
copy('/tmp/report_2026.pdf', $destination);
echo "File saved to: $destination";
?>
```

### Solution 2: Use Atomic File Creation with flock

Prevent race conditions by acquiring an exclusive lock before creating files.

```php
<?php
function atomicCreate(string $path, string $content): bool {
    $lockPath = $path . '.lock';
    $lock = fopen($lockPath, 'c');
    if ($lock === false || !flock($lock, LOCK_EX | LOCK_NB)) {
        if ($lock) fclose($lock);
        return false; // Another process is creating this file
    }

    try {
        if (file_exists($path)) {
            return false; // Already created
        }
        return file_put_contents($path, $content) !== false;
    } finally {
        flock($lock, LOCK_UN);
        fclose($lock);
        @unlink($lockPath);
    }
}

// Usage
$cacheFile = '/tmp/cache/products_' . date('Ymd') . '.json';
if (atomicCreate($cacheFile, json_encode($products))) {
    echo "Cache created successfully";
} else {
    echo "Cache already exists or is being created by another process";
}
?>
```

## Prevention Tips

- Always handle the 'file exists' case explicitly rather than assuming files are absent
- Use file_put_contents() with the LOCK_EX flag for simple atomic writes
- For concurrent workers, consider using a lock file or a distributed lock mechanism

## Related Errors

- [File Write Error]({{< relref "/languages/php/file-write-error" >}})
- [File Lock Error]({{< relref "/languages/php/file-lock-error" >}})
