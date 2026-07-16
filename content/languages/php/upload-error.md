---
title: "PHP File Upload Error / Upload Failed"
description: "Fix PHP file upload errors. Learn to resolve upload_max_filesize, tmp directory issues, and common upload failures."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["upload", "file-upload", "upload-error", "multipart", "tmp"]
weight: 5
---

# PHP File Upload Error / Upload Failed

PHP file upload errors occur when the uploaded file cannot be processed. Errors are indicated by the `$_FILES['file']['error']` code or by exceeding PHP configuration limits.

## Common Causes

- File exceeds `upload_max_filesize` in php.ini
- POST data exceeds `post_max_size`
- Temporary directory is full or not writable
- Missing or incorrect `enctype="multipart/form-data"` in HTML form

## How to Fix

### Check Upload Error Code

```php
<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $error = $_FILES['upload']['error'];
    switch ($error) {
        case UPLOAD_ERR_INI_SIZE:
            echo 'File exceeds upload_max_filesize';
            break;
        case UPLOAD_ERR_FORM_SIZE:
            echo 'File exceeds MAX_FILE_SIZE';
            break;
        case UPLOAD_ERR_PARTIAL:
            echo 'File was only partially uploaded';
            break;
        case UPLOAD_ERR_NO_FILE:
            echo 'No file was uploaded';
            break;
        case UPLOAD_ERR_CANT_WRITE:
            echo 'Failed to write to disk';
            break;
        default:
            echo 'Unknown upload error: ' . $error;
    }
}
?>
```

### Increase Upload Limits in php.ini

```ini
upload_max_filesize = 64M
post_max_size = 128M
max_file_uploads = 20
max_execution_time = 300
```

### Ensure Proper Form Encoding

```html
<form method="POST" action="/upload" enctype="multipart/form-data">
    <input type="file" name="upload">
    <button type="submit">Upload</button>
</form>
```

### Fix Temporary Directory Permissions

```php
<?php
echo sys_get_temp_dir();
// Ensure this directory is writable by the web server
chmod(sys_get_temp_dir(), 0775);
?>
```

## Examples

```php
<?php
// Example 1: File too large
// $_FILES['upload']['error'] = UPLOAD_ERR_INI_SIZE
// Fix: increase upload_max_filesize in php.ini

// Example 2: Missing enctype
// <form method="POST" action="/upload"> <!-- Missing enctype -->
// $_FILES['upload'] is empty
// Fix: add enctype="multipart/form-data"

// Example 3: Move uploaded file
if ($_FILES['upload']['error'] === UPLOAD_ERR_OK) {
    $dest = '/uploads/' . basename($_FILES['upload']['name']);
    if (move_uploaded_file($_FILES['upload']['tmp_name'], $dest)) {
        echo 'Upload successful';
    } else {
        echo 'Failed to move uploaded file';
    }
}
?>
```

## Related Errors

- [PHP Fatal Error: Allowed memory size exhausted]({{< relref "/languages/php/fatal-error" >}})
- [PHP Cannot modify header information]({{< relref "/languages/php/headers-sent" >}})
- [PHP Warning: count()]({{< relref "/languages/php/warning-count" >}})
