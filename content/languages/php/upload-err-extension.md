---
title: "[Solution] PHP UPLOAD_ERR_EXTENSION — Upload Stopped by Extension"
description: "Fix PHP UPLOAD_ERR_EXTENSION (error code 7) by checking upload limits, increasing post_max_size, disabling conflicting extensions, and checking error logs."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 134
---

# PHP UPLOAD_ERR_EXTENSION (Error Code 7) — Upload Stopped by Extension

A PHP extension stopped the file upload. This is a generic error that occurs when a PHP extension (such as suhosin, mod_security, or a custom upload handler) halts the upload process. Unlike other upload errors, this one doesn't have a specific root cause — it depends on which extension is interfering.

## Common Causes

```php
<?php
// Cause 1: suhosin extension enforcing upload limits
// suhosin.upload.max_filesize or suhosin.post.max_value_size exceeded
// These override normal PHP upload settings

// Cause 2: mod_security blocking the upload
// Web application firewall detects potentially malicious upload
// Rules may block certain file types, sizes, or content patterns

// Cause 3: Custom upload handler extension interfering
// Fileinfo, imagemagick, or other extensions processing during upload
// Extension crashes or aborts the upload process

// Cause 4: post_max_size exceeded with multiple variables
// Total POST data (form fields + files) exceeds post_max_size
// PHP kills the entire request, reported as extension error

// Cause 5: memory_limit exhausted during upload processing
// Extension trying to read/process file runs out of memory
?>
```

## How to Fix

### Fix 1: Check and increase post_max_size

```ini
; php.ini
; Increase post_max_size to accommodate total POST data
post_max_size = 128M

; Also increase upload_max_filesize
upload_max_size = 64M

; Ensure memory is sufficient
memory_limit = 256M
```

```php
<?php
// Verify current limits
echo "post_max_size: " . ini_get('post_max_size') . "\n";
echo "upload_max_filesize: " . ini_get('upload_max_filesize') . "\n";
echo "memory_limit: " . ini_get('memory_limit') . "\n";

// Check if post_max_size was the issue
// When post_max_size is exceeded, $_POST and $_FILES are both empty
if (empty($_POST) && empty($_FILES) && $_SERVER['REQUEST_METHOD'] === 'POST') {
    echo "WARNING: Total POST data exceeded post_max_size (" . ini_get('post_max_size') . ")\n";
}
?>
```

### Fix 2: Disable or configure conflicting extensions

```ini
; php.ini — Disable suhosin upload restrictions if safe to do so
; Only relevant if suhosin extension is installed
suhosin.upload.max_filesize = 0        ; 0 = no limit (use with caution)
suhosin.post.max_value_size = 0         ; 0 = no limit (use with caution)
suhosin.upload.disallow_raw = 0         ; Allow raw file uploads
```

```bash
# Check which extensions are loaded
php -m | grep -iE 'suhosin|security|upload'

# Disable suhosin in php.ini (if present and causing issues)
# sudo nano /etc/php/8.2/apache2/php.ini
# Find and comment out: extension=suhosin.so

# Restart web server after changes
sudo systemctl restart apache2
# or
sudo systemctl restart php8.2-fpm
```

### Fix 3: Check mod_security rules

```bash
# Check if mod_security is installed and active
apache2ctl -M 2>/dev/null | grep security
# or
nginx -T 2>/dev/null | grep -i security

# Temporarily disable mod_security for upload endpoint
# In .htaccess:
```

```apache
# .htaccess — Disable mod_security for upload handler
<IfModule mod_security.c>
    SecRuleEngine Off
    SecRule REQUEST_URI "upload.php" "allow,nolog"
</IfModule>
```

### Fix 4: Check PHP error logs for extension details

```php
<?php
// Log extension error details for debugging
function logUploadExtensionError(array $file): void {
    if ($file['error'] === UPLOAD_ERR_EXTENSION) {
        $logEntry = sprintf(
            "[%s] UPLOAD_ERR_EXTENSION: file=%s, size=%d, type=%s, tmp_name=%s\n",
            date('Y-m-d H:i:s'),
            $file['name'],
            $file['size'],
            $file['type'],
            $file['tmp_name']
        );

        // Log to custom error log
        error_log($logEntry, 3, __DIR__ . '/logs/upload_errors.log');

        // Also check PHP's error log location
        $phpLog = ini_get('error_log');
        if ($phpLog) {
            error_log("PHP Upload Extension Error: " . $logEntry, 3, $phpLog);
        }
    }
}

if (isset($_FILES['document'])) {
    logUploadExtensionError($_FILES['document']);
}
?>
```

```bash
# Check PHP error logs for details about which extension caused the error
tail -f /var/log/php/error.log | grep -i upload
# or
tail -f /var/log/apache2/error.log | grep -i upload

# Check for suhosin logs
tail -f /var/log/suhosin.log 2>/dev/null

# Check mod_security audit log
tail -f /var/log/modsec_audit.log 2>/dev/null
```

## Examples

```php
<?php
// Complete upload handler with extension error diagnostics
function handleExtensionError(array $file): array {
    if ($file['error'] !== UPLOAD_ERR_EXTENSION) {
        return null;
    }

    $diagnostics = [
        'error' => 'Upload stopped by a PHP extension.',
        'checks' => []
    ];

    // Check if post_max_size was exceeded
    $totalPostSize = 0;
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        $contentLength = (int)($_SERVER['CONTENT_LENGTH'] ?? 0);
        $postMaxSize = returnBytes(ini_get('post_max_size'));
        $diagnostics['checks']['post_max_size'] = [
            'limit' => ini_get('post_max_size'),
            'limit_bytes' => $postMaxSize,
            'request_size' => $contentLength,
            'exceeded' => $contentLength > $postMaxSize
        ];
    }

    // Check memory limit
    $diagnostics['checks']['memory_limit'] = [
        'limit' => ini_get('memory_limit'),
        'used' => memory_get_usage(true),
        'peak' => memory_get_peak_usage(true)
    ];

    // Check loaded extensions
    $dangerous = ['suhosin'];
    $loaded = get_loaded_extensions();
    $diagnostics['loaded_extensions'] = array_filter($loaded, function ($ext) use ($dangerous) {
        return in_array(strtolower($ext), $dangerous, true);
    });

    // Suggest fixes
    $diagnostics['suggestions'] = [
        'Increase post_max_size in php.ini',
        'Check error logs for which extension blocked the upload',
        'Temporarily disable mod_security rules for upload endpoint',
        'If suhosin is installed, adjust suhosin.upload.max_filesize'
    ];

    return $diagnostics;
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

// Usage
if (isset($_FILES['document']) && $_FILES['document']['error'] === UPLOAD_ERR_EXTENSION) {
    header('Content-Type: application/json');
    echo json_encode(handleExtensionError($_FILES['document']), JSON_PRETTY_PRINT);
}
?>
```

## Related Errors

- [UPLOAD_ERR_INI_SIZE](/languages/php/upload-err-ini-size) — File exceeds upload_max_filesize
- [UPLOAD_ERR_NO_FILE](/languages/php/upload-err-no-file) — No file was uploaded
- [UPLOAD_ERR_CANT_WRITE](/languages/php/upload-err-cant-write) — Failed to write to disk
- [UPLOAD_ERR_NO_TMP_DIR](/languages/php/upload-err-no-tmp-dir) — Missing temporary folder
