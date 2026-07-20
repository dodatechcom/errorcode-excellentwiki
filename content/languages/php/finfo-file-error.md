---
title: "[Solution] PHP finfo::file() Returns False — Invalid Fileinfo Object"
description: "Fix PHP finfo::file() returns false by checking file path, verifying finfo initialization, and handling empty files. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 17
---

# PHP finfo::file() Returns False — Invalid Fileinfo Object

The `finfo::file()` method returned `false` instead of the MIME type string. This happens when the file path is invalid, the file is not readable, the finfo object was not initialized properly, or the file is empty.

## Common Causes

```php
// Cause 1: File does not exist
$finfo = new finfo(FILEINFO_MIME_TYPE);
$mimeType = $finfo->file('/nonexistent/file.txt'); // Returns false

// Cause 2: File is not readable
$finfo = new finfo(FILEINFO_MIME_TYPE);
$mimeType = $finfo->file('/protected/secret.bin'); // Permission denied

// Cause 3: Empty file
file_put_contents('/tmp/empty.txt', '');
$finfo = new finfo(FILEINFO_MIME_TYPE);
$mimeType = $finfo->file('/tmp/empty.txt'); // Returns 'application/x-empty'

// Cause 4: finfo object not properly initialized
$finfo = false;
$mimeType = $finfo->file('test.txt'); // Calling method on false

// Cause 5: Path is a directory, not a file
$finfo = new finfo(FILEINFO_MIME_TYPE);
$mimeType = $finfo->file('/tmp/'); // Returns false
```

## How to Fix

### Fix 1: Validate File Before Detection

```php
function safeDetectMimeType(string $filePath): ?string {
    $realPath = realpath($filePath);

    if ($realPath === false) {
        error_log("File path does not exist: {$filePath}");
        return null;
    }

    if (!is_file($realPath)) {
        error_log("Path is not a file: {$realPath}");
        return null;
    }

    if (!is_readable($realPath)) {
        error_log("File is not readable: {$realPath}");
        return null;
    }

    if (filesize($realPath) === 0) {
        return 'application/x-empty';
    }

    $finfo = new finfo(FILEINFO_MIME_TYPE);
    $mimeType = $finfo->file($realPath);

    if ($mimeType === false) {
        error_log("finfo::file() failed for: {$realPath}");
        return null;
    }

    return $mimeType;
}
```

### Fix 2: Check finfo Object Initialization

```php
function createFinfoObject(): ?finfo {
    if (!extension_loaded('fileinfo')) {
        error_log('fileinfo extension is not installed');
        return null;
    }

    $finfo = @new finfo(FILEINFO_MIME_TYPE);

    if ($finfo === false) {
        error_log('Failed to create finfo object');
        return null;
    }

    return $finfo;
}

function detectMimeTypeSafe(string $filePath): ?string {
    $finfo = createFinfoObject();
    if ($finfo === null) {
        return null;
    }

    $mimeType = @$finfo->file($filePath);

    if ($mimeType === false) {
        error_log("MIME detection failed for: {$filePath}");
        return null;
    }

    return $mimeType;
}
```

### Fix 3: Handle Empty Files

```php
function detectMimeTypeWithEmptyCheck(string $filePath): string {
    if (!file_exists($filePath)) {
        return 'application/octet-stream';
    }

    $size = filesize($filePath);

    if ($size === 0) {
        return 'application/x-empty';
    }

    $finfo = new finfo(FILEINFO_MIME_TYPE);
    $mimeType = $finfo->file($filePath);

    if ($mimeType === false) {
        return 'application/octet-stream';
    }

    return $mimeType;
}
```

### Fix 4: Use finfo_buffer() for In-Memory Data

```php
function detectMimeTypeFromBuffer(string $data): string {
    if (empty($data)) {
        return 'application/x-empty';
    }

    if (!extension_loaded('fileinfo')) {
        return 'application/octet-stream';
    }

    $finfo = new finfo(FILEINFO_MIME_TYPE);
    $mimeType = $finfo->buffer($data);

    if ($mimeType === false) {
        return 'application/octet-stream';
    }

    return $mimeType;
}
```

## Examples

```php
// Example: Batch MIME type detection with error handling
function batchDetectMimeTypes(array $filePaths): array {
    $results = [];
    $finfo = null;

    if (extension_loaded('fileinfo')) {
        $finfo = new finfo(FILEINFO_MIME_TYPE);
    }

    foreach ($filePaths as $filePath) {
        if (!file_exists($filePath)) {
            $results[$filePath] = ['error' => 'File not found'];
            continue;
        }

        if (!is_readable($filePath)) {
            $results[$filePath] = ['error' => 'File not readable'];
            continue;
        }

        if ($finfo !== null) {
            $mimeType = $finfo->file($filePath);
            if ($mimeType !== false) {
                $results[$filePath] = ['mime' => $mimeType, 'size' => filesize($filePath)];
                continue;
            }
        }

        // Fallback to extension-based detection
        $ext = strtolower(pathinfo($filePath, PATHINFO_EXTENSION));
        $results[$filePath] = ['mime' => "application/{$ext}", 'size' => filesize($filePath)];
    }

    return $results;
}

$files = ['/tmp/photo.jpg', '/tmp/missing.txt', '/tmp/data.bin'];
$results = batchDetectMimeTypes($files);
```

## Related Errors

- [finfo::finfo() failed to load magic database](/languages/php/finfo-load-error/)
- [MIME detection error](/languages/php/mime-detection-error/)
- [file read error](/languages/php/file-read-error/)
