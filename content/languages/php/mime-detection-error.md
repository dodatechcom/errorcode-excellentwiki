---
title: "[Solution] PHP Incorrect MIME Type Detection"
description: "Fix PHP incorrect MIME type detection by checking magic database, using finfo_buffer(), and verifying file content. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 17
---

# PHP Incorrect MIME Type Detection

The MIME type detected for a file does not match its actual content. This happens when the magic database is outdated, the detection method relies on file extensions instead of content, or the file has been misidentified.

## Common Causes

```php
// Cause 1: Relying on file extension only
$mimeType = mime_content_type('photo.jpg'); // May return wrong type

// Cause 2: Outdated magic database
$finfo = new finfo(FILEINFO_MIME_TYPE);
$mimeType = $finfo->file('new-format.webp'); // May not recognize WebP

// Cause 3: Empty or corrupted file
$finfo = new finfo(FILEINFO_MIME_TYPE);
$mimeType = $finfo->file('corrupted.jpg'); // Returns generic type

// Cause 4: Mismatched file extension and content
rename('photo.png', 'photo.jpg');
$finfo = new finfo(FILEINFO_MIME_TYPE);
$mimeType = $finfo->file('photo.jpg'); // Returns image/png despite .jpg extension

// Cause 5: Binary file with ambiguous header
$finfo = new finfo(FILEINFO_MIME_TYPE);
$mimeType = $finfo->file('data.bin'); // Returns application/octet-stream
```

## How to Fix

### Fix 1: Use Content-Based Detection Instead of Extension

```php
function detectMimeTypeByContent(string $filePath): string {
    if (!file_exists($filePath) || filesize($filePath) === 0) {
        return 'application/octet-stream';
    }

    $handle = fopen($filePath, 'rb');
    if ($handle === false) {
        return 'application/octet-stream';
    }

    $header = fread($handle, 16);
    fclose($handle);

    // Check file signatures
    $signatures = [
        "\x89PNG" => 'image/png',
        "\xFF\xD8\xFF" => 'image/jpeg',
        'GIF87a' => 'image/gif',
        'GIF89a' => 'image/gif',
        "RIFF" => 'image/webp', // RIFF....WEBP
        "II\x2A\x00" => 'image/tiff',
        "MM\x00\x2A" => 'image/tiff',
        '%PDF' => 'application/pdf',
        'PK' => 'application/zip',
        "\x1F\x8B" => 'application/gzip',
    ];

    foreach ($signatures as $sig => $mime) {
        if (str_starts_with($header, $sig)) {
            if ($sig === "RIFF" && strlen($header) >= 12 && substr($header, 8, 4) === 'WEBP') {
                return 'image/webp';
            }
            return $mime;
        }
    }

    return 'application/octet-stream';
}
```

### Fix 2: Use finfo_buffer() for In-Memory Data

```php
function detectMimeTypeFromData(string $data): string {
    if (empty($data)) {
        return 'application/x-empty';
    }

    if (!extension_loaded('fileinfo')) {
        return detectMimeTypeByContentString($data);
    }

    $finfo = new finfo(FILEINFO_MIME_TYPE);
    $mimeType = $finfo->buffer($data);

    return $mimeType !== false ? $mimeType : 'application/octet-stream';
}

function detectMimeTypeByContentString(string $data): string {
    if (str_starts_with($data, "\x89PNG")) return 'image/png';
    if (str_starts_with($data, "\xFF\xD8\xFF")) return 'image/jpeg';
    if (str_starts_with($data, 'GIF8')) return 'image/gif';
    if (str_starts_with($data, '%PDF')) return 'application/pdf';
    if (str_starts_with($data, 'PK')) return 'application/zip';

    return 'application/octet-stream';
}
```

### Fix 3: Cross-Validate Detection Methods

```php
function crossValidateMimeType(string $filePath): array {
    $results = [];

    // Method 1: finfo
    if (extension_loaded('fileinfo')) {
        $finfo = new finfo(FILEINFO_MIME_TYPE);
        $results['finfo'] = $finfo->file($filePath) ?: 'unknown';
    }

    // Method 2: mime_content_type
    if (function_exists('mime_content_type')) {
        $results['mime_content_type'] = mime_content_type($filePath) ?: 'unknown';
    }

    // Method 3: File signature
    $results['signature'] = detectMimeTypeByContent($filePath);

    // Method 4: File extension
    $ext = strtolower(pathinfo($filePath, PATHINFO_EXTENSION));
    $extMap = [
        'jpg' => 'image/jpeg', 'jpeg' => 'image/jpeg',
        'png' => 'image/png', 'gif' => 'image/gif',
        'webp' => 'image/webp', 'pdf' => 'application/pdf',
    ];
    $results['extension'] = $extMap[$ext] ?? "application/{$ext}";

    // Report mismatches
    $unique = array_unique(array_values($results));
    $results['consistent'] = count($unique) <= 1;

    return $results;
}
```

### Fix 4: Update Magic Database

```bash
# Update file database on Ubuntu/Debian
sudo update-file /usr/share/misc/magic

# Or install latest libmagic
sudo apt-get install libmagic1

# Verify magic database version
file --version

# Test MIME detection
file --mime-type /path/to/file
```

## Examples

```php
// Example: Secure file upload validator
function validateUploadedFile(string $tmpPath, array $allowedTypes): array {
    $result = ['valid' => false, 'mime' => null, 'error' => null];

    if (!file_exists($tmpPath)) {
        $result['error'] = 'File does not exist';
        return $result;
    }

    $finfo = new finfo(FILEINFO_MIME_TYPE);
    $detectedMime = $finfo->file($tmpPath);

    if ($detectedMime === false) {
        $result['error'] = 'Could not detect MIME type';
        return $result;
    }

    $result['mime'] = $detectedMime;

    if (!in_array($detectedMime, $allowedTypes, true)) {
        $result['error'] = "MIME type {$detectedMime} not in allowed list";
        return $result;
    }

    // Cross-validate with file signature
    $signatureMime = detectMimeTypeByContent($tmpPath);
    if ($signatureMime !== $detectedMime && $signatureMime !== 'application/octet-stream') {
        $result['error'] = "MIME mismatch: finfo={$detectedMime}, signature={$signatureMime}";
        return $result;
    }

    $result['valid'] = true;
    return $result;
}

$allowed = ['image/jpeg', 'image/png', 'image/gif', 'image/webp'];
$uploadResult = validateUploadedFile('/tmp/uploaded_photo.jpg', $allowed);
```

## Related Errors

- [finfo::finfo() failed to load magic database](/languages/php/finfo-load-error/)
- [finfo::file() returns false](/languages/php/finfo-file-error/)
- [file read error](/languages/php/file-read-error/)
