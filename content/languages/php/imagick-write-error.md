---
title: "[Solution] PHP Imagick writeImage() Failed — Cannot Write Image"
description: "Fix PHP Imagick writeImage() failed by checking directory permissions, verifying disk space, and checking image format support. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 3
---

# PHP Imagick writeImage() Failed — Cannot Write Image

The `writeImage()` method failed because Imagick cannot write the processed image to the specified output path. This is commonly caused by insufficient directory permissions, lack of disk space, or unsupported output formats.

## Common Causes

```php
// Cause 1: Output directory does not exist
$img = new Imagick('input.jpg');
$img->writeImage('/nonexistent/dir/output.jpg');

// Cause 2: No write permission on directory
$img = new Imagick('input.jpg');
$img->writeImage('/var/protected/output.jpg'); // Permission denied

// Cause 3: Insufficient disk space
$img = new Imagick('large-input.tiff');
$img->writeImage('/tmp/output.tiff'); // Disk full

// Cause 4: Unsupported output format
$img = new Imagick('input.jpg');
$img->setImageFormat('xyz');
$img->writeImage('output.xyz'); // Unknown format

// Cause 5: File already open by another process
$img = new Imagick('input.jpg');
$img->writeImage('/tmp/locked-file.jpg'); // File locked
```

## How to Fix

### Fix 1: Verify Directory Exists and Is Writable

```php
function safeWriteImage(Imagick $img, string $outputPath): bool {
    $dir = dirname($outputPath);

    if (!is_dir($dir)) {
        $created = mkdir($dir, 0755, true);
        if (!$created) {
            error_log("Failed to create directory: {$dir}");
            return false;
        }
    }

    if (!is_writable($dir)) {
        error_log("Directory not writable: {$dir}");
        return false;
    }

    try {
        $img->writeImage($outputPath);
        return true;
    } catch (ImagickException $e) {
        error_log('writeImage failed: ' . $e->getMessage());
        return false;
    }
}
```

### Fix 2: Check Available Disk Space

```php
function writeImageWithDiskCheck(Imagick $img, string $outputPath): bool {
    $dir = dirname($outputPath);
    $freeSpace = disk_free_space($dir);

    // Estimate output size (rough approximation: width * height * 3 bytes)
    $imageSize = $img->getImageWidth() * $img->getImageHeight() * 3;

    if ($freeSpace !== false && $freeSpace < $imageSize * 2) {
        error_log("Insufficient disk space. Need ~{$imageSize} bytes, have {$freeSpace} bytes.");
        return false;
    }

    try {
        $img->writeImage($outputPath);
        return true;
    } catch (ImagickException $e) {
        error_log('writeImage failed: ' . $e->getMessage());
        return false;
    }
}
```

### Fix 3: Use Temporary File for Atomic Writes

```php
function atomicWriteImage(Imagick $img, string $outputPath): bool {
    $dir = dirname($outputPath);
    $tmpFile = tempnam($dir, 'img_');

    if ($tmpFile === false) {
        error_log('Failed to create temporary file');
        return false;
    }

    try {
        $img->writeImage($tmpFile);

        if (rename($tmpFile, $outputPath)) {
            return true;
        }

        error_log('Failed to rename temporary file to target');
        unlink($tmpFile);
        return false;
    } catch (ImagickException $e) {
        error_log('writeImage failed: ' . $e->getMessage());
        if (file_exists($tmpFile)) {
            unlink($tmpFile);
        }
        return false;
    }
}
```

### Fix 4: Validate Output Format Support

```php
function writeImageWithFormatCheck(Imagick $img, string $outputPath): bool {
    $supportedFormats = ['JPEG', 'PNG', 'GIF', 'WEBP', 'BMP', 'TIFF'];
    $format = strtoupper(pathinfo($outputPath, PATHINFO_EXTENSION));

    if (!in_array($format, $supportedFormats)) {
        error_log("Unsupported output format: {$format}");
        return false;
    }

    try {
        $img->setImageFormat($format);
        $img->writeImage($outputPath);
        return true;
    } catch (ImagickException $e) {
        error_log('writeImage failed: ' . $e->getMessage());
        return false;
    }
}
```

## Examples

```php
// Example: Complete image save pipeline
function saveProcessedImage(string $inputPath, string $outputPath, array $options = []): bool {
    $defaults = [
        'quality' => 85,
        'maxWidth' => 1920,
        'maxHeight' => 1080,
        'format' => null,
    ];
    $options = array_merge($defaults, $options);

    try {
        $img = new Imagick($inputPath);
        $img->autoOrientImage();

        // Resize if necessary
        $width = $img->getImageWidth();
        $height = $img->getImageHeight();

        if ($width > $options['maxWidth'] || $height > $options['maxHeight']) {
            $img->resizeImage(
                $options['maxWidth'],
                $options['maxHeight'],
                Imagick::FILTER_LANCZOS,
                1,
                true
            );
        }

        $img->setImageCompressionQuality($options['quality']);

        if ($options['format'] !== null) {
            $img->setImageFormat($options['format']);
        }

        $img->stripImage(); // Remove metadata

        $dir = dirname($outputPath);
        if (!is_dir($dir)) {
            mkdir($dir, 0755, true);
        }

        $img->writeImage($outputPath);
        $img->destroy();

        return true;
    } catch (ImagickException $e) {
        error_log('Image save failed: ' . $e->getMessage());
        return false;
    }
}
```

## Related Errors

- [ImagickException](/languages/php/imagick-exception/)
- [Imagick readImage() failed](/languages/php/imagick-read-error/)
- [Imagick Memory allocation failed](/languages/php/imagick-memory-error/)
