---
title: "[Solution] PHP UPLOAD_ERR_CANT_WRITE — Failed to Write to Disk"
description: "Fix PHP UPLOAD_ERR_CANT_WRITE (error code 5) by checking upload_tmp_dir permissions, verifying disk space, and checking directory permissions."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 132
---

# PHP UPLOAD_ERR_CANT_WRITE (Error Code 5) — Failed to Write to Disk

Failed to write file to disk. This occurs after a successful upload transfer but when PHP cannot write the temporary file to the upload directory. The cause is typically permission issues on the temporary or upload directory, or insufficient disk space.

## Common Causes

```php
<?php
// Cause 1: upload_tmp_dir directory doesn't exist or has wrong permissions
// PHP cannot write temporary files to the configured upload_tmp_dir
// Default is often /tmp which may have restrictive permissions

// Cause 2: Destination directory permissions prevent move_uploaded_file()
// Target upload directory not writable by web server user (www-data, nginx, etc.)

// Cause 3: Disk is full
// Server has no remaining disk space for the uploaded file

// Cause 4: Disk quota exceeded
// Hosting account or user quota has been exceeded

// Cause 5: Filesystem is read-only
// Mounted filesystem became read-only due to errors or configuration
?>
```

## How to Fix

### Fix 1: Check and fix upload_tmp_dir permissions

```php
<?php
// Check current upload_tmp_dir
$tmpDir = ini_get('upload_tmp_dir') ?: sys_get_temp_dir();
echo "upload_tmp_dir: {$tmpDir}\n";
echo "Exists: " . (is_dir($tmpDir) ? 'yes' : 'no') . "\n";
echo "Writable: " . (is_writable($tmpDir) ? 'yes' : 'no') . "\n";
echo "Permissions: " . substr(sprintf('%o', fileperms($tmpDir)), -4) . "\n";

// Fix permissions via shell (run as root or with sudo)
// sudo chown www-data:www-data /tmp
// sudo chmod 1733 /tmp
?>
```

```bash
# Fix upload_tmp_dir permissions (run in terminal)
sudo chown www-data:www-data /tmp
sudo chmod 1777 /tmp

# Or set a custom upload_tmp_dir in php.ini
# upload_tmp_dir = /var/www/tmp
sudo mkdir -p /var/www/tmp
sudo chown www-data:www-data /var/www/tmp
sudo chmod 1777 /var/www/tmp
```

### Fix 2: Ensure destination directory is writable

```php
<?php
$uploadDir = __DIR__ . '/uploads';

if (!is_dir($uploadDir)) {
    if (!mkdir($uploadDir, 0755, true)) {
        die("Failed to create upload directory: {$uploadDir}");
    }
}

if (!is_writable($uploadDir)) {
    die("Upload directory is not writable: {$uploadDir}");
}

// Verify disk space
$freeSpace = disk_free_space($uploadDir);
$fileSize = $_FILES['document']['size'] ?? 0;

if ($freeSpace < $fileSize) {
    $freeMB = round($freeSpace / 1048576, 2);
    $neededMB = round($fileSize / 1048576, 2);
    die("Insufficient disk space. Available: {$freeMB}MB, needed: {$neededMB}MB");
}

// Proceed with upload
$dest = $uploadDir . '/' . basename($_FILES['document']['name']);
if (move_uploaded_file($_FILES['document']['tmp_name'], $dest)) {
    echo "Upload successful: {$dest}";
} else {
    echo "move_uploaded_file failed. Check disk space and permissions.";
}
?>
```

### Fix 3: Set a custom upload_tmp_dir in php.ini

```ini
; php.ini
upload_tmp_dir = /var/www/app/tmp/uploads
```

```bash
# Create and configure custom temp directory
sudo mkdir -p /var/www/app/tmp/uploads
sudo chown www-data:www-data /var/www/app/tmp/uploads
sudo chmod 1777 /var/www/app/tmp/uploads
```

### Fix 4: Monitor disk space and quotas

```php
<?php
function checkUploadPrerequisites(string $uploadDir, int $fileSize): array {
    $checks = [];

    // Check directory exists and is writable
    $checks['dir_exists'] = is_dir($uploadDir);
    $checks['dir_writable'] = is_writable($uploadDir);

    // Check tmp dir
    $tmpDir = ini_get('upload_tmp_dir') ?: sys_get_temp_dir();
    $checks['tmp_dir_exists'] = is_dir($tmpDir);
    $checks['tmp_dir_writable'] = is_writable($tmpDir);

    // Check disk space
    $freeSpace = disk_free_space($uploadDir);
    $checks['disk_free_bytes'] = $freeSpace;
    $checks['has_enough_space'] = $freeSpace > $fileSize;

    // Check disk total space
    $totalSpace = disk_total_space($uploadDir);
    $checks['disk_usage_percent'] = round((($totalSpace - $freeSpace) / $totalSpace) * 100, 2);

    $checks['all_ok'] = !in_array(false, $checks, true);

    return $checks;
}

// Usage before processing upload
if ($_FILES['document']['error'] === UPLOAD_ERR_CANT_WRITE) {
    $checks = checkUploadPrerequisites(__DIR__ . '/uploads', $_FILES['document']['size']);
    echo json_encode($checks, JSON_PRETTY_PRINT);
}
?>
```

## Examples

```php
<?php
// Full upload handler with disk error diagnostics
function safeUpload(array $file, string $destDir = __DIR__ . '/uploads'): array {
    if ($file['error'] === UPLOAD_ERR_CANT_WRITE) {
        $tmpDir = ini_get('upload_tmp_dir') ?: sys_get_temp_dir();

        $diagnostics = [
            'error' => 'Failed to write file to disk.',
            'tmp_dir' => $tmpDir,
            'tmp_dir_writable' => is_writable($tmpDir),
            'dest_dir' => $destDir,
            'dest_dir_writable' => is_dir($destDir) && is_writable($destDir),
            'disk_free_mb' => round(disk_free_space($destDir) / 1048576, 2),
            'file_size_mb' => round($file['size'] / 1048576, 2),
        ];

        // Try to fix permissions automatically
        if (!is_dir($destDir)) {
            mkdir($destDir, 0755, true);
            $diagnostics['created_dest_dir'] = true;
        }

        return ['success' => false, 'diagnostics' => $diagnostics];
    }

    if ($file['error'] !== UPLOAD_ERR_OK) {
        return ['success' => false, 'error' => "Upload error code: {$file['error']}"];
    }

    $dest = $destDir . '/' . basename($file['name']);
    if (move_uploaded_file($file['tmp_name'], $dest)) {
        return ['success' => true, 'path' => $dest];
    }

    return ['success' => false, 'error' => 'move_uploaded_file() failed.'];
}

// Usage
$result = safeUpload($_FILES['file']);
header('Content-Type: application/json');
echo json_encode($result, JSON_PRETTY_PRINT);
?>
```

## Related Errors

- [UPLOAD_ERR_NO_TMP_DIR](/languages/php/upload-err-no-tmp-dir) — Missing temporary folder
- [UPLOAD_ERR_PARTIAL](/languages/php/upload-err-partial) — Only partial file was uploaded
- [UPLOAD_ERR_EXTENSION](/languages/php/upload-err-extension) — Upload stopped by extension
