---
title: "[Solution] PHP Warning: imagecreatefromjpeg() — Failed to read image"
description: "Fix PHP Warning: imagecreatefromjpeg() Failed to read. Check file path, verify format, check GD extension, validate file."
languages: ["php"]
severities: ["warning"]
error-types: ["runtime-error"]
weight: 102
---

# PHP Warning: imagecreatefromjpeg() — Failed to read image

This warning means PHP's GD library could not create an image resource from the specified JPEG file. It typically occurs when the file does not exist, is not a valid JPEG, or the GD extension is not loaded.

## Common Causes

```php
// Cause 1: File does not exist at the specified path
<?php
$img = imagecreatefromjpeg("/path/to/nonexistent/image.jpg");
// Warning: imagecreatefromjpeg(): Failed to read
?>
```

```php
// Cause 2: File exists but is not a valid JPEG
<?php
rename("photo.png", "photo.jpg");
$img = imagecreatefromjpeg("photo.jpg");
// Warning — file content is PNG, not JPEG
?>
```

```php
// Cause 3: GD extension not loaded
<?php
if (!extension_loaded('gd')) {
    die("GD extension is not available");
}
$img = imagecreatefromjpeg("photo.jpg");
?>
```

```php
// Cause 4: File permissions prevent reading
<?php
chmod("photo.jpg", 0000); // No permissions
$img = imagecreatefromjpeg("photo.jpg");
?>
```

```php
// Cause 5: File is corrupted or incomplete upload
<?php
$img = imagecreatefromjpeg("/tmp/partial-upload.jpg");
// Warning — file is truncated or corrupt
?>
```

## How to Fix

### Fix 1: Check File Path Before Processing

Always verify the file exists and is readable before calling `imagecreatefromjpeg()`.

```php
<?php
$filePath = "/uploads/photo.jpg";

if (!file_exists($filePath)) {
    die("Image file not found: {$filePath}");
}

if (!is_readable($filePath)) {
    die("Image file is not readable: {$filePath}");
}

$img = imagecreatefromjpeg($filePath);
if ($img === false) {
    die("Failed to create image from: {$filePath}");
}
?>
```

### Fix 2: Verify Image Format

Detect the actual file type using `getimagesize()` or `finfo`.

```php
<?php
$filePath = "/uploads/photo.jpg";

$info = getimagesize($filePath);
if ($info === false) {
    die("File is not a valid image");
}

$mimeType = $info['mime'];
$allowedTypes = ['image/jpeg', 'image/png', 'image/gif'];

if (!in_array($mimeType, $allowedTypes)) {
    die("Unsupported image type: {$mimeType}");
}

if ($mimeType === 'image/jpeg') {
    $img = imagecreatefromjpeg($filePath);
} elseif ($mimeType === 'image/png') {
    $img = imagecreatefrompng($filePath);
} elseif ($mimeType === 'image/gif') {
    $img = imagecreatefromgif($filePath);
}
?>
```

### Fix 3: Check and Enable the GD Extension

Ensure the GD extension is installed and enabled.

```php
<?php
// Check if GD is loaded
if (!extension_loaded('gd')) {
    echo "GD extension is not loaded.\n";
    echo "Install with: sudo apt-get install php-gd\n";
    echo "Then restart your web server.";
    exit(1);
}

// Check for specific format support
$gdInfo = gd_info();
if (!$gdInfo['JPEG Support']) {
    echo "JPEG support is not available in GD.\n";
}
?>
```

### Fix 4: Validate and Sanitize File Uploads

Ensure uploaded files are valid before processing them.

```php
<?php
function processUpload(array $file): void
{
    if ($file['error'] !== UPLOAD_ERR_OK) {
        die("Upload error: " . $file['error']);
    }

    $finfo = new finfo(FILEINFO_MIME_TYPE);
    $mimeType = $finfo->file($file['tmp_name']);

    if ($mimeType !== 'image/jpeg') {
        die("Uploaded file is not a JPEG: {$mimeType}");
    }

    $img = imagecreatefromjpeg($file['tmp_name']);
    if ($img === false) {
        die("Failed to process uploaded image");
    }

    // Process the image
    imagejpeg($img, "/uploads/processed.jpg", 85);
    imagedestroy($img);
}

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['photo'])) {
    processUpload($_FILES['photo']);
}
?>
```

## Examples

```php
<?php
// Safe image processing wrapper
function loadJpegImage(string $path): GdImage|false
{
    if (!file_exists($path)) {
        error_log("Image not found: {$path}");
        return false;
    }

    $size = @getimagesize($path);
    if ($size === false || $size['mime'] !== 'image/jpeg') {
        error_log("Invalid JPEG: {$path}");
        return false;
    }

    $img = imagecreatefromjpeg($path);
    if ($img === false) {
        error_log("GD failed to load: {$path}");
        return false;
    }

    return $img;
}

$img = loadJpegImage("/uploads/photo.jpg");
if ($img !== false) {
    // Resize or manipulate
    $width = imagesx($img);
    $height = imagesy($img);
    echo "Loaded image: {$width}x{$height}";
    imagedestroy($img);
}
?>
```

## Related Errors

- [PHP Warning: imagecreatefrompng()](/languages/php/warning-imagemanager-failed)
- [PHP Warning: Imagick Not Read](/languages/php/warning-imagick-not-read)
- [PHP Warning: File Read Error](/languages/php/file-read-error)
