---
title: "[Solution] PHP Warning: fwrite() — Supplied Argument Is Not a Valid Stream Resource"
description: "Fix PHP Warning: fwrite() supplied argument is not a valid stream resource. Check fopen() return value, verify write mode, handle errors."
languages: ["php"]
severities: ["warning"]
error-types: ["runtime-error"]
weight: 9
---

# PHP Warning: fwrite() — Supplied Argument Is Not a Valid Stream Resource

This warning occurs when `fwrite()` receives a value that is not a valid stream resource. Typically this happens when `fopen()` failed (returned `false`) and the code does not check the return value before writing.

## Common Causes

```php
<?php
// Example 1: Not checking fopen() return value
$handle = fopen("/nonexistent/file.txt", "w");
fwrite($handle, "data");
// Warning: fwrite() expects parameter 1 to be resource, bool given
```

```php
<?php
// Example 2: File already closed
$handle = fopen("data.txt", "w");
fclose($handle);
fwrite($handle, "more data");
// Warning: fwrite(): supplied argument is not a valid stream resource
```

```php
<?php
// Example 3: Wrong variable name
$fh = fopen("log.txt", "a");
fwrite($handle, "entry"); // $handle is undefined, $fh was used
```

```php
<?php
// Example 4: fopen() returned false due to permissions
$handle = fopen("/root/protected.txt", "w");
// $handle is false — fwrite() will warn
fwrite($handle, "secret data");
```

```php
<?php
// Example 5: Stream wrapper failure with remote URL
$handle = fopen("https://example.com/upload", "w");
fwrite($handle, $postData);
// Warning: fwrite(): supplied argument is not a valid stream resource
```

## How to Fix

### Fix 1: Always Check fopen() Return Value

Never use a stream resource without verifying `fopen()` succeeded.

```php
<?php
$handle = fopen("/var/www/data.csv", "w");
if ($handle === false) {
    throw new \RuntimeException("Cannot open file for writing");
}

fwrite($handle, "column1,column2\n");
fclose($handle);
```

### Fix 2: Verify File Is Opened in Write Mode

Ensure the open mode supports writing (`w`, `a`, `r+`, `w+`, `a+`, `x`, `x+`).

```php
<?php
$handle = fopen("data.txt", "r"); // Read-only mode!
if ($handle === false) {
    throw new \RuntimeException("Cannot open file");
}

// WRONG: Writing to a read-only stream
fwrite($handle, "new data"); // Warning: not a valid writable stream

// CORRECT: Use write mode
fclose($handle);
$handle = fopen("data.txt", "w");
fwrite($handle, "new data");
fclose($handle);
```

### Fix 3: Use fwrite() Return Value to Detect Errors

Check the return value of `fwrite()` to confirm bytes were written.

```php
<?php
$handle = fopen("output.txt", "w");
if ($handle === false) {
    throw new \RuntimeException("Cannot open output.txt");
}

$bytesWritten = fwrite($handle, "Hello, World!");
if ($bytesWritten === false) {
    throw new \RuntimeException("fwrite() failed");
}

fclose($handle);
```

### Fix 4: Use a Safe Wrapper Function

Create a reusable function that handles all error cases.

```php
<?php
function safeWrite(string $filepath, string $data, string $mode = "w"): int {
    $handle = @fopen($filepath, $mode);
    if ($handle === false) {
        throw new \RuntimeException("Cannot open {$filepath} in mode {$mode}");
    }

    $bytes = fwrite($handle, $data);
    fclose($handle);

    if ($bytes === false) {
        throw new \RuntimeException("Failed to write to {$filepath}");
    }

    return $bytes;
}

$safeWrite("/var/www/logs/app.log", date('c') . " - Request processed\n", "a");
```

## Examples

```php
<?php
// Scenario: Writing to a log file
$logpath = "/var/www/logs/app.log";

$handle = fopen($logpath, "a");
if ($handle === false) {
    error_log("Cannot open log file: {$logpath}");
    return;
}

$message = sprintf("[%s] User %d performed action\n", date('c'), $userId);
$written = fwrite($handle, $message);

if ($written === false) {
    error_log("Failed to write to log: {$logpath}");
}

fclose($handle);
```

## Related Errors

- [PHP Warning: fopen() Failed](/languages/php/warning-fopen-failed)
- [PHP File Write Error](/languages/php/file-write-error)
- [PHP File Permission Error](/languages/php/file-permission-error)
