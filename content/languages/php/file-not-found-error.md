---
title: "[Solution] PHP File Not Found Error — No Such File or Directory"
description: "Fix PHP 'No such file or directory' errors. Resolve file not found issues with fopen, include, require, and file operations."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "php"
tags: ["php", "filesystem", "file-not-found"]
severity: "error"
---

# PHP File Not Found Error

## Error Message

```
fopen(/path/to/file.txt): Failed to open stream: No such file or directory
```

## Common Causes

- The file path is incorrect or contains a typo
- The file was deleted or moved before the script ran
- Relative paths resolve differently than expected due to the working directory

## Solutions

### Solution 1: Verify the Path Exists Before Accessing

Always check whether the file exists before attempting to read or write to it.

```php
<?php
$filePath = __DIR__ . '/uploads/data.csv';

if (!file_exists($filePath)) {
    // Create the file or handle the missing file gracefully
    throw new RuntimeException("Required file not found: $filePath");
}

// Safe to proceed
$handle = fopen($filePath, 'r');
// ... read from $handle
fclose($handle);
?>
```

### Solution 2: Use Absolute Paths or __DIR__

Avoid relative paths that depend on the current working directory. Use __DIR__ or __FILE__ to anchor paths to the script's location.

```php
<?php
// Bad — depends on the current working directory
$config = file_get_contents('config/app.php');

// Good — anchored to this file's directory
$config = file_get_contents(__DIR__ . '/config/app.php');

// Good — use a known base path constant
define('BASE_PATH', '/var/www/app');
$template = file_get_contents(BASE_PATH . '/views/home.php');

// Good — resolve symlinks and .. segments
$realPath = realpath(__DIR__ . '/../shared/data.json');
if ($realPath === false) {
    throw new RuntimeException("Path does not exist");
}
$data = file_get_contents($realPath);
?>
```

## Prevention Tips

- Use `__DIR__` to build paths relative to the current script
- Log the full resolved path when debugging file-not-found errors
- Ensure deployment scripts copy all required files to the target environment

## Related Errors

- [File Permission Error]({{< relref "/languages/php/file-permission-error" >}})
- [File Read Error]({{< relref "/languages/php/file-read-error" >}})
