---
title: "[Solution] PHP UPLOAD_ERR_FORM_SIZE — File Exceeds MAX_FILE_SIZE"
description: "Fix PHP UPLOAD_ERR_FORM_SIZE (error code 2) by updating MAX_FILE_SIZE, using chunked uploads, and validating client-side."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 129
---

# PHP UPLOAD_ERR_FORM_SIZE (Error Code 2) — File Exceeds MAX_FILE_SIZE

The uploaded file exceeds the `MAX_FILE_SIZE` hidden field value in the HTML form. This is a client-side limit that PHP enforces during upload. The `MAX_FILE_SIZE` value must appear before the file input field in the form and is set by the developer, not the user.

## Common Causes

```php
<?php
// Cause 1: MAX_FILE_SIZE set too low in HTML form
// <input type="hidden" name="MAX_FILE_SIZE" value="1048576"> <!-- 1MB -->
// User tries to upload a 5MB file

// Cause 2: MAX_FILE_SIZE field missing or set to 0
// No MAX_FILE_SIZE hidden field means no form-level size limit
// But server upload_max_filesize still applies

// Cause 3: MAX_FILE_SIZE placed after file input (ignored by PHP)
// Wrong: <input type="file" name="upload">
//        <input type="hidden" name="MAX_FILE_SIZE" value="1048576">

// Cause 4: Client-side validation bypassed
// JavaScript validation removed or disabled, relying only on MAX_FILE_SIZE

// Cause 5: Mismatch between MAX_FILE_SIZE and server limits
// MAX_FILE_SIZE = 50MB but upload_max_filesize = 2M
// User sees UPLOAD_ERR_INI_SIZE instead of UPLOAD_ERR_FORM_SIZE
?>
```

## How to Fix

### Fix 1: Update MAX_FILE_SIZE to appropriate value

```html
<!-- MAX_FILE_SIZE must appear BEFORE the file input field -->
<form action="upload.php" method="post" enctype="multipart/form-data">
    <!-- Set to desired max size in bytes (e.g., 10MB = 10485760) -->
    <input type="hidden" name="MAX_FILE_SIZE" value="10485760">
    <input type="file" name="document">
    <input type="submit" value="Upload">
</form>
```

### Fix 2: Use chunked uploads to bypass form size limits

```php
<?php
// upload_chunk.php
$fileName = $_POST['filename'] ?? 'upload.bin';
$chunkNumber = (int)($_POST['chunk'] ?? 0);
$totalChunks = (int)($_POST['chunks'] ?? 1);
$targetDir = __DIR__ . '/uploads/temp/' . session_id();

if (!is_dir($targetDir)) {
    mkdir($targetDir, 0755, true);
}

$targetFile = $targetDir . '/' . basename($fileName);
$out = fopen($targetFile, $chunkNumber === 0 ? 'wb' : 'ab');
$in = fopen($_FILES['chunk']['tmp_name'], 'rb');

if ($out && $in) {
    while ($buff = fread($in, 4096)) {
        fwrite($out, $buff);
    }
    fclose($in);
    fclose($out);
}

// If last chunk, move to final location
if ($chunkNumber === $totalChunks - 1) {
    $finalPath = __DIR__ . '/uploads/' . basename($fileName);
    rename($targetFile, $finalPath);
    rmdir($targetDir);
    echo json_encode(['status' => 'complete', 'path' => $finalPath]);
} else {
    echo json_encode(['status' => 'partial', 'chunk' => $chunkNumber]);
}
?>
```

### Fix 3: Add client-side validation as a first line of defense

```html
<form action="upload.php" method="post" enctype="multipart/form-data" id="uploadForm">
    <input type="hidden" name="MAX_FILE_SIZE" value="10485760">
    <input type="file" name="document" id="fileInput">
    <span id="fileError" style="color: red;"></span>
    <input type="submit" value="Upload" id="submitBtn">
</form>

<script>
document.getElementById('uploadForm').addEventListener('submit', function(e) {
    const file = document.getElementById('fileInput').files[0];
    const maxSize = parseInt(document.querySelector('input[name="MAX_FILE_SIZE"]').value);
    const errorEl = document.getElementById('fileError');

    if (file && file.size > maxSize) {
        e.preventDefault();
        const maxMB = (maxSize / 1048576).toFixed(1);
        errorEl.textContent = `File is too large. Maximum size is ${maxMB}MB.`;
        return false;
    }
    errorEl.textContent = '';
});
</script>
```

## Examples

```php
<?php
// Complete upload handler with MAX_FILE_SIZE error handling
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['document'])) {
    $file = $_FILES['document'];

    switch ($file['error']) {
        case UPLOAD_ERR_OK:
            $maxFileSize = (int)(new DOMDocument())
                ->loadHTML(file_get_contents('php://input'))
                ->getElementsByTagName('input')[0]->getAttribute('value');

            if ($file['size'] > 0) {
                $dest = __DIR__ . '/uploads/' . time() . '_' . basename($file['name']);
                if (move_uploaded_file($file['tmp_name'], $dest)) {
                    echo "Upload successful: {$dest}";
                } else {
                    echo "Failed to move uploaded file.";
                }
            }
            break;

        case UPLOAD_ERR_FORM_SIZE:
            $maxSize = ini_get('post_max_size');
            echo "File exceeds the form's MAX_FILE_SIZE limit. Server allows up to {$maxSize}.";
            break;

        case UPLOAD_ERR_INI_SIZE:
            echo "File exceeds server upload_max_filesize limit of " . ini_get('upload_max_filesize');
            break;

        default:
            echo "Upload error code: {$file['error']}";
    }
}
?>
```

## Related Errors

- [UPLOAD_ERR_INI_SIZE](/languages/php/upload-err-ini-size) — File exceeds upload_max_filesize in php.ini
- [UPLOAD_ERR_PARTIAL](/languages/php/upload-err-partial) — Only partial file was uploaded
- [UPLOAD_ERR_NO_FILE](/languages/php/upload-err-no-file) — No file was uploaded
