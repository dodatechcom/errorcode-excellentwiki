---
title: "[Solution] PHP 8.1 Filesystem Function Type Requirements"
description: "Fix PHP 8.1 filesystem function parameter type strictness. Pass correct types, handle null, use proper declarations."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1104
---

# PHP 8.1 Filesystem Function Type Requirements

PHP 8.1 enforces stricter type requirements on filesystem functions like `file_get_contents()`, `fopen()`, `file_put_contents()`, and `unlink()`. Passing `null` to parameters that expect `string` triggers deprecation notices, and returning `false` on failure is now more consistent.

## Common Causes

```php
<?php
// Cause 1: Passing null to string parameters
$path = $_GET['file'] ?? null;
$contents = file_get_contents($path); // Deprecated: null to non-nullable param

// Cause 2: Using false return without checking
$content = file_get_contents('nonexistent.txt');
echo strlen($content); // Warning: passing false to strlen()

// Cause 3: Passing null to fopen mode parameter
$mode = null;
$handle = fopen('file.txt', $mode); // Deprecated: null to non-nullable param

// Cause 4: Mismatched parameter types after changes
$path = 123; // int instead of string
file_get_contents($path); // Deprecated: int to string parameter

// Cause 5: Chaining with functions that may return null
$dir = getenv('UPLOAD_DIR'); // returns string|false
$files = scandir($dir); // Warning if $dir is false
```

## How to Fix

### Fix 1: Check for null before calling filesystem functions

```php
<?php
$path = $_GET['file'] ?? null;

if ($path !== null && is_string($path)) {
    $contents = file_get_contents($path);
} else {
    throw new \InvalidArgumentException('Invalid file path');
}

// Or use a default value
$path = $_GET['file'] ?? '/tmp/default.txt';
$contents = file_get_contents($path);
```

### Fix 2: Always check return values before using them

```php
<?php
$content = file_get_contents('config.json');

if ($content === false) {
    throw new \RuntimeException('Failed to read config file');
}

// Now safe to use
$config = json_decode($content, true);

// Same pattern for fopen
$handle = fopen('data.csv', 'r');
if ($handle === false) {
    throw new \RuntimeException('Failed to open file');
}

// Use with try/finally for cleanup
try {
    $handle = fopen('data.csv', 'r');
    if ($handle === false) {
        throw new \RuntimeException('Failed to open file');
    }
    // Process file
} finally {
    if (isset($handle) && is_resource($handle)) {
        fclose($handle);
    }
}
```

### Fix 3: Ensure all parameters are correct types

```php
<?php
// Bad: potentially null or wrong type
$path = $config['upload_path'] ?? null;
$filename = $request->filename;
$fullPath = $path . '/' . $filename;
$handle = fopen($fullPath, 'r');

// Good: validate and cast types
$path = (string) ($config['upload_path'] ?? '/tmp');
$filename = (string) $request->filename;
$fullPath = rtrim($path, '/') . '/' . basename($filename);

if (!is_file($fullPath)) {
    throw new \RuntimeException("File not found: $fullPath");
}

$handle = fopen($fullPath, 'r');
if ($handle === false) {
    throw new \RuntimeException("Cannot open: $fullPath");
}
```

### Fix 4: Handle type mismatches with proper validation

```php
<?php
function safeFileGetContents(string $path, bool $useIncludePath = false): string
{
    $result = file_get_contents($path, $useIncludePath);

    if ($result === false) {
        throw new \RuntimeException("Cannot read file: $path");
    }

    return $result;
}

// Usage
try {
    $config = safeFileGetContents('/etc/app/config.json');
    $data = json_decode($config, true);
} catch (\RuntimeException $e) {
    error_log($e->getMessage());
}
```

## Examples

```php
<?php
// Proper filesystem function usage in PHP 8.1+

// Reading a file with full error handling
function readFileSafely(string $path): string
{
    if (!is_file($path)) {
        throw new \RuntimeException("File not found: $path");
    }

    if (!is_readable($path)) {
        throw new \RuntimeException("File not readable: $path");
    }

    $content = file_get_contents($path);

    if ($content === false) {
        throw new \RuntimeException("Failed to read: $path");
    }

    return $content;
}

// Writing a file with proper type handling
function writeFileSafely(string $path, string $data): void
{
    $dir = dirname($path);

    if (!is_dir($dir)) {
        if (!mkdir($dir, 0755, true)) {
            throw new \RuntimeException("Cannot create directory: $dir");
        }
    }

    $result = file_put_contents($path, $data);

    if ($result === false) {
        throw new \RuntimeException("Failed to write: $path");
    }
}
```

## Related Errors

- [File Permission Error]({{< relref "/languages/php/file-permission-error" >}}) — permission denied
- [File Not Found Error]({{< relref "/languages/php/file-not-found-error" >}}) — file not found
- [Warning File Get Contents Failed]({{< relref "/languages/php/warning-file-get-contents-failed" >}}) — file_get_contents failure
