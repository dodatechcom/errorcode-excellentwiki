---
title: "[Solution] PHP Session Save Path Not Writable Error"
description: "Fix PHP session save path errors. Resolve 'Session save path not writable' by fixing permissions and configuration."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "php"
tags: ["php", "session", "filesystem"]
severity: "error"
---

# PHP Session Save Path Not Writable Error

## Error Message

```
session_start(): open(/var/lib/php/sessions/sess_abc123, O_RDWR) failed: Permission denied (13)
```

## Common Causes

- The session save path directory does not exist
- The web server user lacks write permission on the session directory
- The session.save_path is configured to a directory owned by a different user

## Solutions

### Solution 1: Fix Session Directory Permissions

Ensure the session save path exists and is writable by the web server user.

```php
<?php
// Check and fix the session save path
$savePath = session_save_path();
echo "Current save path: $savePath\n";

if (!is_dir($savePath)) {
    echo "Directory does not exist. Creating it...\n";
    mkdir($savePath, 0733, true);
}

if (!is_writable($savePath)) {
    echo "Directory is not writable.\n";
    // Terminal fix:
    // sudo chown www-data:www-data /var/lib/php/sessions
    // sudo chmod 733 /var/lib/php/sessions
}

// Now start the session
if (session_start()) {
    echo "Session started successfully\n";
} else {
    echo "Session start failed\n";
}
?>
```

### Solution 2: Use a Custom Session Save Path

Override the default session save path with a writable directory inside your project.

```php
<?php
$customPath = __DIR__ . '/var/sessions';

// Create the directory if it doesn't exist
if (!is_dir($customPath)) {
    mkdir($customPath, 0755, true);
}

// Set the custom path before starting the session
session_save_path($customPath);
session_start();

// Verify it worked
echo "Session ID: " . session_id() . "\n";
echo "Save path: " . session_save_path() . "\n";
echo "File created: " . (file_exists("$customPath/sess_" . session_id()) ? 'yes' : 'no') . "\n";
?>
```

## Prevention Tips

- Run `ls -la /var/lib/php/sessions` to check ownership and permissions
- Consider using Redis or Memcached as a session handler for production
- Set session.gc_maxlifetime appropriately to clean up old session files

## Related Errors

- [Session Start Error]({{< relref "/languages/php/session-start-error" >}})
- [File Permission Error]({{< relref "/languages/php/file-permission-error" >}})
