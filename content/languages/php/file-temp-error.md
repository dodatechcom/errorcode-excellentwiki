---
title: "[Solution] PHP Temporary File Error — Temp File Creation Failed"
description: "Fix PHP temporary file errors. Resolve temp file creation failures with sys_get_temp_dir, tempnam, and upload handling."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "php"
tags: ["php", "filesystem", "temp-file"]
severity: "error"
---

# PHP Temporary File Error

## Error Message

```
tempnam(): Cannot create temporary file in /tmp: No space left on device
```

## Common Causes

- The system temporary directory is full or out of inodes
- The open_basedir restriction prevents PHP from using the temp directory
- The upload_tmp_dir in php.ini points to a non-existent or unwritable location

## Solutions

### Solution 1: Use a Custom Temporary Directory

Bypass the system temp directory by defining a project-specific temporary path.

```php
<?php
function createTempFile(string $suffix = '.tmp'): string {
    $tempDir = __DIR__ . '/../tmp';

    if (!is_dir($tempDir)) {
        mkdir($tempDir, 0755, true);
    }

    $tempFile = tempnam($tempDir, 'app_');
    if ($tempFile === false) {
        throw new RuntimeException("Cannot create temp file in $tempDir");
    }

    return $tempFile;
}

// Usage
$tmpPath = createTempFile('.csv');
try {
    // Write data to the temp file
    file_put_contents($tmpPath, $csvData);
    // Process or move it
    rename($tmpPath, '/var/www/exports/report_' . date('Ymd') . '.csv');
} catch (Throwable $e) {
    @unlink($tmpPath); // Clean up on failure
    throw $e;
}
?>
```

### Solution 2: Clean Up Temp Files Automatically

Use a destructor or shutdown function to ensure temporary files are removed even when errors occur.

```php
<?php
class TempFileManager {
    private array $files = [];

    public function create(string $extension = '.tmp'): string {
        $path = tempnam(sys_get_temp_dir(), 'php_app_');
        if ($extension !== '') {
            $newPath = $path . $extension;
            rename($path, $newPath);
            $path = $newPath;
        }
        $this->files[] = $path;
        return $path;
    }

    public function __destruct() {
        foreach ($this->files as $file) {
            if (file_exists($file)) {
                @unlink($file);
            }
        }
    }
}

// Usage — files are cleaned up when $manager goes out of scope
$manager = new TempFileManager();
$tmpA = $manager->create('.json');
$tmpB = $manager->create('.xml');
file_put_contents($tmpA, json_encode($data));
// Both temp files are deleted when $manager is destroyed
?>
```

## Prevention Tips

- Monitor disk space and inode usage on the temp partition
- Set open_basedir to include your custom temp directory if needed
- Clean up temp files in a finally block or use a destructor-based approach

## Related Errors

- [File Permission Error]({{< relref "/languages/php/file-permission-error" >}})
- [File Write Error]({{< relref "/languages/php/file-write-error" >}})
