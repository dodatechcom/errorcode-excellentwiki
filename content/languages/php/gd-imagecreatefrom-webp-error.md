---
title: "[Solution] PHP imagecreatefromwebp() Failed — Cannot Read WebP"
description: "Fix PHP imagecreatefromwebp() failed by checking file path, verifying WebP format, installing libwebp, and checking GD support (PHP 7.4+). Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 7
---

# PHP imagecreatefromwebp() Failed — Cannot Read WebP

The `imagecreatefromwebp()` function failed to create an image resource from a WebP file. This happens when the file doesn't exist, is not a valid WebP, or when GD was compiled without WebP support. WebP support requires PHP 7.4+.

## Common Causes

```php
// Cause 1: File does not exist
$img = imagecreatefromwebp('/missing/photo.webp');

// Cause 2: File is not a valid WebP
$img = imagecreatefromwebp('document.txt');

// Cause 3: GD compiled without WebP support
$img = imagecreatefromwebp('valid-photo.webp'); // Returns false

// Cause 4: PHP version too old (requires 7.4+)
$img = imagecreatefromwebp('photo.webp'); // Function does not exist

// Cause 5: Corrupted WebP file
$img = imagecreatefromwebp('damaged.webp'); // Partial file
```

## How to Fix

### Fix 1: Check GD WebP Support and PHP Version

```php
if (PHP_VERSION_ID < 70400) {
    echo 'WebP support requires PHP 7.4 or later.';
} elseif (function_exists('imagecreatefromwebp')) {
    $gdInfo = gd_info();
    if ($gdInfo['WebP Support']) {
        echo 'WebP support is enabled.';
    } else {
        echo 'WebP support is NOT enabled in GD.';
    }
} else {
    echo 'imagecreatefromwebp() is not available.';
}
```

```bash
# Install GD with WebP support on Ubuntu/Debian
sudo apt-get install php-gd libwebp-dev

# Verify WebP support
php -r 'print_r(gd_info());' | grep WebP
```

### Fix 2: Validate File Before Reading

```php
function safeImagecreatefromwebp(string $path): ?GdImage {
    if (!function_exists('imagecreatefromwebp')) {
        error_log('imagecreatefromwebp() requires PHP 7.4+');
        return null;
    }

    $realPath = realpath($path);

    if ($realPath === false || !file_exists($realPath)) {
        error_log("WebP file not found: {$path}");
        return null;
    }

    if (!is_readable($realPath)) {
        error_log("WebP file not readable: {$realPath}");
        return null;
    }

    $finfo = new finfo(FILEINFO_MIME_TYPE);
    $mimeType = $finfo->file($realPath);

    if ($mimeType !== 'image/webp') {
        error_log("File is not WebP (got {$mimeType}): {$realPath}");
        return null;
    }

    $img = imagecreatefromwebp($realPath);
    if ($img === false) {
        error_log("imagecreatefromwebp failed: {$realPath}");
        return null;
    }

    return $img;
}
```

### Fix 3: Handle WebP Error Suppression

```php
function readWebpWithErrorHandling(string $path): ?GdImage {
    if (!function_exists('imagecreatefromwebp')) {
        return null;
    }

    if (!file_exists($path)) {
        return null;
    }

    $img = @imagecreatefromwebp($path);

    if ($img === false) {
        error_log("Failed to create image from WebP: {$path}");
        return null;
    }

    return $img;
}
```

### Fix 4: Check libwebp Installation

```bash
# Check if libwebp is installed
dpkg -l | grep libwebp

# Install libwebp on Ubuntu/Debian
sudo apt-get install libwebp-dev

# Reinstall PHP GD extension
sudo apt-get install --reinstall php-gd

# Restart web server
sudo systemctl restart apache2
# or
sudo systemctl restart php-fpm
```

## Examples

```php
// Example: WebP thumbnail generator (PHP 7.4+)
function createWebpThumbnail(string $inputPath, string $outputPath, int $maxSize = 150): bool {
    if (!function_exists('imagecreatefromwebp')) {
        error_log('WebP support requires PHP 7.4+');
        return false;
    }

    $img = safeImagecreatefromwebp($inputPath);
    if ($img === false) {
        return false;
    }

    $origWidth = imagesx($img);
    $origHeight = imagesy($img);

    $ratio = min($maxSize / $origWidth, $maxSize / $origHeight);
    $newWidth = (int)($origWidth * $ratio);
    $newHeight = (int)($origHeight * $ratio);

    $thumb = imagecreatetruecolor($newWidth, $newHeight);
    imagecopyresampled($thumb, $img, 0, 0, 0, 0, $newWidth, $newHeight, $origWidth, $origHeight);

    $result = imagewebp($thumb, $outputPath, 80);

    imagedestroy($img);
    imagedestroy($thumb);

    return $result !== false;
}
```

## Related Errors

- [GD imagecreate() failed](/languages/php/gd-imagecreate-error/)
- [GD imagecreatefromjpeg() failed](/languages/php/gd-imagecreatefrom-jpeg-error/)
- [GD imagecreatefromgif() failed](/languages/php/gd-imagecreatefrom-gif-error/)
