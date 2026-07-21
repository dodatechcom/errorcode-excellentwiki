---
title: "[Solution] Laravel Log File Permission Error"
description: "Fix Laravel unable to create log file permission denied. Resolve log channel write failures in Laravel."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

This error appears when the logging system cannot write to the log file due to filesystem permission restrictions.

## Common Causes

- Log file exists and is owned by root while the app runs as `www-data`
- The `storage/logs` directory does not exist
- Log file is locked by another process
- Disk is full and cannot write new data
- Log rotation left stale file handles open

## How to Fix

1. Fix directory permissions:

```bash
chmod -R 775 storage/logs
chown -R www-data:www-data storage/logs
```

2. Remove stale log files if disk is full:

```bash
# Truncate the log without deleting
> storage/logs/laravel.log
# Or use log rotation
```

3. Configure daily log rotation in `config/logging.php`:

```php
'channels' => [
    'stack' => [
        'driver' => 'stack',
        'channels' => ['daily'],
        'ignore_exceptions' => false,
    ],
    'daily' => [
        'driver' => 'daily',
        'path' => storage_path('logs/laravel.log'),
        'level' => env('LOG_LEVEL', 'debug'),
        'days' => 14,
    ],
],
```

4. Test write access:

```bash
touch storage/logs/test.log && rm storage/logs/test.log
echo "Permissions OK"
```

## Examples

```php
// Log write fails silently or throws
Log::error('Payment failed', ['order_id' => $order->id]);
// ErrorException: file_put_contents(.../storage/logs/laravel.log): Failed to open stream: Permission denied

// Fallback to stderr for debugging
config(['logging.channels.stderr' => [
    'driver' => 'errorlog',
    'level' => 'debug',
]]);
```
