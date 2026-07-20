---
title: "[Solution] PHP imagecreatefromavif() Failed — Cannot Read AVIF"
description: "Fix PHP imagecreatefromavif() failed by checking file path, verifying AVIF format, installing libavif, and checking GD support (PHP 8.1+). Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 7
---

# PHP imagecreatefromavif() Failed — Cannot Read AVIF

The `imagecreatefromavif()` function failed to create an image resource from an AVIF file. This happens when the file doesn't exist, is not a valid AVIF, or when GD was compiled without AVIF support. AVIF support requires PHP 8.1+.

## Common Causes

```php
// Cause 1: File does not exist
$img = imagecreatefromavif('/missing/photo.avif');

// Cause 2: File is not a valid AVIF
$img = imagecreatefromavif('document.txt');

// Cause 3: GD compiled without AVIF support
$img = imagecreatefromavif('valid-photo.avif'); // Returns false

// Cause 4: PHP version too old (requires 8.1+)
$img = imagecreatefromavif('photo.avif'); // Function does not exist

// Cause 5: Corrupted AVIF file
$img = imagecreatefromavif('damaged.avif'); // Partial file
```

## How to Fix

### Fix 1: Check GD AVIF Support and PHP Version

```php
if (PHP_VERSION_ID < 80100) {
    echo 'AVIF support requires PHP 8.1 or later.';
} elseif (function_exists('imagecreatefromavif')) {
    $gdInfo = gd_info();
    if ($gdInfo['AVIF Support'] ?? false) {
        echo 'AVIF support is enabled.';
    } else {
        echo 'AVIF support is NOT enabled in GD.';
    }
} else {
    echo 'imagecreatefromavif() is not available.';
}
```

```bash
# Check PHP version
php -v

# Install GD with AVIF support on Ubuntu/Debian (PHP 8.1+)
sudo apt-get install php8.1-gd libavif-dev

# Verify AVIF support
php -r 'print_r(gd_info());' | grep AVIF
```

### Fix 2: Validate File Before Reading

```php
function safeImagecreatefromavif(string $path): ?GdImage {
    if (!function_exists('imagecreatefromavif')) {
        error_log('imagecreatefromavif() requires PHP 8.1+');
        return null;
    }

    $realPath = realpath($path);

    if ($realPath === false || !file_exists($realPath)) {
        error_log("AVIF file not found: {$path}");
        return null;
    }

    if (!is_readable($realPath)) {
        error_log("AVIF file not readable: {$realPath}");
        return null;
    }

    $finfo = new finfo(FILEINFO_MIME_TYPE);
    $mimeType = $finfo->file($realPath);

    if ($mimeType !== 'image/avif') {
        error_log("File is not AVIF (got {$mimeType}): {$realPath}");
        return null;
    }

    $img = imagecreatefromavif($realPath);
    if ($img === false) {
        error_log("imagecreatefromavif failed: {$realPath}");
        return null;
    }

    return $img;
}
```

### Fix 3: Install libavif and Recompile GD

```bash
# Install libavif on Ubuntu/Debian
sudo apt-get install libavif-dev

# For PHP-FPM, restart the service
sudo systemctl restart php8.1-fpm

# For Apache
sudo systemctl restart apache2

# Verify AVIF is supported
php -r 'print_r(gd_info());'
```

```bash
# On CentOS/RHEL
sudo yum install libavif-devel

# Recompile PHP GD with AVIF support
# Check phpinfo() for configure command to see current GD flags
```

### Fix 4: Use Imagick Fallback for Older PHP

```php
function readAvifWithFallback(string $path): ?GdImage {
    // Try native GD support first (PHP 8.1+)
    if (function_exists('imagecreatefromavif')) {
        $img = @imagecreatefromavif($path);
        if ($img !== false) {
            return $img;
        }
    }

    // Fallback: use Imagick if available
    if (class_exists('Imagick')) {
        try {
            $imagick = new Imagick($path);
            $imagick->setImageFormat('png');
            $pngData = $imagick->getImageBlob();

            $tmpFile = tempnam(sys_get_temp_dir(), 'avif_');
            file_put_contents($tmpFile, $pngData);
            $img = imagecreatefrompng($tmpFile);
            unlink($tmpFile);

            return $img;
        } catch (Exception $e) {
            error_log("Imagick AVIF fallback failed: " . $e->getMessage());
        }
    }

    error_log('AVIF support requires PHP 8.1+ with libavif or Imagick extension');
    return null;
}
```

## Examples

```php
// Example: AVIF to PNG converter (PHP 8.1+)
function convertAvifToPng(string $inputPath, string $outputPath): bool {
    if (!function_exists('imagecreatefromavif')) {
        error_log('AVIF support requires PHP 8.1+');
        return false;
    }

    $img = safeImagecreatefromavif($inputPath);
    if ($img === false) {
        return false;
    }

    $result = imagepng($img, $outputPath);

    imagedestroy($img);

    return $result !== false;
}
```

## Related Errors

- [GD imagecreate() failed](/languages/php/gd-imagecreate-error/)
- [GD imagecreatefromjpeg() failed](/languages/php/gd-imagecreatefrom-jpeg-error/)
- [GD imagecreatefromwebp() failed](/languages/php/gd-imagecreatefrom-webp-error/)
