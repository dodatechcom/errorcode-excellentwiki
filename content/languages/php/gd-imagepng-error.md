---
title: "[Solution] PHP imagepng() Output Failed — Cannot Write PNG"
description: "Fix PHP imagepng() output failed by checking directory permissions, verifying compression level, and handling disk space. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 8
---

# PHP imagepng() Output Failed — Cannot Write PNG

The `imagepng()` function failed to write a PNG image to disk. This happens when the target directory doesn't exist, is not writable, the compression level is invalid, or disk space is exhausted.

## Common Causes

```php
// Cause 1: Target directory does not exist
imagepng($img, '/nonexistent/path/image.png');

// Cause 2: Directory not writable
imagepng($img, '/readonly/images/image.png');

// Cause 3: Invalid compression level (must be 0-9)
imagepng($img, 'image.png', 15);

// Cause 4: Disk space full
imagepng($img, '/full-disk/image.png');

// Cause 5: Invalid image resource
$invalidImg = false;
imagepng($invalidImg, 'image.png'); // Not a GdImage resource
```

## How to Fix

### Fix 1: Validate Directory Before Writing

```php
function safeImagepng(GdImage $img, string $path, int $compression = 6): bool {
    $dir = dirname($path);

    if (!is_dir($dir)) {
        if (!mkdir($dir, 0755, true)) {
            error_log("Failed to create directory: {$dir}");
            return false;
        }
    }

    if (!is_writable($dir)) {
        error_log("Directory not writable: {$dir}");
        return false;
    }

    $compression = max(0, min(9, $compression));

    $result = @imagepng($img, $path, $compression);

    if ($result === false) {
        error_log("imagepng failed to write: {$path}");
        return false;
    }

    return true;
}
```

### Fix 2: Check Disk Space Before Writing

```php
function hasSufficientDiskSpace(string $path, int $estimatedBytes = 2097152): bool {
    $dir = dirname($path);
    $freeSpace = disk_free_space($dir);

    if ($freeSpace === false) {
        error_log("Could not determine free disk space for: {$dir}");
        return false;
    }

    return $freeSpace > $estimatedBytes;
}
```

### Fix 3: Validate Image Resource and Compression

```php
function writePngWithValidation(GdImage $img, string $path, int $compression = 6): bool {
    if (!($img instanceof GdImage)) {
        error_log('Invalid image resource provided');
        return false;
    }

    $width = imagesx($img);
    $height = imagesy($img);

    if ($width <= 0 || $height <= 0) {
        error_log('Image has invalid dimensions');
        return false;
    }

    $compression = max(0, min(9, (int)$compression));

    ob_start();
    $result = imagepng($img, null, $compression);
    $data = ob_get_clean();

    if ($result === false || $data === false) {
        error_log('imagepng failed to generate PNG data');
        return false;
    }

    return file_put_contents($path, $data) !== false;
}
```

### Fix 4: Stream PNG to Output with Proper Headers

```php
function outputPngToBrowser(GdImage $img, int $compression = 6): void {
    header('Content-Type: image/png');

    $compression = max(0, min(9, $compression));

    $result = imagepng($img, null, $compression);

    if ($result === false) {
        http_response_code(500);
        error_log('Failed to output PNG image');
    }
}
```

## Examples

```php
// Example: Generate PNG watermark overlay
function addPngWatermark(string $sourcePath, string $watermarkPath, string $outputPath): bool {
    $source = imagecreatefrompng($sourcePath);
    $watermark = imagecreatefrompng($watermarkPath);

    if ($source === false || $watermark === false) {
        return false;
    }

    $sourceWidth = imagesx($source);
    $sourceHeight = imagesy($source);
    $markWidth = imagesx($watermark);
    $markHeight = imagesy($watermark);

    $x = $sourceWidth - $markWidth - 20;
    $y = $sourceHeight - $markHeight - 20;

    imagecopy($source, $watermark, $x, $y, 0, 0, $markWidth, $markHeight);

    $result = safeImagepng($source, $outputPath);

    imagedestroy($source);
    imagedestroy($watermark);

    return $result;
}
```

## Related Errors

- [GD imagecreate() failed](/languages/php/gd-imagecreate-error/)
- [GD imagejpeg() output failed](/languages/php/gd-imagejpeg-error/)
- [Warning: fwrite() not writable](/languages/php/warning-fwrite-not-writable/)
