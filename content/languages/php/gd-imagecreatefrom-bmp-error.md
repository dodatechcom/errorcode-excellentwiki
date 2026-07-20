---
title: "[Solution] PHP imagecreatefrombmp() Failed — Cannot Read BMP"
description: "Fix PHP imagecreatefrombmp() failed by checking file path, verifying BMP format, and checking GD support (PHP 7.4+). Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 7
---

# PHP imagecreatefrombmp() Failed — Cannot Read BMP

The `imagecreatefrombmp()` function failed to create an image resource from a BMP file. This happens when the file doesn't exist, is not a valid BMP, or when GD was compiled without BMP support. BMP support requires PHP 7.4+.

## Common Causes

```php
// Cause 1: File does not exist
$img = imagecreatefrombmp('/missing/photo.bmp');

// Cause 2: File is not a valid BMP
$img = imagecreatefrombmp('document.txt');

// Cause 3: GD compiled without BMP support
$img = imagecreatefrombmp('valid-photo.bmp'); // Returns false

// Cause 4: PHP version too old (requires 7.4+)
$img = imagecreatefrombmp('photo.bmp'); // Function does not exist

// Cause 5: Corrupted BMP file
$img = imagecreatefrombmp('damaged.bmp'); // Partial file
```

## How to Fix

### Fix 1: Check GD BMP Support and PHP Version

```php
if (PHP_VERSION_ID < 70400) {
    echo 'BMP support requires PHP 7.4 or later.';
} elseif (function_exists('imagecreatefrombmp')) {
    echo 'imagecreatefrombmp() is available.';
} else {
    echo 'imagecreatefrombmp() is not available in your PHP version.';
}
```

```bash
# BMP support is included in GD for PHP 7.4+
# Install or upgrade GD on Ubuntu/Debian
sudo apt-get install php-gd

# Verify PHP version
php -v

# Verify BMP support (no separate flag in gd_info)
php -r 'var_dump(function_exists("imagecreatefrombmp"));'
```

### Fix 2: Validate File Before Reading

```php
function safeImagecreatefrombmp(string $path): ?GdImage {
    if (!function_exists('imagecreatefrombmp')) {
        error_log('imagecreatefrombmp() requires PHP 7.4+');
        return null;
    }

    $realPath = realpath($path);

    if ($realPath === false || !file_exists($realPath)) {
        error_log("BMP file not found: {$path}");
        return null;
    }

    if (!is_readable($realPath)) {
        error_log("BMP file not readable: {$realPath}");
        return null;
    }

    $finfo = new finfo(FILEINFO_MIME_TYPE);
    $mimeType = $finfo->file($realPath);

    if ($mimeType !== 'image/bmp' && $mimeType !== 'image/x-ms-bmp') {
        error_log("File is not BMP (got {$mimeType}): {$realPath}");
        return null;
    }

    $img = imagecreatefrombmp($realPath);
    if ($img === false) {
        error_log("imagecreatefrombmp failed: {$realPath}");
        return null;
    }

    return $img;
}
```

### Fix 3: Handle BMP Error Suppression

```php
function readBmpWithErrorHandling(string $path): ?GdImage {
    if (!function_exists('imagecreatefrombmp')) {
        return null;
    }

    if (!file_exists($path)) {
        return null;
    }

    $img = @imagecreatefrombmp($path);

    if ($img === false) {
        error_log("Failed to create image from BMP: {$path}");
        return null;
    }

    return $img;
}
```

### Fix 4: Provide Fallback for Older PHP Versions

```php
function readBmpWithFallback(string $path): ?GdImage {
    if (function_exists('imagecreatefrombmp')) {
        return imagecreatefrombmp($path);
    }

    // Attempt to convert BMP to PNG using Imagick as fallback
    if (class_exists('Imagick')) {
        try {
            $imagick = new Imagick($path);
            $imagick->setImageFormat('png');
            $pngData = $imagick->getImageBlob();

            $tmpFile = tempnam(sys_get_temp_dir(), 'bmp_');
            file_put_contents($tmpFile, $pngData);
            $img = imagecreatefrompng($tmpFile);
            unlink($tmpFile);

            return $img;
        } catch (Exception $e) {
            error_log("Imagick fallback failed: " . $e->getMessage());
        }
    }

    error_log('BMP support requires PHP 7.4+ or Imagick extension');
    return null;
}
```

## Examples

```php
// Example: BMP to JPEG converter
function convertBmpToJpeg(string $inputPath, string $outputPath, int $quality = 85): bool {
    $img = safeImagecreatefrombmp($inputPath);
    if ($img === false) {
        return false;
    }

    $result = imagejpeg($img, $outputPath, $quality);

    imagedestroy($img);

    return $result !== false;
}
```

## Related Errors

- [GD imagecreate() failed](/languages/php/gd-imagecreate-error/)
- [GD imagecreatefromjpeg() failed](/languages/php/gd-imagecreatefrom-jpeg-error/)
- [GD imagecreatefromgif() failed](/languages/php/gd-imagecreatefrom-gif-error/)
