---
title: "[Solution] PHP File Write Error — Failed to Write Stream"
description: "Fix PHP 'Failed to write stream' errors. Resolve file write failures with fopen, fwrite, and file_put_contents."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "php"
tags: ["php", "filesystem", "file-write"]
severity: "error"
---

# PHP File Write Error

## Error Message

```
fwrite(): Failed to write stream: No space left on device
```

## Common Causes

- The disk is full and cannot accept more data
- The file handle is not open in write mode ('w', 'a', 'x')
- The process lacks write permission to the target directory

## Solutions

### Solution 1: Check Disk Space Before Writing

Verify available disk space before attempting large writes to avoid mid-operation failures.

```php
<?php
function hasDiskSpace(string $directory, int $minBytes = 1048576): bool {
    $free = disk_free_space($directory);
    if ($free === false) {
        error_log("Cannot determine free space for: $directory");
        return false;
    }
    return $free >= $minBytes;
}

// Usage
$uploadDir = '/var/www/uploads';
if (!hasDiskSpace($uploadDir, 10 * 1024 * 1024)) {
    http_response_code(507);
    throw new RuntimeException("Insufficient disk space for upload");
}

// Safe to write
$dest = "$uploadDir/" . basename($_FILES['document']['name']);
if (move_uploaded_file($_FILES['document']['tmp_name'], $dest)) {
    echo "Upload successful";
} else {
    error_log("Upload failed for: " . $_FILES['document']['name']);
}
?>
```

### Solution 2: Use Atomic Writes to Prevent Corruption

Write to a temporary file first, then rename it into place so readers never see a partially written file.

```php
<?php
function atomicWrite(string $targetPath, string $content): bool {
    $tempPath = $targetPath . '.' . getmypid() . '.tmp';

    $bytesWritten = file_put_contents($tempPath, $content, LOCK_EX);
    if ($bytesWritten === false) {
        @unlink($tempPath);
        return false;
    }

    // Atomic rename — replaces $targetPath if it exists
    if (!rename($tempPath, $targetPath)) {
        @unlink($tempPath);
        return false;
    }

    return true;
}

// Usage — safe for config files and caches
$config = [
    'db_host' => '127.0.0.1',
    'db_name' => 'myapp',
    'debug'   => false,
];

if (atomicWrite('/var/www/app/config/runtime.json', json_encode($config, JSON_PRETTY_PRINT))) {
    echo "Config written successfully";
} else {
    error_log("Failed to write config file");
}
?>
```

## Prevention Tips

- Always check disk_free_space() before writing large files
- Use file_put_contents() with LOCK_EX for simple atomic writes
- Consider rotating log files when they exceed a size threshold

## Related Errors

- [File Permission Error]({{< relref "/languages/php/file-permission-error" >}})
- [File Lock Error]({{< relref "/languages/php/file-lock-error" >}})
