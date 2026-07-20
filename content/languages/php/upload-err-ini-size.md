---
title: "[Solution] PHP UPLOAD_ERR_INI_SIZE — File Exceeds upload_max_filesize"
description: "Fix PHP UPLOAD_ERR_INI_SIZE (error code 1) by increasing upload_max_filesize, using chunked uploads, and checking post_max_size."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 128
---

# PHP UPLOAD_ERR_INI_SIZE (Error Code 1) — File Exceeds upload_max_filesize

The uploaded file exceeds the `upload_max_filesize` directive in `php.ini`. This error occurs when a user tries to upload a file larger than the maximum allowed size configured on the server. The default value is typically 2M (2 megabytes).

## Common Causes

```php
<?php
// Cause 1: File exceeds default upload_max_filesize (2M)
// User uploads a 10MB file with default php.ini settings

// Cause 2: upload_max_filesize too small for application needs
$uploadedSize = $_FILES['document']['size']; // 5MB
// But upload_max_filesize = 2M in php.ini

// Cause 3: post_max_size smaller than upload_max_filesize
// post_max_size = 8M but trying to upload 10MB file

// Cause 4: Multiple file upload total exceeds limit
$totalSize = 0;
foreach ($_FILES['documents']['size'] as $size) {
    $totalSize += $size;
}
// Total exceeds upload_max_filesize

// Cause 5: Form data combined with file exceeds post_max_size
$formData = strlen(http_build_query($_POST)); // Large form data
$fileSize = $_FILES['file']['size'];
// Combined exceeds post_max_size
?>
```

## How to Fix

### Fix 1: Increase upload_max_filesize in php.ini

```ini
; php.ini
upload_max_filesize = 64M
post_max_size = 128M
```

Or set via `.htaccess`:

```apache
php_value upload_max_filesize 64M
php_value post_max_size 128M
```

Or via `.user.ini` (for CGI/FastCGI):

```ini
upload_max_filesize = 64M
post_max_size = 128M
```

### Fix 2: Use chunked uploads for large files

```php
<?php
// Frontend: Split file into chunks and upload sequentially
// upload.php
$chunk = $_POST['chunk'] ?? 0;
$chunks = $_POST['chunks'] ?? 0;
$fileName = $_POST['name'] ?? 'upload.bin';

$tmpFile = $_FILES['file']['tmp_name'];
$targetPath = __DIR__ . '/uploads/' . basename($fileName);

if ($chunks > 1) {
    // Append chunk to file
    $out = fopen($targetPath, $chunk === 0 ? 'wb' : 'ab');
    $in = fopen($tmpFile, 'rb');
    if ($out && $in) {
        while ($buff = fread($in, 4096)) {
            fwrite($out, $buff);
        }
        fclose($in);
        fclose($out);
    }
} else {
    move_uploaded_file($tmpFile, $targetPath);
}

echo json_encode(['status' => 'ok', 'chunk' => $chunk]);
?>
```

### Fix 3: Check and align post_max_size with upload_max_filesize

```php
<?php
// Validate before processing upload
$maxUpload = ini_get('upload_max_filesize'); // e.g., "2M"
$maxPost = ini_get('post_max_size');         // e.g., "8M"

$maxUploadBytes = returnBytes($maxUpload);
$maxPostBytes = returnBytes($maxPost);

if ($_FILES['file']['size'] > $maxUploadBytes) {
    die("File exceeds server upload limit of {$maxUpload}.");
}

function returnBytes(string $val): int {
    $val = trim($val);
    $last = strtolower($val[strlen($val) - 1]);
    $bytes = (int) $val;
    match ($last) {
        'g' => $bytes *= 1024 * 1024 * 1024,
        'm' => $bytes *= 1024 * 1024,
        'k' => $bytes *= 1024,
    };
    return $bytes;
}
?>
```

## Examples

```php
<?php
// Complete upload handler with size validation
function handleUpload(array $file, int $maxSizeBytes): array {
    if ($file['error'] === UPLOAD_ERR_INI_SIZE) {
        $maxSize = ini_get('upload_max_filesize');
        return [
            'success' => false,
            'error' => "File exceeds maximum upload size of {$maxSize}."
        ];
    }

    if ($file['error'] !== UPLOAD_ERR_OK) {
        return ['success' => false, 'error' => 'Upload failed with error: ' . $file['error']];
    }

    if ($file['size'] > $maxSizeBytes) {
        return ['success' => false, 'error' => 'File too large for this form.'];
    }

    $dest = __DIR__ . '/uploads/' . basename($file['name']);
    if (move_uploaded_file($file['tmp_name'], $dest)) {
        return ['success' => true, 'path' => $dest];
    }

    return ['success' => false, 'error' => 'Failed to move uploaded file.'];
}

// Usage
$result = handleUpload($_FILES['document'], 10 * 1024 * 1024); // 10MB limit
echo $result['success'] ? "Uploaded to {$result['path']}" : $result['error'];
?>
```

## Related Errors

- [UPLOAD_ERR_FORM_SIZE](/languages/php/upload-err-form-size) — File exceeds MAX_FILE_SIZE hidden field
- [UPLOAD_ERR_PARTIAL](/languages/php/upload-err-partial) — Only partial file was uploaded
- [UPLOAD_ERR_CANT_WRITE](/languages/php/upload-err-cant-write) — Failed to write file to disk
- [UPLOAD_ERR_NO_TMP_DIR](/languages/php/upload-err-no-tmp-dir) — Missing temporary folder
