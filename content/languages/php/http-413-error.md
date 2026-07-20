---
title: "[Solution] PHP HTTP 413 Request Entity Too Large — POST Body Exceeds Limits"
description: "Fix PHP HTTP 413 Request Entity Too Large: POST body exceeds limits. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1104
---

# PHP HTTP 413 Request Entity Too Large — POST Body Exceeds Limits

An HTTP 413 Request Entity Too Large error occurs when the client sends a request body (POST data or file upload) that exceeds the server's configured size limits. In PHP, this is governed by `post_max_size`, `upload_max_filesize`, and Nginx's `client_max_body_size` settings.

## Common Causes

```php
<?php
// Uploading a file larger than upload_max_filesize
// Form submission with large POST body exceeding post_max_size

// Checking current limits
echo ini_get('post_max_size');       // e.g., "8M"
echo ini_get('upload_max_filesize'); // e.g., "2M"
echo ini_get('max_file_uploads');    // e.g., 20

// $_POST and $_FILES will be empty if post_max_size is exceeded
if (empty($_POST) && $_SERVER['REQUEST_METHOD'] === 'POST') {
    // Likely hit post_max_size limit
    echo "Request body too large";
}
```

## How to Fix

### Fix 1: Increase post_max_size in php.ini

```ini
; php.ini — increase POST body size limit
; This affects all POST data including form submissions
post_max_size = 64M

; Also increase upload-specific limits
upload_max_filesize = 64M
max_file_uploads = 50
```

```php
<?php
// Set at runtime (must be done before any output)
ini_set('post_max_size', '64M');
ini_set('upload_max_filesize', '64M');
// Note: ini_set may not work for post_max_size in all environments
// Prefer php.ini or .user.ini for these settings
```

### Fix 2: Increase Nginx client_max_body_size

```nginx
# nginx.conf — in http, server, or location block
http {
    client_max_body_size 64M;
}

server {
    client_max_body_size 64M;

    location /upload {
        client_max_body_size 128M;
    }
}
```

### Fix 3: Increase Apache LimitRequestBody

```apache
# Apache .htaccess or httpd.conf
# Limit in bytes: 64MB = 67108864
<IfModule mod_php.c>
    php_value post_max_size 64M
    php_value upload_max_filesize 64M
</IfModule>

# Apache directive (in bytes)
LimitRequestBody 67108864
```

### Fix 4: Use Chunked File Uploads for Large Files

```php
<?php
// Handle large files with chunked uploads
// Client-side: split file into chunks and send via AJAX

// Server-side: receive and assemble chunks
function receiveChunkedUpload(string $uploadDir, int $totalChunks): array
{
    $chunkIndex = (int) ($_POST['chunk_index'] ?? 0);
    $totalChunks = (int) ($_POST['total_chunks'] ?? 1);
    $fileId = preg_replace('/[^a-zA-Z0-9_-]/', '', $_POST['file_id'] ?? '');

    if (empty($fileId)) {
        http_response_code(400);
        return ['error' => 'Invalid file ID'];
    }

    $chunkDir = $uploadDir . '/chunks/' . $fileId;

    if (!is_dir($chunkDir)) {
        mkdir($chunkDir, 0755, true);
    }

    // Save individual chunk
    $chunkPath = $chunkDir . '/' . $chunkIndex;
    move_uploaded_file($_FILES['chunk']['tmp_name'], $chunkPath);

    // If all chunks received, assemble the file
    if ($chunkIndex === $totalChunks - 1) {
        $finalPath = $uploadDir . '/' . ($_POST['filename'] ?? 'uploaded_file');
        $out = fopen($finalPath, 'wb');

        for ($i = 0; $i < $totalChunks; $i++) {
            $chunk = $chunkDir . '/' . $i;
            $in = fopen($chunk, 'rb');
            stream_copy_to_stream($in, $out);
            fclose($in);
            unlink($chunk);
        }

        fclose($out);
        rmdir($chunkDir);

        return ['success' => true, 'path' => $finalPath];
    }

    return ['success' => true, 'chunk' => $chunkIndex];
}
```

