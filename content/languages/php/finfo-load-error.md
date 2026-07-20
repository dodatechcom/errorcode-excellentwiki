---
title: "[Solution] PHP finfo::finfo() Failed to Load Magic Database"
description: "Fix PHP finfo::finfo() Failed to load magic database by checking magic file path, installing file extension, and verifying LIBMAGIC_PATH. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 17
---

# PHP finfo::finfo() Failed to Load Magic Database

The `new finfo()` or `finfo_open()` call failed to load the magic database. This happens when the magic file is missing, the `fileinfo` extension is not installed, or the path to the magic database is incorrect.

## Common Causes

```php
// Cause 1: fileinfo extension not loaded
$finfo = new finfo(FILEINFO_MIME_TYPE); // Class not found

// Cause 2: Custom magic file path is wrong
$finfo = new finfo(FILEINFO_MIME_TYPE, '/nonexistent/magic.mgc');

// Cause 3: Missing magic database on system
$finfo = finfo_open(FILEINFO_MIME_TYPE); // Returns false

// Cause 4: Corrupted magic database file
$finfo = new finfo(FILEINFO_MIME_TYPE, '/corrupted/path/magic.mgc');

// Cause 5: Fileinfo extension compiled but magic files not installed
// On minimal Docker images or stripped-down systems
```

## How to Fix

### Fix 1: Verify fileinfo Extension Is Installed

```php
if (extension_loaded('fileinfo')) {
    echo 'fileinfo extension is loaded.';
} else {
    echo 'fileinfo extension is NOT installed.';
}

// Check available classes
if (class_exists('finfo')) {
    echo 'finfo class is available.';
}
```

```bash
# Install fileinfo extension on Ubuntu/Debian
sudo apt-get install php-fileinfo

# Verify fileinfo is loaded
php -m | grep fileinfo

# Check for magic database files
ls -la /usr/share/misc/magic*
```

### Fix 2: Use Default Magic Database

```php
function safeFinfo(string $path = null): ?finfo {
    if (!extension_loaded('fileinfo')) {
        error_log('fileinfo extension is not installed');
        return null;
    }

    if ($path !== null && file_exists($path)) {
        $finfo = @new finfo(FILEINFO_MIME_TYPE, $path);
    } else {
        $finfo = @new finfo(FILEINFO_MIME_TYPE);
    }

    if ($finfo === null) {
        error_log('Failed to create finfo instance');
        return null;
    }

    return $finfo;
}
```

### Fix 3: Check Magic Database Path

```bash
# Find magic database on the system
find / -name "magic.mgc" 2>/dev/null
find / -name "magic" -type f 2>/dev/null

# Typical locations:
# /usr/share/misc/magic.mgc
# /usr/share/file/misc/magic
# /usr/local/share/misc/magic.mgc
```

```php
function getMagicDatabasePath(): ?string {
    $possiblePaths = [
        '/usr/share/misc/magic.mgc',
        '/usr/share/file/misc/magic',
        '/usr/local/share/misc/magic.mgc',
        '/usr/share/misc/magic',
    ];

    foreach ($possiblePaths as $path) {
        if (file_exists($path) && is_readable($path)) {
            return $path;
        }
    }

    return null;
}

$magicPath = getMagicDatabasePath();
if ($magicPath !== null) {
    $finfo = new finfo(FILEINFO_MIME_TYPE, $magicPath);
} else {
    // Use default (no explicit path)
    $finfo = new finfo(FILEINFO_MIME_TYPE);
}
```

### Fix 4: Fallback Without fileinfo

```php
function getMimeTypeFallback(string $filePath): string {
    if (extension_loaded('fileinfo')) {
        $finfo = new finfo(FILEINFO_MIME_TYPE);
        $mimeType = $finfo->file($filePath);
        if ($mimeType !== false) {
            return $mimeType;
        }
    }

    // Fallback: guess from extension
    $extensions = [
        'jpg' => 'image/jpeg',
        'jpeg' => 'image/jpeg',
        'png' => 'image/png',
        'gif' => 'image/gif',
        'pdf' => 'application/pdf',
        'txt' => 'text/plain',
        'html' => 'text/html',
        'css' => 'text/css',
        'js' => 'application/javascript',
    ];

    $ext = strtolower(pathinfo($filePath, PATHINFO_EXTENSION));
    return $extensions[$ext] ?? 'application/octet-stream';
}
```

## Examples

```php
// Example: Safe MIME type detection with multiple fallbacks
function detectMimeType(string $filePath): string {
    if (!file_exists($filePath)) {
        return 'application/octet-stream';
    }

    // Method 1: fileinfo (preferred)
    if (extension_loaded('fileinfo')) {
        $finfo = new finfo(FILEINFO_MIME_TYPE);
        $mimeType = $finfo->file($filePath);
        if ($mimeType !== false && $mimeType !== 'application/octet-stream') {
            return $mimeType;
        }
    }

    // Method 2: file extension
    $ext = strtolower(pathinfo($filePath, PATHINFO_EXTENSION));
    $mimeTypes = [
        'jpg' => 'image/jpeg',
        'png' => 'image/png',
        'gif' => 'image/gif',
        'webp' => 'image/webp',
        'pdf' => 'application/pdf',
    ];

    if (isset($mimeTypes[$ext])) {
        return $mimeTypes[$ext];
    }

    // Method 3: Check file header bytes
    $handle = fopen($filePath, 'rb');
    if ($handle !== false) {
        $header = fread($handle, 8);
        fclose($handle);

        if (str_starts_with($header, "\x89PNG")) return 'image/png';
        if (str_starts_with($header, "\xFF\xD8\xFF")) return 'image/jpeg';
        if (str_starts_with($header, "GIF8")) return 'image/gif';
        if (str_starts_with($header, "RIFF") && substr($header, 8, 4) === 'WEBP') return 'image/webp';
        if (str_starts_with($header, "%PDF")) return 'application/pdf';
    }

    return 'application/octet-stream';
}
```

## Related Errors

- [finfo::file() returns false](/languages/php/finfo-file-error/)
- [MIME detection error](/languages/php/mime-detection-error/)
- [file read error](/languages/php/file-read-error/)
