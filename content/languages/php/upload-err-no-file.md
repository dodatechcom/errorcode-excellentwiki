---
title: "[Solution] PHP UPLOAD_ERR_NO_FILE — No File Was Uploaded"
description: "Fix PHP UPLOAD_ERR_NO_FILE (error code 4) by checking form enctype, verifying file input name, and handling empty uploads."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 131
---

# PHP UPLOAD_ERR_NO_FILE (Error Code 4) — No File Was Uploaded

No file was uploaded. The form was submitted but the file input field contained no file, or the form was not submitted as a `multipart/form-data` request. This is the most common upload error and is often caused by misconfigured forms.

## Common Causes

```php
<?php
// Cause 1: Missing enctype="multipart/form-data" on the form
// <form action="upload.php" method="post">
// <!-- Missing enctype attribute means file data is not sent -->

// Cause 2: File input name mismatch
// HTML: <input type="file" name="my_file">
// PHP:  $_FILES['upload']  // Wrong key — should be 'my_file'

// Cause 3: File input is disabled or not included in form
// <input type="file" name="document" disabled>

// Cause 4: Form submitted via JavaScript without file input data
// fetch('upload.php', { method: 'POST', body: formData })
// But formData doesn't include the file

// Cause 5: User submits form without selecting a file
// No validation to ensure a file was selected before submission
?>
```

## How to Fix

### Fix 1: Ensure form uses multipart/form-data enctype

```html
<!-- Correct: enctype must be multipart/form-data for file uploads -->
<form action="upload.php" method="post" enctype="multipart/form-data">
    <input type="file" name="document" required>
    <input type="submit" value="Upload">
</form>
```

### Fix 2: Verify file input name matches PHP key

```php
<?php
// upload.php
// Match the name attribute from your HTML form exactly

// HTML: <input type="file" name="user_avatar">
// PHP must access: $_FILES['user_avatar']

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Debug: see what was actually received
    if (empty($_FILES)) {
        echo "No files received. Check:\n";
        echo "1. Form enctype is 'multipart/form-data'\n";
        echo "2. File input has a 'name' attribute\n";
        echo "3. $_POST data: " . print_r(array_keys($_POST), true) . "\n";
        exit;
    }

    echo "Received files: " . print_r(array_keys($_FILES), true);
}
?>
```

### Fix 3: Handle empty uploads gracefully

```php
<?php
function uploadFile(array $file, string $uploadDir = __DIR__ . '/uploads'): array {
    // Check for no file uploaded
    if ($file['error'] === UPLOAD_ERR_NO_FILE) {
        return [
            'success' => false,
            'error' => 'No file was uploaded. Please select a file.',
            'code' => UPLOAD_ERR_NO_FILE
        ];
    }

    // Check for other errors first
    if ($file['error'] !== UPLOAD_ERR_OK) {
        return [
            'success' => false,
            'error' => 'Upload error: ' . uploadErrorMessage($file['error']),
            'code' => $file['error']
        ];
    }

    // Validate file was actually uploaded (size > 0)
    if ($file['size'] === 0) {
        return [
            'success' => false,
            'error' => 'Uploaded file is empty (0 bytes).'
        ];
    }

    // Validate file type
    $allowedTypes = ['image/jpeg', 'image/png', 'image/gif', 'application/pdf'];
    $finfo = new finfo(FILEINFO_MIME_TYPE);
    $mimeType = $finfo->file($file['tmp_name']);

    if (!in_array($mimeType, $allowedTypes, true)) {
        return [
            'success' => false,
            'error' => "File type '{$mimeType}' is not allowed."
        ];
    }

    // Move to destination
    if (!is_dir($uploadDir)) {
        mkdir($uploadDir, 0755, true);
    }

    $dest = $uploadDir . '/' . time() . '_' . basename($file['name']);
    if (move_uploaded_file($file['tmp_name'], $dest)) {
        return ['success' => true, 'path' => $dest, 'type' => $mimeType];
    }

    return ['success' => false, 'error' => 'Failed to move uploaded file.'];
}

function uploadErrorMessage(int $code): string {
    return match ($code) {
        UPLOAD_ERR_INI_SIZE   => 'File exceeds server upload limit.',
        UPLOAD_ERR_FORM_SIZE  => 'File exceeds form size limit.',
        UPLOAD_ERR_PARTIAL    => 'File was only partially uploaded.',
        UPLOAD_ERR_CANT_WRITE => 'Failed to write file to disk.',
        UPLOAD_ERR_NO_TMP_DIR => 'Missing temporary upload directory.',
        UPLOAD_ERR_EXTENSION  => 'Upload stopped by a PHP extension.',
        default               => 'Unknown upload error.'
    };
}
?>
```

### Fix 4: Validate file selection before form submission

```html
<form action="upload.php" method="post" enctype="multipart/form-data" id="uploadForm">
    <input type="file" name="document" id="fileInput" required>
    <button type="submit">Upload</button>
</form>

<script>
document.getElementById('uploadForm').addEventListener('submit', function(e) {
    const fileInput = document.getElementById('fileInput');
    if (!fileInput.files.length) {
        e.preventDefault();
        alert('Please select a file before uploading.');
        return false;
    }
});
</script>
```

## Examples

```php
<?php
// Complete form handler that detects all common UPLOAD_ERR_NO_FILE causes
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Check if any files were sent at all
    if (empty($_FILES)) {
        $contentType = $_SERVER['CONTENT_TYPE'] ?? '';
        if (strpos($contentType, 'multipart/form-data') === false) {
            echo "Error: Form must use enctype='multipart/form-data'.";
        } else {
            echo "Error: No file input found in form submission.";
            echo "Received POST keys: " . implode(', ', array_keys($_POST));
        }
        exit;
    }

    $file = $_FILES['document'] ?? null;
    if (!$file) {
        echo "Error: File input name mismatch. Available: " . implode(', ', array_keys($_FILES));
        exit;
    }

    if ($file['error'] === UPLOAD_ERR_NO_FILE) {
        echo "No file selected. Please choose a file to upload.";
        exit;
    }

    if ($file['error'] === UPLOAD_ERR_OK && $file['size'] > 0) {
        $dest = __DIR__ . '/uploads/' . basename($file['name']);
        if (move_uploaded_file($file['tmp_name'], $dest)) {
            echo "File uploaded successfully: {$dest}";
        } else {
            echo "Failed to save uploaded file.";
        }
    }
}
?>
```

## Related Errors

- [UPLOAD_ERR_INI_SIZE](/languages/php/upload-err-ini-size) — File exceeds upload_max_filesize
- [UPLOAD_ERR_FORM_SIZE](/languages/php/upload-err-form-size) — File exceeds MAX_FILE_SIZE hidden field
- [UPLOAD_ERR_PARTIAL](/languages/php/upload-err-partial) — Only partial file was uploaded
