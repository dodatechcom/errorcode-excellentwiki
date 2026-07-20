---
title: "[Solution] PHP UPLOAD_ERR_PARTIAL — Partial File Upload"
description: "Fix PHP UPLOAD_ERR_PARTIAL (error code 3) by increasing max_execution_time, using chunked uploads, and checking network stability."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 130
---

# PHP UPLOAD_ERR_PARTIAL (Error Code 3) — Partial File Upload

Only a partial file was uploaded. The server stopped receiving the file before the entire file was transmitted. This typically happens when the upload takes too long and hits execution time limits, the connection drops, or the client disconnects prematurely.

## Common Causes

```php
<?php
// Cause 1: max_execution_time exceeded during upload
// Default is 30 seconds; large file on slow connection exceeds this
// PHP terminates the upload mid-transfer

// Cause 2: max_input_time exceeded
// Default is -1 (unlimited) on some systems, but may be set to a finite value
// Time spent receiving POST data exceeds the limit

// Cause 3: Network interruption or timeout
// Client connection drops during large file transfer
// Proxy or load balancer timeout kills the connection

// Cause 4: Client-side timeout or abort
// User navigates away or closes browser during upload
// JavaScript XMLHttpRequest or fetch timeout triggers

// Cause 5: Server resource limits
// Memory limit exhausted during upload processing
// max_file_uploads reached for concurrent uploads
?>
```

## How to Fix

### Fix 1: Increase max_execution_time and max_input_time

```ini
; php.ini
max_execution_time = 300      ; 5 minutes (0 = unlimited in CLI)
max_input_time = 300          ; 5 minutes (-1 = unlimited)
memory_limit = 256M           ; Ensure enough memory for large uploads
```

Or at runtime:

```php
<?php
// Set before upload processing (may not work if server restricts ini_set)
ini_set('max_execution_time', '300');
ini_set('max_input_time', '300');

// Check current values
echo "max_execution_time: " . ini_get('max_execution_time') . "\n";
echo "max_input_time: " . ini_get('max_input_time') . "\n";
echo "memory_limit: " . ini_get('memory_limit') . "\n";
?>
```

### Fix 2: Use chunked uploads to avoid timeout issues

```php
<?php
// upload_chunk.php
header('Content-Type: application/json');

$uploadDir = __DIR__ . '/uploads/chunks/';
if (!is_dir($uploadDir)) {
    mkdir($uploadDir, 0755, true);
}

$fileId = $_POST['file_id'] ?? bin2hex(random_bytes(16));
$chunkIndex = (int)($_POST['chunk_index'] ?? 0);
$totalChunks = (int)($_POST['total_chunks'] ?? 1);
$fileName = $_POST['file_name'] ?? 'upload.bin';

$chunkFile = $uploadDir . $fileId . '_' . $chunkIndex;
move_uploaded_file($_FILES['chunk']['tmp_name'], $chunkFile);

$uploadedChunks = glob($uploadDir . $fileId . '_*');
if (count($uploadedChunks) === $totalChunks) {
    // All chunks received, assemble file
    $finalFile = __DIR__ . '/uploads/' . basename($fileName);
    $out = fopen($finalFile, 'wb');
    for ($i = 0; $i < $totalChunks; $i++) {
        $chunkPath = $uploadDir . $fileId . '_' . $i;
        $in = fopen($chunkPath, 'rb');
        while ($buff = fread($in, 8192)) {
            fwrite($out, $buff);
        }
        fclose($in);
        unlink($chunkPath);
    }
    fclose($out);
    echo json_encode(['status' => 'complete', 'path' => $finalFile]);
} else {
    echo json_encode([
        'status' => 'partial',
        'received' => count($uploadedChunks),
        'total' => $totalChunks
    ]);
}
?>
```

### Fix 3: Increase max_input_time and add keep-alive

```php
<?php
// upload.php
ini_set('max_input_time', '600');
ini_set('max_execution_time', '600');

// Send keep-alive header to prevent proxy timeouts
header('Connection: keep-alive');

// Process the upload
if ($_FILES['document']['error'] === UPLOAD_ERR_PARTIAL) {
    echo json_encode([
        'error' => 'Partial upload. Check network connection and try again.',
        'bytes_received' => $_FILES['document']['size']
    ]);
    exit;
}

if ($_FILES['document']['error'] === UPLOAD_ERR_OK) {
    $dest = __DIR__ . '/uploads/' . basename($_FILES['document']['name']);
    if (move_uploaded_file($_FILES['document']['tmp_name'], $dest)) {
        echo json_encode(['success' => true, 'path' => $dest]);
    }
}
?>
```

### Fix 4: Validate upload completion and retry on client side

```javascript
// Client-side retry logic for partial uploads
async function uploadWithRetry(file, url, maxRetries = 3) {
    for (let attempt = 1; attempt <= maxRetries; attempt++) {
        try {
            const formData = new FormData();
            formData.append('document', file);

            const response = await fetch(url, {
                method: 'POST',
                body: formData,
                signal: AbortSignal.timeout(300000) // 5 minute timeout
            });

            const result = await response.json();
            if (result.success) return result;

            console.warn(`Attempt ${attempt} failed, retrying...`);
        } catch (err) {
            console.warn(`Attempt ${attempt} error:`, err.message);
            if (attempt === maxRetries) throw err;
        }
    }
}
```

## Examples

```php
<?php
// Robust upload handler with partial upload detection
function processUpload(array $file): array {
    switch ($file['error']) {
        case UPLOAD_ERR_OK:
            $dest = __DIR__ . '/uploads/' . basename($file['name']);
            if (move_uploaded_file($file['tmp_name'], $dest)) {
                return ['success' => true, 'path' => $dest, 'size' => $file['size']];
            }
            return ['success' => false, 'error' => 'Failed to move file to destination.'];

        case UPLOAD_ERR_PARTIAL:
            $received = $file['size'];
            return [
                'success' => false,
                'error' => "Partial upload: only {$received} bytes received before connection was interrupted.",
                'suggestion' => 'Try chunked upload or increase max_execution_time.'
            ];

        case UPLOAD_ERR_INI_SIZE:
            $maxSize = ini_get('upload_max_filesize');
            return ['success' => false, 'error' => "File exceeds server limit of {$maxSize}."];

        default:
            return ['success' => false, 'error' => "Upload error code: {$file['error']}"];
    }
}

// Usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    header('Content-Type: application/json');
    echo json_encode(processUpload($_FILES['upload']));
}
?>
```

## Related Errors

- [UPLOAD_ERR_INI_SIZE](/languages/php/upload-err-ini-size) — File exceeds upload_max_filesize
- [UPLOAD_ERR_NO_FILE](/languages/php/upload-err-no-file) — No file was uploaded
- [UPLOAD_ERR_CANT_WRITE](/languages/php/upload-err-cant-write) — Failed to write to disk
