---
title: "[Solution] PHP UPLOAD_ERR_NO_TMP_DIR — Missing Temporary Folder"
description: "Fix PHP UPLOAD_ERR_NO_TMP_DIR (error code 6) by configuring upload_tmp_dir in php.ini, creating the temp directory, and checking permissions."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 133
---

# PHP UPLOAD_ERR_NO_TMP_DIR (Error Code 6) — Missing Temporary Folder

Missing temporary folder. PHP cannot find or access the temporary directory used to store uploaded files before they are moved to their final destination. This typically means the `upload_tmp_dir` directive is not configured or points to a non-existent directory.

## Common Causes

```php
<?php
// Cause 1: upload_tmp_dir not configured in php.ini
// PHP falls back to system default which may not exist or be accessible

// Cause 2: upload_tmp_dir points to a non-existent directory
// upload_tmp_dir = /var/www/tmp  but /var/www/tmp doesn't exist

// Cause 3: Temporary directory was deleted while server is running
// Deployment script or cleanup cron removed the temp directory

// Cause 4: open_basedir restriction prevents access to tmp dir
// PHP security restriction blocks access outside allowed paths

// Cause 5: SELinux or AppArmor blocks PHP from accessing the directory
// Security policies prevent the web server process from writing to tmp
?>
```

## How to Fix

### Fix 1: Configure upload_tmp_dir in php.ini

```ini
; php.ini
; Set a custom temporary directory for uploads
upload_tmp_dir = /var/www/app/tmp/uploads
```

```bash
# Create the directory and set proper ownership
sudo mkdir -p /var/www/app/tmp/uploads
sudo chown www-data:www-data /var/www/app/tmp/uploads
sudo chmod 1777 /var/www/app/tmp/uploads
```

### Fix 2: Create the temp directory if it doesn't exist

```php
<?php
function ensureUploadTmpDir(): string {
    $tmpDir = ini_get('upload_tmp_dir');

    if (empty($tmpDir)) {
        $tmpDir = sys_get_temp_dir();
    }

    if (!is_dir($tmpDir)) {
        if (!mkdir($tmpDir, 0755, true)) {
            throw new RuntimeException("Cannot create upload tmp directory: {$tmpDir}");
        }
    }

    if (!is_writable($tmpDir)) {
        throw new RuntimeException("Upload tmp directory is not writable: {$tmpDir}");
    }

    return $tmpDir;
}

// Call before processing uploads
try {
    $tmpDir = ensureUploadTmpDir();
    echo "Upload tmp dir ready: {$tmpDir}";
} catch (RuntimeException $e) {
    echo "Error: " . $e->getMessage();
}
?>
```

### Fix 3: Handle the error with a fallback temp directory

```php
<?php
function handleUploadWithFallback(array $file): array {
    if ($file['error'] === UPLOAD_ERR_NO_TMP_DIR) {
        // Try to create a fallback temp directory
        $fallbackDir = __DIR__ . '/tmp_uploads';

        if (!is_dir($fallbackDir)) {
            mkdir($fallbackDir, 0755, true);
        }

        // Update php.ini setting at runtime if allowed
        if (ini_set('upload_tmp_dir', $fallbackDir) !== false) {
            return [
                'success' => false,
                'error' => 'Temp directory missing. Created fallback and retry needed.',
                'fallback_dir' => $fallbackDir,
                'retry' => true
            ];
        }

        return [
            'success' => false,
            'error' => 'upload_tmp_dir is missing and cannot be set at runtime.',
            'suggestion' => "Set upload_tmp_dir in php.ini to: {$fallbackDir}"
        ];
    }

    if ($file['error'] !== UPLOAD_ERR_OK) {
        return ['success' => false, 'error' => "Upload error: {$file['error']}"];
    }

    $dest = __DIR__ . '/uploads/' . basename($file['name']);
    if (move_uploaded_file($file['tmp_name'], $dest)) {
        return ['success' => true, 'path' => $dest];
    }

    return ['success' => false, 'error' => 'Failed to move uploaded file.'];
}

// Usage
$result = handleUploadWithFallback($_FILES['document']);
header('Content-Type: application/json');
echo json_encode($result);
?>
```

### Fix 4: Check and fix open_basedir restrictions

```php
<?php
// Check if open_basedir is restricting temp directory access
$openBasedir = ini_get('open_basedir');
$tmpDir = ini_get('upload_tmp_dir') ?: sys_get_temp_dir();

echo "open_basedir: " . ($openBasedir ?: 'not set (unrestricted)') . "\n";
echo "upload_tmp_dir: {$tmpDir}\n";

if ($openBasedir) {
    $allowedPaths = explode(':', $openBasedir);
    $isAllowed = false;

    foreach ($allowedPaths as $path) {
        $path = rtrim(trim($path), '/');
        if (strpos($tmpDir, $path) === 0) {
            $isAllowed = true;
            break;
        }
    }

    if (!$isAllowed) {
        echo "WARNING: upload_tmp_dir is outside open_basedir restrictions!\n";
        echo "Add {$tmpDir} to open_basedir in php.ini:\n";
        echo "open_basedir = {$openBasedir}:{$tmpDir}\n";
    }
}
?>
```

## Examples

```php
<?php
// Upload handler with comprehensive temp directory diagnostics
function debugUploadTempDir(): array {
    $diagnostics = [];

    $diagnostics['upload_tmp_dir_value'] = ini_get('upload_tmp_dir') ?: '(not set)';
    $diagnostics['sys_get_temp_dir'] = sys_get_temp_dir();

    $effectiveTmpDir = ini_get('upload_tmp_dir') ?: sys_get_temp_dir();
    $diagnostics['effective_tmp_dir'] = $effectiveTmpDir;
    $diagnostics['dir_exists'] = is_dir($effectiveTmpDir);
    $diagnostics['dir_writable'] = is_writable($effectiveTmpDir);

    if (is_dir($effectiveTmpDir)) {
        $diagnostics['permissions'] = substr(sprintf('%o', fileperms($effectiveTmpDir)), -4);
    }

    // Check open_basedir
    $openBasedir = ini_get('open_basedir');
    $diagnostics['open_basedir'] = $openBasedir ?: '(not set)';

    return $diagnostics;
}

if ($_FILES['document']['error'] === UPLOAD_ERR_NO_TMP_DIR) {
    header('Content-Type: application/json');
    echo json_encode([
        'error' => 'Missing temporary folder',
        'diagnostics' => debugUploadTempDir(),
        'fix' => 'Add this to php.ini: upload_tmp_dir = /var/www/tmp && create directory with proper permissions'
    ], JSON_PRETTY_PRINT);
}
?>
```

## Related Errors

- [UPLOAD_ERR_CANT_WRITE](/languages/php/upload-err-cant-write) — Failed to write to disk
- [UPLOAD_ERR_INI_SIZE](/languages/php/upload-err-ini-size) — File exceeds upload_max_filesize
- [UPLOAD_ERR_PARTIAL](/languages/php/upload-err-partial) — Only partial file was uploaded
