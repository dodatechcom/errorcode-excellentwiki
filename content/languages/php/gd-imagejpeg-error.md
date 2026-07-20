---
title: "[Solution] PHP imagejpeg() Output Failed — Cannot Write JPEG"
description: "Fix PHP imagejpeg() output failed by checking directory permissions, verifying quality parameter, and handling disk space. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 8
---

# PHP imagejpeg() Output Failed — Cannot Write JPEG

The `imagejpeg()` function failed to write a JPEG image to disk. This happens when the target directory doesn't exist, is not writable, the quality parameter is invalid, or disk space is exhausted.

## Common Causes

```php
// Cause 1: Target directory does not exist
imagejpeg($img, '/nonexistent/path/photo.jpg', 85);

// Cause 2: Directory not writable
imagejpeg($img, '/readonly/photos/photo.jpg', 85);

// Cause 3: Invalid quality parameter
imagejpeg($img, 'photo.jpg', 150); // Quality must be 0-100

// Cause 4: Disk space full
imagejpeg($img, '/full-disk/photo.jpg', 85);

// Cause 5: Invalid image resource
$invalidImg = false;
imagejpeg($invalidImg, 'photo.jpg', 85); // Not a GdImage resource
```

## How to Fix

### Fix 1: Validate Directory Before Writing

```php
function safeImagejpeg(GdImage $img, string $path, int $quality = 85): bool {
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

    $quality = max(0, min(100, $quality));

    $result = @imagejpeg($img, $path, $quality);

    if ($result === false) {
        error_log("imagejpeg failed to write: {$path}");
        return false;
    }

    return true;
}
```

### Fix 2: Check Disk Space

```php
function hasSufficientDiskSpace(string $path, int $estimatedBytes = 1048576): bool {
    $dir = dirname($path);
    $freeSpace = disk_free_space($dir);

    if ($freeSpace === false) {
        error_log("Could not determine free disk space for: {$dir}");
        return false;
    }

    return $freeSpace > $estimatedBytes;
}
```

### Fix 3: Validate Quality Parameter

```php
function writeJpegWithValidation(GdImage $img, string $path, int $quality = 85): bool {
    if (!($img instanceof GdImage)) {
        error_log('Invalid image resource provided');
        return false;
    }

    $quality = max(0, min(100, (int)$quality));

    ob_start();
    $result = imagejpeg($img, null, $quality);
    $data = ob_get_clean();

    if ($result === false || $data === false) {
        error_log('imagejpeg failed to generate JPEG data');
        return false;
    }

    return file_put_contents($path, $data) !== false;
}
```

### Fix 4: Set Appropriate File Permissions

```php
function writeJpegWithPermissions(GdImage $img, string $path, int $quality = 85, int $mode = 0644): bool {
    $result = @imagejpeg($img, $path, $quality);

    if ($result === false) {
        error_log("imagejpeg failed: {$path}");
        return false;
    }

    chmod($path, $mode);

    return true;
}
```

## Examples

```php
// Example: Generate JPEG thumbnail and handle errors
function createAndSaveJpegThumbnail(
    GdImage $source,
    string $outputPath,
    int $maxWidth = 300,
    int $quality = 80
): bool {
    $origWidth = imagesx($source);
    $origHeight = imagesy($source);

    $ratio = min($maxWidth / $origWidth, 1.0);
    $newWidth = (int)($origWidth * $ratio);
    $newHeight = (int)($origHeight * $ratio);

    $thumb = imagecreatetruecolor($newWidth, $newHeight);
    imagecopyresampled($thumb, $source, 0, 0, 0, 0, $newWidth, $newHeight, $origWidth, $origHeight);

    $success = safeImagejpeg($thumb, $outputPath, $quality);

    imagedestroy($thumb);

    return $success;
}
```

## Related Errors

- [GD imagecreate() failed](/languages/php/gd-imagecreate-error/)
- [GD imagepng() output failed](/languages/php/gd-imagepng-error/)
- [Warning: fwrite() not writable](/languages/php/warning-fwrite-not-writable/)