### Fix 5: Validate and Handle Size Errors Gracefully

```php
<?php
function validateUpload(): array
{
    $maxUploadSize = ini_get('upload_max_filesize');
    $maxPostSize = ini_get('post_max_size');

    if (empty($_FILES)) {
        // Check if post_max_size was exceeded
        if ($_SERVER['REQUEST_METHOD'] === 'POST'
            && (empty($_POST) && file_get_contents('php://input') === '')) {
            return [
                'error' => "Maximum POST size exceeded ({$maxPostSize})",
                'code'  => 413,
            ];
        }
        return ['error' => 'No file uploaded'];
    }

    $file = $_FILES['upload'] ?? null;
    if ($file === null) {
        return ['error' => 'No upload field found'];
    }

    if ($file['error'] === UPLOAD_ERR_INI_SIZE) {
        return [
            'error' => "File exceeds upload_max_filesize ({$maxUploadSize})",
            'code'  => 413,
        ];
    }

    if ($file['error'] === UPLOAD_ERR_FORM_SIZE) {
        return [
            'error' => "File exceeds MAX_FILE_SIZE in form",
            'code'  => 413,
        ];
    }

    if ($file['error'] !== UPLOAD_ERR_OK) {
        return ['error' => 'Upload error: ' . $file['error']];
    }

    return ['success' => true, 'file' => $file];
}

// Usage
$result = validateUpload();
if (isset($result['error'])) {
    http_response_code($result['code'] ?? 400);
    echo json_encode($result);
    exit;
}
```

## Examples

```php
<?php
// Example 1: Form with file upload
// HTML form:
// <form method="POST" enctype="multipart/form-data" action="/upload.php">
//   <input type="hidden" name="MAX_FILE_SIZE" value="10485760">
//   <input type="file" name="document">
//   <button type="submit">Upload</button>
// </form>

// upload.php
function handleUpload(): void
{
    $maxSize = 10 * 1024 * 1024; // 10MB

    if (!isset($_FILES['document'])) {
        http_response_code(400);
        echo json_encode(['error' => 'No file provided']);
        return;
    }

    $file = $_FILES['document'];

    if ($file['error'] !== UPLOAD_ERR_OK) {
        $errors = [
            UPLOAD_ERR_INI_SIZE   => 'File exceeds server size limit',
            UPLOAD_ERR_FORM_SIZE  => 'File exceeds form size limit',
            UPLOAD_ERR_PARTIAL    => 'File was only partially uploaded',
            UPLOAD_ERR_NO_FILE    => 'No file was uploaded',
            UPLOAD_ERR_NO_TMP_DIR => 'Missing temporary folder',
            UPLOAD_ERR_CANT_WRITE => 'Failed to write to disk',
        ];
        http_response_code(400);
        echo json_encode(['error' => $errors[$file['error']] ?? 'Unknown upload error']);
        return;
    }

    if ($file['size'] > $maxSize) {
        http_response_code(413);
        echo json_encode(['error' => 'File exceeds 10MB limit']);
        return;
    }

    $dest = '/var/www/uploads/' . basename($file['name']);
    move_uploaded_file($file['tmp_name'], $dest);

    http_response_code(200);
    echo json_encode(['success' => true, 'path' => $dest]);
}

handleUpload();

// Example 2: Check limits before submitting
function getUploadLimits(): array
{
    return [
        'post_max_size'       => ini_get('post_max_size'),
        'upload_max_filesize' => ini_get('upload_max_filesize'),
        'max_file_uploads'    => (int) ini_get('max_file_uploads'),
        'max_input_vars'      => (int) ini_get('max_input_vars'),
    ];
}

echo json_encode(getUploadLimits());
```

## Related Errors

- [PHP Upload Error]({{< relref "/languages/php/upload-error" >}})
- [PHP File Write Error]({{< relref "/languages/php/file-write-error" >}})
- [PHP Memory Exhausted]({{< relref "/languages/php/memory-exhausted" >}})
