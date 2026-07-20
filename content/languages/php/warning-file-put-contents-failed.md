---
title: "[Solution] PHP Warning: file_put_contents() Failed to Open Stream"
description: "Fix PHP Warning: file_put_contents() failed to open stream. Check directory permissions, verify disk space, check file permissions."
languages: ["php"]
severities: ["warning"]
error-types: ["runtime-error"]
weight: 9
---

# PHP Warning: file_put_contents() Failed to Open Stream

This warning occurs when `file_put_contents()` cannot write to the specified file or directory. The function returns `false` instead of the number of bytes written, and the data is silently lost.

## Common Causes

```php
<?php
// Example 1: Directory does not exist
file_put_contents("/nonexistent/path/data.txt", "content");
// Warning: file_put_contents(): Failed to open stream: No such file or directory
```

```php
<?php
// Example 2: Insufficient permissions on directory
file_put_contents("/var/www/protected/data.txt", "content");
// Warning: file_put_contents(): Failed to open stream: Permission denied
```

```php
<?php
// Example 3: Disk full
file_put_contents("/var/www/uploads/large.dat", $hugeData);
// Warning: file_put_contents(): Failed to write stream: No space left on device
```

```php
<?php
// Example 4: Read-only file system
file_put_contents("/readonly_mount/data.txt", "content");
// Warning: file_put_contents(): Failed to open stream: Read-only file system
```

```php
<?php
// Example 5: Filename with invalid characters
file_put_contents("/var/www/data/file:name.txt", "content");
// Warning: file_put_contents(): Failed to open stream: Invalid argument
```

## How to Fix

### Fix 1: Ensure the Directory Exists

Create the directory before writing if it may not exist.

```php
<?php
$filepath = "/var/www/uploads/2026/report.csv";
$directory = dirname($filepath);

if (!is_dir($directory)) {
    if (!mkdir($directory, 0755, true)) {
        throw new \RuntimeException("Cannot create directory: {$directory}");
    }
}

$result = file_put_contents($filepath, "data");
if ($result === false) {
    throw new \RuntimeException("Failed to write to {$filepath}");
}
```

### Fix 2: Verify Directory Permissions

Ensure the web server user can write to the target directory.

```php
<?php
$directory = "/var/www/uploads";

if (!is_writable($directory)) {
    throw new \RuntimeException("Directory not writable: {$directory}");
}

file_put_contents($directory . "/data.txt", "content");
```

```bash
# Fix from command line
chown -R www-data:www-data /var/www/uploads
chmod -R 755 /var/www/uploads
```

### Fix 3: Check Available Disk Space

Verify sufficient disk space before writing large files.

```php
<?php
$filepath = "/var/www/data/large_export.csv";
$directory = dirname($filepath);
$data = generateLargeExport();

$freeSpace = disk_free_space($directory);
if ($freeSpace === false || strlen($data) > $freeSpace) {
    throw new \RuntimeException("Insufficient disk space. Need: " . strlen($data) . ", Free: {$freeSpace}");
}

$result = file_put_contents($filepath, $data);
if ($result === false) {
    throw new \RuntimeException("Write failed");
}
```

### Fix 4: Use LOCK_EX for Atomic Writes

Prevent race conditions when multiple processes write to the same file.

```php
<?php
$logEntry = date('c') . " - Request processed\n";

// LOCK_EX ensures exclusive lock — prevents partial writes
$result = file_put_contents("/var/www/logs/access.log", $logEntry, LOCK_EX);
if ($result === false) {
    error_log("Failed to write log entry");
}
```

### Fix 5: Validate Filenames Before Writing

Sanitize filenames to remove or replace invalid characters.

```php
<?php
function safeFilename(string $name): string {
    // Remove characters not allowed in filenames
    $name = preg_replace('/[^\w\-\.]/', '_', $name);
    // Prevent path traversal
    $name = basename($name);
    return $name;
}

$filename = safeFilename($_POST['filename'] ?? 'untitled');
$filepath = "/var/www/uploads/{$filename}";

file_put_contents($filepath, $content);
```

## Examples

```php
<?php
// Complete safe write example
function safeFilePutContents(string $filepath, string $data, int $flags = 0): int {
    $directory = dirname($filepath);

    if (!is_dir($directory)) {
        if (!mkdir($directory, 0755, true)) {
            throw new \RuntimeException("Cannot create directory: {$directory}");
        }
    }

    if (!is_writable($directory)) {
        throw new \RuntimeException("Directory not writable: {$directory}");
    }

    $result = file_put_contents($filepath, $data, $flags);
    if ($result === false) {
        $error = error_get_last();
        throw new \RuntimeException("Write failed: " . ($error["message"] ?? "Unknown error"));
    }

    return $result;
}

$bytes = safeFilePutContents("/var/www/data/report.csv", $csvData, LOCK_EX);
```

## Related Errors

- [PHP Warning: fopen() Failed](/languages/php/warning-fopen-failed)
- [PHP Warning: fwrite() Not Writable](/languages/php/warning-fwrite-not-writable)
- [PHP File Permission Error](/languages/php/file-permission-error)
