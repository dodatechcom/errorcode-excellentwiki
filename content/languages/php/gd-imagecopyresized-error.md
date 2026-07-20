---
title: "[Solution] PHP imagecopyresized() Failed — Image Resize Error"
description: "Fix PHP imagecopyresized() failed by verifying source image, checking destination size, and validating coordinates. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 8
---

# PHP imagecopyresized() Failed — Image Resize Error

The `imagecopyresized()` or `imagecopyresampled()` function failed during an image resize operation. This occurs when the source image is invalid, destination dimensions are incorrect, or coordinates are out of bounds.

## Common Causes

```php
// Cause 1: Source image is not a valid resource
$src = false;
$dst = imagecreatetruecolor(100, 100);
imagecopyresized($dst, $src, 0, 0, 0, 0, 100, 100, 200, 200); // $src is false

// Cause 2: Invalid destination dimensions
$src = imagecreatefromjpeg('photo.jpg');
$dst = imagecreatetruecolor(0, 0); // Zero-size destination
imagecopyresized($dst, $src, 0, 0, 0, 0, 0, 0, imagesx($src), imagesy($src));

// Cause 3: Source coordinates exceed image bounds
$src = imagecreatefromjpeg('photo.jpg');
$dst = imagecreatetruecolor(100, 100);
imagecopyresized($dst, $src, 0, 0, 5000, 5000, 100, 100, imagesx($src), imagesy($src));

// Cause 4: Negative or mixed dimensions
$dst = imagecreatetruecolor(100, 100);
imagecopyresized($dst, $src, 0, 0, 0, 0, -100, -100, 200, 200);

// Cause 5: Memory exceeded during resize
$dst = imagecreatetruecolor(10000, 10000); // Allocates too much memory
```

## How to Fix

### Fix 1: Validate Source and Destination Images

```php
function safeImageResize(GdImage $src, int $newWidth, int $newHeight): ?GdImage {
    $srcWidth = imagesx($src);
    $srcHeight = imagesy($src);

    if ($srcWidth === false || $srcHeight === false) {
        error_log('Invalid source image dimensions');
        return null;
    }

    if ($newWidth <= 0 || $newHeight <= 0) {
        error_log("Invalid destination dimensions: {$newWidth}x{$newHeight}");
        return null;
    }

    $dst = imagecreatetruecolor($newWidth, $newHeight);
    if ($dst === false) {
        error_log('Failed to create destination image');
        return null;
    }

    imagecopyresampled($dst, $src, 0, 0, 0, 0, $newWidth, $newHeight, $srcWidth, $srcHeight);

    return $dst;
}
```

### Fix 2: Clamp Coordinates to Image Bounds

```php
function safeImageCrop(GdImage $src, int $x, int $y, int $width, int $height): ?GdImage {
    $srcWidth = imagesx($src);
    $srcHeight = imagesy($src);

    // Clamp coordinates to valid range
    $x = max(0, min($x, $srcWidth - 1));
    $y = max(0, min($y, $srcHeight - 1));
    $width = min($width, $srcWidth - $x);
    $height = min($height, $srcHeight - $y);

    if ($width <= 0 || $height <= 0) {
        error_log("Invalid crop region after clamping: {$width}x{$height}");
        return null;
    }

    $dst = imagecreatetruecolor($width, $height);
    if ($dst === false) {
        return null;
    }

    imagecopyresampled($dst, $src, 0, 0, $x, $y, $width, $height, $width, $height);

    return $dst;
}
```

### Fix 3: Calculate Resize with Aspect Ratio

```php
function resizeWithAspectRatio(GdImage $src, int $maxWidth, int $maxHeight): ?GdImage {
    $srcWidth = imagesx($src);
    $srcHeight = imagesy($src);

    if ($srcWidth === false || $srcHeight === false) {
        return null;
    }

    $ratio = min($maxWidth / $srcWidth, $maxHeight / $srcHeight);

    if ($ratio >= 1.0) {
        $newWidth = $srcWidth;
        $newHeight = $srcHeight;
    } else {
        $newWidth = (int)($srcWidth * $ratio);
        $newHeight = (int)($srcHeight * $ratio);
    }

    if ($newWidth <= 0 || $newHeight <= 0) {
        return null;
    }

    $dst = imagecreatetruecolor($newWidth, $newHeight);
    if ($dst === false) {
        return null;
    }

    imagecopyresampled($dst, $src, 0, 0, 0, 0, $newWidth, $newHeight, $srcWidth, $srcHeight);

    return $dst;
}
```

## Examples

```php
// Example: Complete image resize pipeline
function resizeAndSaveImage(string $inputPath, string $outputPath, int $maxWidth, int $maxHeight, int $quality = 85): bool {
    if (!file_exists($inputPath)) {
        error_log("Input file not found: {$inputPath}");
        return false;
    }

    $src = @imagecreatefromjpeg($inputPath);
    if ($src === false) {
        error_log("Failed to load image: {$inputPath}");
        return false;
    }

    $dst = resizeWithAspectRatio($src, $maxWidth, $maxHeight);
    imagedestroy($src);

    if ($dst === false) {
        error_log('Resize failed');
        return false;
    }

    $result = imagejpeg($dst, $outputPath, $quality);
    imagedestroy($dst);

    if ($result === false) {
        error_log("Failed to save image: {$outputPath}");
        return false;
    }

    return true;
}
```

## Related Errors

- [GD imagecreate() failed](/languages/php/gd-imagecreate-error/)
- [GD imagecreatefromjpeg() failed](/languages/php/gd-imagecreatefrom-jpeg-error/)
- [GD imagecreatefrompng() failed](/languages/php/gd-imagecreatefrom-png-error/)
- [Imagick writeImage() failed](/languages/php/imagick-write-error/)
